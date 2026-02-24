import os
import streamlit as st
from PIL import Image
from config import FOLDER_PATH, DEFAULT_COLLECTION
from ingestion import ingest_data

st.title("⚙️ Quản Lý File Ảnh")
st.markdown("Hiển thị và quản lý các file ảnh trong thư mục law_data. Upload thêm ảnh và trích xuất vào Qdrant.")

# Upload file
uploaded_files = st.file_uploader("Upload Ảnh Mới (PNG, JPG, etc.)", type=['png', 'jpg', 'jpeg', 'tiff', 'bmp'], accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(FOLDER_PATH, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success(f"Đã upload {len(uploaded_files)} file!")

# Input collection
collection_name = st.text_input("Nhập Tên Index (Collection) Để Lưu:", value=DEFAULT_COLLECTION)

image_files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
# Button ingest
if st.button("Trích Xuất và Lưu", icon="💾"):
    if not image_files:
        st.error("Chưa có ảnh để xử lý!")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        ingest_data(collection_name, progress_callback=progress_bar.progress, status_callback=status_text.text)
        st.success("Đã trích xuất và lưu thành công!")
        
# Hiển thị ảnh
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

