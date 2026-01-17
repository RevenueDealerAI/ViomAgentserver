"""
Generate OAuth Token for Google Calendar
Run this script ONCE on a machine with a web browser to generate token.json
"""

from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def generate_token():
    """
    Generate OAuth token for Google Calendar API.
    This will open a browser window for authentication.
    """
    
    # Check if credentials.json exists
    credentials_path = 'credentials.json'
    if not os.path.exists(credentials_path):
        print("❌ Error: credentials.json not found!")
        print("\nTo get credentials.json:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a new project or select existing one")
        print("3. Enable Google Calendar API")
        print("4. Go to 'Credentials' → 'Create Credentials' → 'OAuth client ID'")
        print("5. Choose 'Desktop app' as application type")
        print("6. Download the JSON file and save it as 'credentials.json'")
        return
    
    try:
        print("🔐 Starting OAuth flow...")
        print("A browser window will open for authentication.")
        
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, 
            SCOPES
        )
        
        # This will open a browser window on port 8080
        creds = flow.run_local_server(port=8080)
        
        # Save the token
        token_path = 'token.json'
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())
        
        print(f"\n✅ Success! Token saved to {token_path}")
        print("\n📋 Next steps:")
        print(f"1. Copy {token_path} to your server")
        print(f"2. Set environment variable: GOOGLE_TOKEN_PATH=/path/to/{token_path}")
        print("3. Your agent will now be able to access Google Calendar!")
        
    except Exception as e:
        print(f"\n❌ Error generating token: {e}")
        print("\nTroubleshooting:")
        print("- Make sure credentials.json is valid")
        print("- Check that you have a web browser available")
        print("- Ensure you're running this on your local machine, not a server")

if __name__ == '__main__':
    generate_token()