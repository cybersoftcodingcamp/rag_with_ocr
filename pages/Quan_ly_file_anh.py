import os
import streamlit as st
from PIL import Image
from config import FOLDER_PATH, DEFAULT_COLLECTION
from ingestion import ingest_data, get_qdrant_client  # Thêm import get_qdrant_client
from qdrant_client.http.models import Distance, VectorParams, PointStruct

st.title("⚙️ Quản Lý File Ảnh")
st.markdown("Hiển thị và quản lý các file ảnh trong thư mục law_data. Upload thêm ảnh và trích xuất vào Qdrant.")

# Upload file (lưu ngay vào folder khi upload)
uploaded_files = st.file_uploader("Upload Ảnh Mới (PNG, JPG, etc.)", type=['png', 'jpg', 'jpeg', 'tiff', 'bmp'], accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(FOLDER_PATH, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success(f"Đã upload và lưu {len(uploaded_files)} file vào folder!")

# Load danh sách ảnh sau upload (vì Streamlit rerun script)
image_files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]

# Hiển thị ảnh ngay (sẽ update tự động sau upload)
st.subheader("Danh Sách Ảnh Hiện Có")
if image_files:
    cols = st.columns(3)
    for idx, filename in enumerate(image_files):
        image_path = os.path.join(FOLDER_PATH, filename)
        img = Image.open(image_path)
        img.thumbnail((200, 200))
        with cols[idx % 3]:
            st.image(img, caption=filename, use_column_width=True)
else:
    st.info("Chưa có ảnh nào trong thư mục.")

# Input collection
collection_name = st.text_input("Nhập Tên Index (Collection) Để Lưu:", value=DEFAULT_COLLECTION)

# Khởi tạo qdrant client
qdrant_client = get_qdrant_client()

# Kiểm tra collection tồn tại (sử dụng collection_exists thay vì has_collection)
collection_exists = qdrant_client.collection_exists(collection_name)

# Button ingest
if st.button("Trích Xuất và Lưu", icon="💾"):
    if not image_files:
        st.error("Chưa có ảnh để xử lý!")
    elif not collection_exists:
        st.warning(f"Collection '{collection_name}' chưa tồn tại. Vui lòng tạo trước khi lưu data.")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        ingest_data(collection_name, progress_callback=progress_bar.progress, status_callback=status_text.text)
        st.success("Đã trích xuất và lưu thành công!")

# Nếu collection chưa tồn tại, hiển thị button để tạo
if not collection_exists:
    if st.button("Tạo Collection Mới", icon="🆕"):
        with st.spinner("Đang tạo collection..."):
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
            )
        st.success(f"Đã tạo collection '{collection_name}' thành công! Bây giờ bạn có thể trích xuất và lưu data.")
        st.rerun()  # Rerun để update status