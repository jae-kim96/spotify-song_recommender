import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError
import spotipy.util as sp


class userAuth:
    username = ""
    
    clientID = "7d5c137ab5154cf1a3ff64ae97a85c74"
    secret = "7bf61d8df66b4b6e98881d94721f095c"
    redirect = "http://localhost:7777/callback"
    scope = "user-read-recently-played%20playlist-read-private"
    
    auth = None
    token = ""
    refreshToken = ""
    response = None

    # Constructor to set constants like clientID and secretClientID and redirect URL
    def __init__(self, userID):
        self.auth = SpotifyOAuth(client_id = self.clientID, client_secret = self.secret, redirect_uri = self.redirect, scope = self.scope, username = userID, open_browser = True)
        self.username = userID
       

    # API Call to Token Endpoint and sets the innate vlaues as well
    def getToken(self):
        self.response = self.auth.get_access_token()
        
        self.token = self.response["access_token"]
        self.refreshToken = self.response["refresh_token"]
        #print(self.token)
        return self.token, self.refreshToken

    def refreshUserToken(self, refreshToken):
        self.response = self.auth.refresh_access_token(refreshToken)
        #print(response)
        return self.response

    def isTokenExpired(self):
        try:
            self.auth.is_token_expired(self.response)
            return True
        except (SpotifyOauthError):
            return False
        except TypeError:
            return "None Type Error"
        
        #return self.auth.is_token_expired(self.response)

    def updateToken(self, newToken, refreshToken):
        self.token = newToken
        self.refreshToken = refreshToken

