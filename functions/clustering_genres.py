import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from .clustering_utils import SEED, cluster_with_kmeans

seed_value = SEED()

def preprocess_genre_data(data):
    """
    Preprocess the data and apply PCA for dimensionality reduction.

    Parameters:
    - data (DataFrame): The input data.
    - n_components: Int | float | str | None

    Returns:
    - projection (DataFrame): DataFrame with PCA projection.
    - components (int): Number of principal components retained.
    - var_exp (float): Total explained variance by the retained components.
    """
    try:
        # Create a pipeline with two steps: standardization and dimensionality reduction (PCA)
        pipeline = Pipeline([
            ('scaler', StandardScaler()),   # Standardization step
            ('PCA', PCA(n_components=2, random_state= seed_value))   # PCA step with 2 principal components 
        ])

        genre_embedding_pca = pipeline.fit_transform(data)
        projection = pd.DataFrame(columns=['x', 'y'], data=genre_embedding_pca)
        components = pipeline[1].n_components_ 
        var_exp  = pipeline[1].explained_variance_ratio_.sum()
        return projection, components, var_exp 

    except Exception as e:
        print(f"An error occurred during preprocess genre data: {e}")
        return None, None, None

def clustering_genre_projection(data):
    try:
        # Step 1: Remove genres from 'data_by_genres'
        data_v1 = data.drop('genres', axis = 1)

        # Step 2: Preprocess the data and apply PCA for dimensionality reduction
        projection, components, var_exp = preprocess_genre_data(data_v1)
        
        # Step 3: Cluster data using K-Means on PCA-projected data
        _, projection = cluster_with_kmeans(data_v1, projection)
        
        # Step 4: Add 'genres' column to the projection DataFrame
        projection['genres'] = data['genres']
        projection_shape = projection.shape
        return projection, components, var_exp, projection_shape
    
    except Exception as e:
        print(f"An error occurred during genre clustering projection: {e}")
        return None, None, None, None
