from spotify_dl.spotify import parse_spotify_url, get_item_name, fetch_tracks
import spotipy
import base64
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl import youtube as yt
import os

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=base64.b64decode('NjliZDE4ZjNiNDY3NGMyNTkwNTllMzE5YTQ1ZGQwMzY=').decode('ascii'),
                                                                    client_secret=base64.b64decode('NTczY2UwYmM2OWUzNDdkNzg3NjgwZDBlMzJmOTQ3MGM=').decode('ascii')))

#plalist LAURA
# url = "https://open.spotify.com/playlist/1yCV1hqPDP1RCCogvcmaqh?si=kkiXqXOkTcKVwWP6qStNXg&utm_source=copy-link&dl_branch=1"

print("Colocar o link de uma playlist do spotify")
url = input()
link = url[:5]

item_type = "playlist"
songs = fetch_tracks(sp, item_type, url)
print(type(songs))

yt.download_songs(songs, download_directory="C:\\Users\\SAMSUNG\\Desktop\\APPS-PROGRMACAO\\Nova pasta\\pastaSpotify", format_string='best',skip_mp3=False, keep_playlist_order=False)
