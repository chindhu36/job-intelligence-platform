import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("OPENAI_API_KEY loaded successfully")
    print("Key starts with:", api_key[:7] + "...")
else:
    print("OPENAI_API_KEY was not found")