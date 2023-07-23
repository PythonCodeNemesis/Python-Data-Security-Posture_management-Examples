import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Retrieve an environment variable
api_key = os.getenv("API_KEY")
# Usage example
print("API Key:", api_key)
