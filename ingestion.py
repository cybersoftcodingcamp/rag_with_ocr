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
    
    # Kiểm tra và tạo collection nếu chưa tồn tại (cơ chế bạn yêu cầu)
    # Nếu collection đã có, chỉ upsert points (lưu data).
    # Nếu chưa có, tạo mới và upsert.
    try:
        qdrant_client.get_collection(collection_name)
        if status_callback:
            status_callback(f"Collection '{collection_name}' đã tồn tại, tiến hành lưu data...")
    except ValueError:
        if status_callback:
            status_callback(f"Collection '{collection_name}' chưa tồn tại, đang tạo mới...")
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )
    
    image_files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
    total_files = len(image_files)
    
    for idx, filename in enumerate(image_files):
        if status_callback:
            status_callback(f"Processing {filename} ({idx+1}/{total_files})...")
        
        image_path = os.path.join(FOLDER_PATH, filename)
        text = extract_text_from_image(image_path)
        if not text:
            if status_callback:
                status_callback(f"No text extracted from {filename}")
            continue
        
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
        
        if progress_callback:
            progress_callback((idx + 1) / total_files)
    
    if status_callback:
        status_callback("Ingestion completed!")

# Nếu chạy standalone: python ingestion.py
if __name__ == "__main__":
    ingest_data('law_database')