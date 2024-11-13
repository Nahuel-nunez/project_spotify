import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd
import csv
import re
from datetime import datetime

load_dotenv()

def credenciales():
    
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    
    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = credenciales)
    return sp

def url_artista(url):
    match = re.search(r'artist/([a-zA-Z0-9]+)', url)
    if match:
        return match.group(1)
    else:
        print("URL no válida.")
        return None

def get_artist_tracks(sp, artist_url, csv_filename='artist_tracks.csv'):
    """
    Obtiene toda la información de álbumes y canciones de un artista dado su URL y la guarda en un archivo CSV.
    """
    # Obtener el ID del artista desde la URL
    artist_id = url_artista(artist_url)
    if not artist_id:
        print("ID de artista no encontrado.")
        return

    all_tracks = []

    # Obtener álbumes del artista
    albums = sp.artist_albums(artist_id, album_type='album,single')
    album_items = albums['items']

    for album in album_items:
        album_id = album['id']
        album_name = album['name']
        album_release_date = album['release_date']
        album_tracks = sp.album_tracks(album_id)['items']
        
        for track in album_tracks:
            track_info = {
                'album': album_name,
                'album_release_date': album_release_date,
                'track_name': track['name'],
                'track_id': track['id']
            }
            all_tracks.append(track_info)

    # Guardar los datos en CSV
    df_tracks = pd.DataFrame(all_tracks)
    df_tracks.to_csv(csv_filename, index=False)
    print(f"Datos de álbumes y canciones guardados en {csv_filename}")
    
    return df_tracks  # También devolvemos el DataFrame si necesitas hacer más operaciones


def get_track_features(sp, track_ids, csv_filename='track_features.csv'):
    """
    Obtiene los "features" de una lista de canciones y los guarda en un archivo CSV.
    """
    all_features = []

    for track_id in track_ids:
        track = sp.track(track_id)
        features = sp.audio_features(track_id)[0]
        
        if features:  # Evitar errores si no hay características disponibles
            track_features = {
                'track_name': track['name'],
                'artist': [artist['name'] for artist in track['artists']],
                'danceability': features['danceability'],
                'energy': features['energy'],
                'key': features['key'],
                'loudness': features['loudness'],
                'mode': features['mode'],
                'speechiness': features['speechiness'],
                'acousticness': features['acousticness'],
                'instrumentalness': features['instrumentalness'],
                'liveness': features['liveness'],
                'valence': features['valence'],
                'tempo': features['tempo'],
                'duration_ms': features['duration_ms'],
                'time_signature': features['time_signature']
            }
            all_features.append(track_features)

    # Guardar los datos en CSV
    df_features = pd.DataFrame(all_features)
    df_features.to_csv(csv_filename, index=False)
    print(f"Datos de features guardados en {csv_filename}")
    
    return df_features  # También devolvemos el DataFrame si necesitas hacer más operaciones





