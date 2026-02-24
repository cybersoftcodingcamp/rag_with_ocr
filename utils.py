import boto3
from openai import OpenAI
from config import OPENAI_API_KEY, AWS_REGION, EMBEDDING_MODEL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# Khởi tạo clients (chỉ import khi cần, để tránh load thừa)
def get_textract_client():
    return boto3.client('textract', 
                        region_name=AWS_REGION,
                        aws_access_key_id=AWS_ACCESS_KEY_ID, 
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY)

# Extract text từ ảnh
def extract_text_from_image(image_path):
    textract_client = get_textract_client()
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()
    
    response = textract_client.detect_document_text(Document={'Bytes': image_bytes})
    
    text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            text += item['Text'] + '\n'
    
    return text.strip()

# Get embedding
def get_embedding(text):
    openai_client = get_openai_client()
    response = openai_client.embeddings.create(input=text, model=EMBEDDING_MODEL)
    return response.data[0].embedding