from sklearn.cluster import KMeans
from sklearn import metrics

import spotipy as sp

class Recommender:
    def __init__(self):
        pass

    def get_recommendations(self, model, sp_auth):
        '''
        A function to get the recommendations for a user based on a clustering model from the
        users playlist.

        Going to recommend off of Spotify's top new songs
        '''
        # Use spotipy featured_playlists and new_releases to run through the clustering model
        playlists = sp_auth.featured_playlists(limit = 50)
        print(playlists)

        pass

    