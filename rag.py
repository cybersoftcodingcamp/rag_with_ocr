from qdrant_client import models
from config import TOP_K
from utils import get_embedding
from ingestion import get_qdrant_client  # Reuse client

openai_client = None  # Lazy load ở generate

def retrieve_documents(query, collection_name, top_k=TOP_K):
    qdrant_client = get_qdrant_client()
    query_embedding = get_embedding(query)
    search_results = qdrant_client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=top_k
    ).points
    return [{'text': point.payload['text'], 'source': point.payload['filename']} for point in search_results]

def generate_response(query, contexts):
    global openai_client
    if openai_client is None:
        from utils import get_openai_client
        openai_client = get_openai_client()
    
    from config import LLM_MODEL
    
    context_str = "\n\n".join([f"Source: {ctx['source']}\nText: {ctx['text']}" for ctx in contexts])
    prompt = f"""
    Bạn là một trợ lý pháp lý. Dựa trên các tài liệu sau, trả lời câu hỏi của người dùng một cách chính xác và ngắn gọn. Luôn trích dẫn source (filename) khi đề cập đến thông tin từ document.
    
    Tài liệu:
    {context_str}
    
    Câu hỏi: {query}
    """
    
    response = openai_client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "Bạn là trợ lý hữu ích."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content