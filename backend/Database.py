import sqlite3
from sqlite3 import Error

class DB:
    # Database constructor to open a connection
    def __init__(self):
        try:
            self.conn = sqlite3.connect(r"C:\Users\jayki\Desktop\spotifyProject\backend\database\spotifyProject.db", uri = True)
            #print("Database exists and connection has been made")
        except Error as e:
            print(e)
        
    def closeConn(self):
        if self.conn:
            self.conn.close()

    # For keeping track of Users
    def createUsersTable(self):
        createSQL = '''
                        CREATE TABLE IF NOT EXISTS users (
                            userID text PRIMARY KEY,
                            name text,
                            token text NOT NULL,
                            refreshToken text NOT NULL
                        )
                    '''    
        try:
            c = self.conn.cursor()
            c.execute(createSQL)
            #print("Users Table created or already exists!")
        except Error as e:
            print(e)

    def insertUserData(self, userID, name, token, refreshToken):
        insertSQL = '''
                    INSERT INTO users (userID, name, token, refreshToken)
                    VALUES (?, ?, ?, ?)
                    '''
        data = (userID, name, token, refreshToken)

        try:
            c = self.conn.cursor()
            c.execute(insertSQL, data)
            self.conn.commit()
            #print("SQL executed")
        except Error as e:
            print(e)

    def userSearch(self, userID):
        searchSQL = '''
                    SELECT *
                    FROM users
                    WHERE userID = ?
                    '''

        data = (userID, ) # Need to add comma when passing in the where clause

        exist = False
        try:
            c = self.conn.cursor()
            c.execute(searchSQL, data)
            rows = c.fetchall()
            if len(rows) > 0:
                exist = True
        except Error as e:
            print(e)

        return exist

    def getUsers(self):
        searchSQL = '''
                    SELECT *
                    FROM users
                    '''

        try:
            c = self.conn.cursor()
            c.execute(searchSQL)
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)


    def getTokens(self, userID):
        searchSQL = '''
                    SELECT token, refreshToken
                    FROM users
                    WHERE userID = ?
                    '''
        data = (userID, )

        try:
            c = self.conn.cursor()
            c.execute(searchSQL, data)
            rows = c.fetchall()
            #print(rows)
            return rows
        except Error as e:
            print(e)

    def updateTokens(self, token, refreshToken, userID):
        updateSQL = '''
                    UPDATE users
                    SET token = ?, refreshToken = ?
                    WHERE userID = ?
                    '''
        
        data = (token, refreshToken, userID)
        
        try:
            c = self.conn.cursor()
            c.execute(updateSQL, data)
        except Error as e:
            print(e)

    # Databse work on storing playlist information
    def createPlaylistTable(self):
        createSQL = '''
                        CREATE TABLE IF NOT EXISTS playlists (
                            id text PRIMARY KEY,
                            name text NOT NULL,
                            userID text NOT NULL,
                            ownerName text,
                            ownerURL text,
                            playlistURL text
                        );
                        '''
        try:
            c = self.conn.cursor()
            c.execute(createSQL)
            #print("Playlist Table created or already exists!")
        except Error as e:
            print(e)


    def insertPlaylistData(self, playID, name, userID, ownerName, ownerURL, playlistURL):
        insertSQL = '''
                    INSERT INTO playlists (id, name, userID, ownerName, ownerURL, playlistURL)
                    VALUES (?, ?, ?, ?, ?, ?)
                    '''
        data = (playID, name, userID, ownerName, ownerURL, playlistURL)
        try:
            c = self.conn.cursor()
            c.execute(insertSQL, data)
            self.conn.commit()
            #print("SQL executed")
        except Error as e:
            print(e)

    # Get Playlist IDs for specified userID
    def getPlaylists(self, userID):
        selectSQL = '''
                    SELECT *
                    FROM playlists
                    WHERE userID = ?
                    '''

        data = (userID, ) # Need to add comma when passing in the where clause

        try:
            c = self.conn.cursor()
            c.execute(selectSQL, data)
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    def getPlaylistFromName(self, playlist):
        selectSQL = '''
                    SELECT *
                    FROM playlists
                    WHERE name = ?
                    '''

        data = (playlist, ) # Need to add comma when passing in the where clause

        try:
            c = self.conn.cursor()
            c.execute(selectSQL, data)
            rows = c.fetchall()
            print(rows)
            return rows
        except Error as e:
            print(e)

    def createSongsTable(self):
        createSQL = '''
                    CREATE TABLE IF NOT EXISTS songs (
                        playlistID text,
                        songID text,
                        songName text,
                        artistID text,
                        artistName text,
                        userID text
                    )
                    '''
        try:
            c = self.conn.cursor()
            c.execute(createSQL)
            #print("Playlist Table created or already exists!")
        except Error as e:
            print(e)

    def insertSongs(self, playlistID, songID, songName,  artistID, artistName, userID):
        insertSQL = '''
                    INSERT INTO songs (playlistID, songID, songName, artistID, artistName, userID)
                    VALUES (?, ?, ?, ?, ?, ?)
                    '''
        data = (playlistID, songID, songName,  artistID, artistName, userID)
        try:
            c = self.conn.cursor()
            c.execute(insertSQL, data)
            self.conn.commit()
            #print("SQL executed")
        except Error as e:
            print(e)

    def getSongs(self, userID, playlistID):
        selectSQL = '''
                    SELECT songID
                    FROM playlists
                    WHERE userID = ? AND playlistID = ?
                    '''

        data = (userID, playlistID,)

        try:
            c = self.conn.cursor()
            c.execute(selectSQL, data)
            rows = c.fetchall()
            print(rows)
            return rows
        except Error as e:
            print(e)







