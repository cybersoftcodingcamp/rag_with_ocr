import os
from dotenv import load_dotenv

load_dotenv()

FOLDER_PATH = 'law_data'  # Thư mục chứa ảnh
DEFAULT_COLLECTION = 'law_database'
EMBEDDING_MODEL = 'text-embedding-3-small'
TOP_K = 5  # Số documents retrieve

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")
AWS_REGION = os.getenv("AWS_REGION")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")