import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA

from .clustering_utils import SEED, cluster_with_kmeans

seed_value = SEED()

def preprocess_music_data(data,column):
    try:
        ohe = OneHotEncoder(dtype=int)
        ohe_columns = ohe.fit_transform(data[[column]]).toarray()
        data = data.drop(column, axis=1)
    
        data_dummies_music = pd.concat([data, pd.DataFrame(ohe_columns, columns=ohe.get_feature_names_out([column]))], axis=1)

        # Create a pipeline with two steps: standardization and dimensionality reduction (PCA)
        pipeline = Pipeline([
            ('scaler', StandardScaler()),   # Standardization step
            ('PCA', PCA(n_components=0.7, random_state=seed_value))   # PCA step with 2 principal components 
        ])

        music_embedding_pca = pipeline.fit_transform(data_dummies_music.drop(['id','name', 'artists_song'], axis=1))

        projection = pd.DataFrame(data=music_embedding_pca)
        components = pipeline[1].n_components_ 
        var_exp  = pipeline[1].explained_variance_ratio_.sum()
        return projection, components, var_exp 
    except Exception as e:
        print(f"An error occurred during preprocess music data: {e}")
        return None, None, None

def clustering_music_projection(data):
    try:
        # Step 1: Preprocess the data and apply PCA for dimensionality reduction
        projection, components, var_exp = preprocess_music_data(data, 'artists')
        
        # Step 2: Cluster data using K-Means on PCA-projected data
        _, projection = cluster_with_kmeans(data, projection, n_clusters=50)
        
        # Step 3: Add 'artists' and 'song' column to the projection DataFrame
        projection['song'] = data['artists_song']
        projection['artists'] = data['artists']
        projection_shape = projection.shape
        return projection, components, var_exp, projection_shape
    
    except Exception as e:
        print(f"An error occurred during music clustering projection: {e}")
        return None, None, None, None
    