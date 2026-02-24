import os
import uuid
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from config import QDRANT_HOST, QDRANT_API_KEY, FOLDER_PATH
from utils import extract_text_from_image, get_embedding

def get_qdrant_client():
    return QdrantClient(url=QDRANT_HOST, api_key=QDRANT_API_KEY)

# Hàm ingest (có thể gọi từ Streamlit hoặc standalone)
def ingest_data(collection_name, progress_callback=None, status_callback=None):
    qdrant_client = get_qdrant_client()
    
    image_files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
    total_files = len(image_files)
    
    for idx, filename in enumerate(image_files):
        
        image_path = os.path.join(FOLDER_PATH, filename)
        text = extract_text_from_image(image_path)
        
        embedding = get_embedding(text)
        
        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={'text': text, 'filename': filename}
        )
        qdrant_client.upsert(
            collection_name=collection_name,
            points=[point]
        )