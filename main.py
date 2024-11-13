# %%
import api_func as api
sp = api.credenciales()

# %%
artist_url = 'https://open.spotify.com/intl-es/artist/0UAAJKwQZz8jVDoVtly8NA?si=dKWEGg5oRV-zgPQSrs40hQ'
tracks_df = api.get_artist_tracks(sp, artist_url)
#%%
# Obtener los IDs de las canciones para extraer sus features
track_ids = tracks_df['track_id'].tolist()
features_df = api.get_track_features(sp, track_ids)
# %%
# Cargar los CSV como DataFrames
tracks_df = pd.read_csv('artist_tracks.csv')
features_df = pd.read_csv('track_features.csv')

#