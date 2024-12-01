import os
from dotenv import load_dotenv
from writerai import Writer

load_dotenv()

client = Writer(
    api_key=os.getenv('WRITER_API_KEY')  # Replace with your API key
    print(MY_ENV_VAR)
)