# %%
import api_func as api
sp = api.credenciales()
import pandas as pd
#%% 
prueba = api.obtener_tracks(sp=sp, id_albums='494aUGKXMH5ruXtR3O1a3H')
# %%
id_albums = [['494aUGKXMH5ruXtR3O1a3H'], ['1X472EvsSqH09RyrqbtyXU'], ['3Q9wXhEAX7NYCPP0hxIuDz'], 
             ['28DUZ0itKISf2sr6hlseMy'], ['0zcNtUZ2oEpRmiDuWBFvcX'], ['5Eevxp2BCbWq25ZdiXRwYd'], 
             ['6hU9JCoqq4GjYq86dQ1o9b'], ['3XB2yloP7l00tEUmaODtVi'], ['2FUsvD1bw53HGOjAg56vRD'], 
             ['7qRKpkP0jSOlBMLYZhAMCh'], ['4XHIjbhjRmqWlosjj5rqSI'], ['0hJ3A7sih1AXDoMjXHLr7Q'], 
             ['7IYqppCBhR5z9z8JqgXuxi'], ['4flcwtqnLoKZJ2wrCp1aJq'], ['1FiRqhpAowNK8gTl5sOhxZ'], 
             ['4fy0SXW5G8evBCo2A3kn02'], ['5uvXx5ZQswNRFCdHR521YZ'], ['72seWTJF9U5SljizfyF2ZK'], 
             ['4JtIVJRA342O0YoAchen5Q'], ['7pgs38iLfEqUtwgCRgvbND']]


album_tracks = api.obtener_tracks(sp, id_albums)
# %%
album_tracks
# %%
album_id = '494aUGKXMH5ruXtR3O1a3H'
canciones = api.song_album(sp, album_id)
print(canciones)
# %%
canciones
#%%
asd = api.song_info(sp, canciones)


# %%
asd
# %%
df = pd.DataFrame(asd).T
# %%
df
# %%
song = pd.DataFrame([canciones]).T

# %%
song
# %%
