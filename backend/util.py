import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

from sklearn import preprocessing

import pandas as pd

client_id = "2da0df410e3d4e08843ced8b5fd4e407"
secret = "e9f263214c714293b6d1e59ad35fb7bd"
redirect = "http://127.0.0.1:5000/"
# redirect = 'http://google.com'
scope = "user-read-recently-played%20playlist-read-private"

user = ""

def get_auth(username):
    '''
    A function to take a username and return a spotify auth object for use
    '''
    user = username
    auth = SpotifyOAuth(scope = scope,
                    redirect_uri = redirect,
                    client_id = client_id,
                    client_secret = secret,
                    username = user)
    # print(auth.get_auth_response())
    sp_auth = sp.Spotify(auth_manager = auth)
    return sp_auth

def get_users_songs(sp_auth):
    '''
    A function to get the songs that are in a users playlists.
    Returns songs by the unique spotify song id
    '''
    playlists_resp = sp_auth.current_user_playlists()

    song_list = list()

    for item in playlists_resp['items']:
        list_id = item['id']

        offset = 0
        while True:
            song_resp = sp_auth.playlist_items(playlist_id = list_id, offset = offset, limit = None)
            
            for song in song_resp['items']:
                song_list.append(song['track']['id'])

            # Offset is here because it can only send 100 songs at a time
            if song_resp['next'] is None:
                break
            else:
                offset += 100
    # print('-------------------------------------------')
    # print(len(song_list))
    # print(len(playlists_resp['items']))
    num_playlists = len(playlists_resp['items'])
    return song_list, num_playlists

def get_audio_feats(sp_auth, song_list):
    '''
    Getting the audio features from the song meta-data available from the Spotify API
    features are returned as a Pandas DF
    '''
    audio_feat = list()

    # print(song_list)
    i = 0
    while i < len(song_list):
        # print(sp.audio_features(i))
        try:
            curr = song_list[i]
            audio_feat.append(sp_auth.audio_features(curr)[0])
            i += 1
        except:
            i += 2

    features_list = list()

    for features in audio_feat:
        try:
            features_list.append([features['danceability'], features['energy'], features['key'], 
                                    features['loudness'], features['mode'], features['speechiness'], 
                                    features['acousticness'], features['instrumentalness'], 
                                    features['liveness'], features['valence'], features['tempo'], 
                                    features['id']])
        except:
            break

    features_df = pd.DataFrame(features_list, columns = ['danceability', 'energy', 'key', 
                    'loudness', 'mode', 'speechiness', 'acousticness',  'instrumentalness', 
                    'liveness', 'valence', 'tempo', 'id'])

    feature_vals = features_df[['danceability', 'energy', 'key', 'loudness', 'mode', 
                                'speechiness', 'acousticness',  'instrumentalness', 'liveness', 
                                'valence', 'tempo']]

    cols = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
            'instrumentalness', 'liveness', 'valence', 'tempo']
    
    x = feature_vals.values
    scaler = preprocessing.MinMaxScaler()
    x_scaled = scaler.fit_transform(x)

    scaled_df = pd.DataFrame(x_scaled, columns = cols)

    return scaled_df