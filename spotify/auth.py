import spotipy
import json

from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def setup_spotify_authentication(config_file_path):
    """
    Set up Spotify authentication and return a Spotify API client.

    Args:
        config_file_path (str): The path to the Spotify API configuration file.
        redirect_uri (str): The redirect URI for the Spotify OAuth flow.

    Returns:
        spotipy.Spotify: A Spotify API client instance.
    """
    try:
        # Reading credentials from the configuration file
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)

        # Extracting Spotify client credentials from the configuration
        client_id = config_data['SPOTIFY_CLIENT_ID']
        client_secret = config_data['SPOTIFY_CLIENT_SECRET']
        redirect_uri = config_data['REDIRECT_URI']
        scope = "user-library-read playlist-modify-private"
        
        OAuth = SpotifyOAuth(
            scope=scope,         
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret
        )

        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        return sp

    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return None
    except KeyError:
        print("Error: Invalid configuration data.")
        return None






