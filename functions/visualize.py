import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from skimage import io

def show_plotly_express(data, x, y, title):
    fig = px.line(data_frame = data, x = x, y = y, markers = True, title = title)
    fig.show()

def show_plotly_graph_objects(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data['year'], y = data['acousticness'], name = 'Acousticness'))
    fig.add_trace(go.Scatter(x = data['year'], y = data['valence'], name = 'Valence'))
    fig.add_trace(go.Scatter(x = data['year'], y = data['danceability'], name = 'Danceability'))
    fig.add_trace(go.Scatter(x = data['year'], y = data['energy'], name = 'Energy'))
    fig.add_trace(go.Scatter(x = data['year'], y = data['instrumentalness'], name = 'Instrumentalness'))
    fig.add_trace(go.Scatter(x = data['year'], y = data['liveness'], name = 'Liveness'))
    fig.add_trace(go.Scatter(x = data['year'], y = data['speechiness'], name = 'Speechiness'))
    fig = px.imshow(data.corr(), text_auto=True)
    fig.show()

def show_cluster(projection, hover_column_value, x='x', y='y'):
    fig = px.scatter(projection, x = x, y = y, color = 'cluster_pca', hover_data=[x, y, hover_column_value])
    fig.show()  

def visualize_songs(name, url):
    num_images = len(url)
    num_columns = 5

    # Calculate the number of rows needed for the subplot grid
    num_rows = (num_images + num_columns - 1) // num_columns

    fig, axes = plt.subplots(num_rows, num_columns, figsize=(15, 10))

    for i, (song_name, img_url) in enumerate(zip(name, url)):
        ax = axes[i // num_columns, i % num_columns]

        # Read the image using scikit-image
        image = io.imread(img_url)

        ax.imshow(image)
        ax.set_title(song_name, fontsize=8)

        # Hide axis labels and ticks
        ax.axis('off')

    # Remove any empty subplots if there are more than needed
    for i in range(num_images, num_columns * num_rows):
        fig.delaxes(axes[i // num_columns, i % num_columns])

    # Adjust subplot layout
    plt.tight_layout()

    # Display the plot
    plt.show()