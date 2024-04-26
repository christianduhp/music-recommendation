import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


def setup_spotify_authentication(client_id, client_secret, redirect_uri):
    """
    Set up Spotify authentication and return a Spotify API client.

    Args:
        client_id (str): Spotify client ID.
        client_secret (str): Spotify client secret.
        redirect_uri (str): The redirect URI for the Spotify OAuth flow.

    Returns:
        spotipy.Spotify: A Spotify API client instance.
    """
    try:
        # Scopes for Spotify API access
        scope = "user-library-read playlist-modify-private"
        
        # Spotify OAuth instance
        OAuth = SpotifyOAuth(
            scope=scope,         
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret
        )

        # Spotify client credentials manager
        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        
        # Creating Spotify API client
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        return sp

    except Exception as e:
        print("Error:", e)
        return None
