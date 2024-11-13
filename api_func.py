import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

def credenciales():
    
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    
    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = credenciales)
    
    return sp

def preparamos_url(link):
    return link.split("/"[-1].split("?")[0])

def obtener_tracks(sp, id_albums):
    
    # Diccionario para almacenar los nombres de las canciones y sus IDs por álbum
    album_tracks = {}

    # Iterar por cada ID de álbum para obtener sus tracks
    for a_id in id_albums:
        try:
            # Obtener los tracks del álbum
            tracks = sp.album_tracks(a_id)
            album_tracks[a_id] = {t['name']: t['id'] for t in tracks['items']}
        
        except Exception as e:
            print(f"Error al obtener los tracks del álbum {a_id}: {e}")
            album_tracks[a_id] = {}  # Almacena un álbum vacío si hay un error

    return album_tracks


def song_album(sp, album_id):
    
    # Obtiene las canciones del álbum
    results = sp.album_tracks(album_id)
    tracks = results['items']

    # Construye un diccionario con el nombre de la canción como clave y el ID como valor
    track_dict = {track['name']: track['id'] for track in tracks}

    return track_dict

def song_info(sp, track_dict):
    # Lista para almacenar los IDs de las canciones
    track_ids = list(track_dict.values())
    
    # Llama al endpoint para obtener características de audio de varias canciones
    audio_features_list = sp.audio_features(tracks=track_ids)

    # Claves que queremos eliminar
    keys_to_discard = ['uri', 'track_href', 'analysis_url']

    # Construye un diccionario con el nombre de la canción y sus características de audio, excluyendo las claves no deseadas
    audio_features_dict = {
        track_name: {k: v for k, v in features.items() if k not in keys_to_discard}
        for track_name, features in zip(track_dict.keys(), audio_features_list)
    }

    return audio_features_dict

