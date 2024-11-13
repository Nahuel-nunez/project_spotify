import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def credenciales():
    
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    
    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = credenciales)
    
    return sp

# def preparamos_url(link):
#     return link.split("/"[-1].split("?")[0])

def albums_artista(sp, artist_id):
    # Lista para almacenar información de los álbumes
    albums_info = []

    # Obtiene los álbumes del artista
    results = sp.artist_albums(artist_id, album_type='album')
    albums = results['items']

    # Procesa cada álbum para extraer la información deseada
    for album in albums:
        album_info = {
            'nombre': album['name'],
            'id_album': album['id'],
            'fecha_lanzamiento': album['release_date'],
            'tipo_album': album['album_type'],
            'cantidad_tracks': album['total_tracks']
        }
        albums_info.append(album_info)

    return albums_info

def aislar_id_albums(albums_info):
    # Lista para almacenar los ids de los álbumes
    id_albums = []
    
    # Recorre cada álbum en la lista y extrae el id_album
    for album in albums_info:
        id_albums.append(album["id_album"])
    
    # Devuelve la lista de ids
    return id_albums

def album_tracks_info(sp, album_ids):
    # Lista para almacenar información de las canciones de todos los álbumes
    tracks_info = []

    # Itera sobre cada álbum usando su ID
    for album_id in album_ids:
        # Obtiene las canciones del álbum
        results = sp.album_tracks(album_id)
        tracks = results['items']

        # Procesa cada canción para extraer la información deseada
        for track in tracks:
            track_info = {
                'album_id': album_id,
                'track_name': track['name'],
                'track_id': track['id'],
                'duration_ms': track['duration_ms'],
                'explicit': track['explicit'],
                'track_number': track['track_number']
            }
            tracks_info.append(track_info)

    return tracks_info

def aislar_id_tracks(album_tracks_info):
    # Lista para almacenar los ids de los tracks
    id_tracks = []
    
    # Recorre cada álbum en la lista y extrae el id_track
    for album in album_tracks_info:
        id_tracks.append(album["track_id"])
    
    # Devuelve la lista de ids
    return id_tracks

# def tracks_info(sp, track_dict):
#     # Lista para almacenar los IDs de las canciones
#     track_ids = list(track_dict.values())
    
#     # Llama al endpoint para obtener características de audio de varias canciones
#     audio_features_list = sp.audio_features(tracks=track_ids)

#     # Claves que queremos eliminar
#     keys_to_discard = ['uri', 'track_href', 'analysis_url']

#     # Construye un diccionario con el nombre de la canción y sus características de audio, excluyendo las claves no deseadas
#     audio_features_dict = {
#         track_name: {k: v for k, v in features.items() if k not in keys_to_discard}
#         for track_name, features in zip(track_dict.keys(), audio_features_list)
#     }

#     return audio_features_dict

def tracks_info(sp, track_list):
    # Llama al endpoint para obtener características de audio de las canciones
    audio_features_list = sp.audio_features(tracks=track_list)

    # Claves que queremos eliminar
    keys_to_discard = ['uri', 'track_href', 'analysis_url']

    # Construye un diccionario con el ID de la canción y sus características de audio, excluyendo las claves no deseadas
    audio_features_dict = {}

    for track_id, features in zip(track_list, audio_features_list):
        # Crear un diccionario filtrado para las características de la canción actual
        filtered_features = {}
        for k, v in features.items():
            if k not in keys_to_discard:
                filtered_features[k] = v
        # Asocia el track_id con sus características de audio filtradas
        audio_features_dict[track_id] = filtered_features

    return audio_features_dict


