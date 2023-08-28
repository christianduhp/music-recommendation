# Music Recommendation System

This is a music recommendation system project that utilizes Spotify data to recommend songs based on an input track. The project encompasses various functionalities, including data preprocessing, visualization, and machine learning with clustering methods, alongside Spotify authentication.

## Prerequisites

Before running this project, ensure that you have the following prerequisites installed:

- Python 3.x
- Python libraries: pandas, scikit-learn, spotipy, plotly, matplotlib, scikit-image

### Spotify Configuration

You'll also need Spotify credentials for authentication. Follow the steps below to set up your credentials:

1. Access [Spotify for Developers](https://developer.spotify.com/dashboard/) and log in or create an account.
2. Create an app in the Spotify Dashboard and obtain your Client ID and Client Secret.
3. In the `spotify/config.json` file, replace `'YOUR_CLIENT_ID'`, `'YOUR_CLIENT_SECRET'` and `'REDIRECT_URI'` with your credentials.

## Project Structure

The project structure is organized as follows:

```
music_recommendation_project/
│
├── data/
│   ├── all_data.csv           # All data
│   ├── data_by_genres.csv     # Data by Genres
│   └── data_by_years.csv      # Data by Years
│
├── functions/
│   ├── __init__.py            # Python package indicating that 'functions' is a package
│   ├── preprocess.py          # Data preprocessing functions
│   ├── visualize.py           # Data visualization functions
│   ├── clustering_genres.py   # Functions for genre clustering
│   └── clustering_music.py    # Functions for music clustering
│
├── spotify/
│   ├── __init__.py            # Python package indicating that 'spotify' is a package
│   ├── auth.py                # Spotify authentication functions
│   ├── config.json            # Json file with your Sportify credentials
│   └── recommendations.py     # Music recommendation functions
│
├── main.py                     # Main file that executes the code
├── README.md                   # This README file
├── LICENSE                     # Project license
└── requirements.txt            # Python dependencies list
```

## Features

This project offers the following features:

### Data Preprocessing

- `functions/preprocess.py` contains functions to load and preprocess data, including removing unnecessary columns and filtering data by year.

### Visualization

- `functions/visualize.py` includes functions for data visualization, such as line charts, clusters and displaying images of music album covers.

### Spotify Authentication

- `spotify/auth.py` provides functions for authenticating with Spotify using the provided credentials.

### Music Recommendation

- `spotify/recommendations.py` contains functions to recommend music based on an input track. The recommendation is made based on the similarity of songs.

### Clustering

- `functions/clustering_genres.py` and `functions/clustering_music.py` perform clustering on data using PCA and K-Means, grouping songs by genre and musical characteristics, respectively.

## Usage

To use this music recommendation system, follow the instructions below:

1. Clone this repository to your local environment:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Spotify credentials in the `config.py` file:

   ```python
   client_id = 'YOUR_CLIENT_ID'
   client_secret = 'YOUR_CLIENT_SECRET'
   ```

4. Run the `main.py` file to use the music recommendation system and explore the project's functionalities:

   ```bash
   python main.py
   ```

5. When running the script, you can choose a music track for recommendation by modifying the `music_name` variable in the `main.py` file. For example:

   ```python
   music_name = 'Ariana Grande - 7 rings'  # Replace with the name of your desired input track
   ```

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
![Music Recommendation](https://github.com/christianduhp/music-recommendation/assets/85292359/433ce0da-60a5-4632-84a9-4cd7f89ae725)
