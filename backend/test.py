import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

def test():
    user = 'ywze3yhb7ati7k9lxo6pwlori'

    client_id = "7d5c137ab5154cf1a3ff64ae97a85c74"
    secret = "7bf61d8df66b4b6e98881d94721f095c"
    redirect = "http://http://127.0.0.1:5000/"
    scope = "user-read-recently-played%20playlist-read-private"

    auth = SpotifyOAuth(scope = scope,
                    redirect_uri = redirect,
                    client_id = client_id,
                    client_secret = secret,
                    username = user)
    sp_auth = sp.Spotify(auth_manager = auth)

    playlists_resp = sp_auth.current_user_playlists()
    print(playlists_resp)

    pass


if __name__ == "__main__":
    test()