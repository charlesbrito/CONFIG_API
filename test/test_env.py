import os
from dotenv import load_dotenv

load_dotenv(override=True)

URL_DATABASE = os.getenv("key_database")
print(f"URL_DATABASE: {URL_DATABASE}")