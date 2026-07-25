import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.model_name = self.model_name = "openai/gpt-oss-120b"

        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY is missing in the .env file")

        

settings = Settings()