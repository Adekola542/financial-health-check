import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    CLIENT_ID: str = os.getenv("CLIENT_ID")
    CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
    REDIRECT_URI: str = os.getenv("REDIRECT_URI")
    AUTH_USERNAME: str = os.getenv("AUTH_USERNAME")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()
