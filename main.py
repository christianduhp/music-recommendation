from functions.preprocess import preprocess_data, preprocess_data_by_genres, preprocess_data_by_years
from functions.visualize import visualize_songs
from functions.clustering_genres import clustering_genre_projection
from functions.clustering_music import clustering_music_projection
from spotify.recommendations import recommend_id, recommend_music

music_name = 'Ariana Grande - 7 rings'

data = preprocess_data('data/all_data.csv')
data_by_genres = preprocess_data_by_genres('data/data_by_genres.csv')
data_by_years = preprocess_data_by_years('data/data_by_years.csv')

projection, components, var_exp, projection_shape= clustering_genre_projection(data_by_genres)
projection_v2, components_v2, var_exp_v2, projection_shape_v2 = clustering_music_projection(data)

def analytics():
    print(f"\nGenre Data: \nComponents = {components} \nTotal explained variance = {round(var_exp * 100,3)}%")
    print(f"\nMusic Data: \nComponents = {components_v2} \nTotal explained variance = {round(var_exp_v2 * 100,3)}% \n")

if __name__ == "__main__":
    analytics()
    playlst_id = recommend_music(music_name, projection_v2, data)['id']
    name, url = recommend_id(playlst_id)
    visualize_songs(name, url) 

