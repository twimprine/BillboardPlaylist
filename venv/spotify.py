class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token


    def create_playlist(self):
        request_body = json.dumps({
            "name": "Wedding Playlist",
            "description": "General Wedding Music",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        #playlist id
        return response_json["id"]




    def get_spotify_uri():
        pass