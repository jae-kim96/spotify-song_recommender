from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests

from util import get_auth, get_audio_feats, get_users_songs
from model import Model
from recommender import Recommender

user = 'ywze3yhb7ati7k9lxo6pwlori'

# app = Flask(__name__)

# @app.route('/')
# def index():

#     return render_template('index.html')

# @app.route('/playlistInfoReturn/<data>')
# def playlist_return(data):
#     # name = info['name']
#     num_playlists = data['num_playlists']

#     # return render_template('playlistReturn.html', userID = name, num_playlists = num_playlists)
#     return render_template('playlistReturn.html', num_playlists = num_playlists)

# @app.route('/playlistInfo', methods = ['POST', 'GET'])
# def get_playlists():
#     user = ''
    
#     if request.method == 'POST':
#         user = request.form["userID"]

#         # util functions to get data from spotify API
#         auth = get_auth(user)
#         songs, num_playlists = get_users_songs(auth)
#         # print(num_playlists)
#         # scaled_df = get_audio_feats(songs)

#         # # model class 
#         # model = Model()
#         # user_model = model.build_model(scaled_df, num_playlists)

#         # # recommender class
#         data = {'name': user, 'num_playlist': num_playlists}
#         # print(data)
#         return redirect(url_for('playlist_return', data = data))
#     elif request.method == 'GET':
#         return render_template('playlist.html')

def main():
    # util functions to get data from spotify API
    auth = get_auth(user)
    print(auth)
    songs, num_playlists = get_users_songs(auth)
    scaled_df = get_audio_feats(auth, songs)

    print(scaled_df)

    # # model class 
    # model = Model()
    # user_model = model.build_model(scaled_df, num_playlists)
    # rec = Recommender()
    # rec.get_recommendations(user_model, auth)

if __name__ == "__main__":
    # app.run(debug = True)
    main()