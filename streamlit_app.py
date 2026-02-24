import streamlit as st

st.set_page_config(
    page_title="Hệ Thống RAG Trợ Lý Pháp Lý",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh để làm đẹp hơn
st.markdown("""
    <style>
    # .stApp { 
    #     background-color: #f0f4f8; 
    # }
    .sidebar .sidebar-content { 
        background-color: #ffffff; 
        border-right: 1px solid #e0e0e0; 
    }
    .stButton>button { 
        background-color: #4CAF50; 
        color: white; 
        border: none; 
        padding: 10px 20px; 
        border-radius: 4px; 
    }
    .stButton>button:hover { 
        background-color: #45a049; 
    }
    .stTextInput>div>div>input { 
        border-radius: 4px; 
        border: 1px solid #ccc; 
    }
    .reportview-container .main .block-container { 
        padding: 2rem; 
        background-color: white; 
        border-radius: 8px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
    }
    h1, h2, h3 { 
        color: #333; 
    }
    .landing-header {
        text-align: center;
        padding: 2rem 0;
    }
    .feature-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .tech-icon {
        text-align: center;
        margin: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar chung
with st.sidebar:
    st.image("./images/scales-of-justice.png", width=100)
    st.title("Về Dự Án")
    st.markdown("""
    **Tên Dự Án:** Hệ Thống RAG Trợ Lý Pháp Lý  
    **Mô Tả:** Dự án này xây dựng một hệ thống Retrieval-Augmented Generation (RAG) sử dụng vector database Qdrant và mô hình GPT-4o-mini để hỏi đáp dựa trên tài liệu pháp lý được extract từ ảnh.  
    **Công Nghệ Sử Dụng:**  
    - AWS Textract cho extraction text.  
    - OpenAI cho embeddings và generation.  
    - Qdrant cho vector store.  
    - Streamlit cho giao diện người dùng.  
    """)
    
    st.markdown("---")
    
    st.subheader("Vấn Đề Giải Quyết")
    st.markdown("""
    Trong lĩnh vực pháp lý, tài liệu thường tồn tại dưới dạng ảnh scan hoặc ảnh chụp, khiến việc tìm kiếm và hỏi đáp thủ công mất thời gian và dễ sai sót.  
    Dự án này giải quyết bằng cách:  
    - Tự động extract text từ ảnh và vector hóa.  
    - Cho phép truy vấn tự nhiên bằng ngôn ngữ tiếng Việt.  
    - Cung cấp câu trả lời chính xác, dựa trên dữ liệu, giúp luật sư và chuyên viên pháp lý tiết kiệm thời gian.  
    """)
    
    st.markdown("---")
    st.caption("Phiên bản 1.0 - Phát triển bởi Việt An Cybersoft | 2026")

# Main Landing Page
st.markdown('<div class="landing-header">', unsafe_allow_html=True)
st.image("./images/scales-of-justice.png", width=150)  # Icon lớn ở header
st.title("Chào Mừng Đến Với Hệ Thống RAG Trợ Lý Pháp Lý ⚖️")
st.markdown("Hệ thống thông minh hỗ trợ xử lý và hỏi đáp tài liệu pháp lý từ ảnh, giúp bạn tiết kiệm thời gian và tăng hiệu quả công việc.")
st.markdown('</div>', unsafe_allow_html=True)

# Phần Giới Thiệu
st.header("Giới Thiệu Dự Án")
st.markdown("""
Dự án này là một giải pháp RAG (Retrieval-Augmented Generation) hiện đại, kết hợp AI để tự động hóa quy trình xử lý tài liệu pháp lý. 
Từ việc extract text từ ảnh scan đến việc trả lời câu hỏi phức tạp dựa trên dữ liệu, hệ thống mang đến trải nghiệm tiện lợi và chính xác.
""")

# Phần Tính Năng Chính (sử dụng columns cho layout đẹp)
st.header("Tính Năng Chính")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/48/upload.png", width=50)
    st.subheader("Quản Lý File Ảnh")
    st.markdown("Upload, hiển thị và quản lý ảnh tài liệu pháp lý dễ dàng.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/48/database.png", width=50)
    st.subheader("Trích Xuất & Lưu Trữ")
    st.markdown("Extract text từ ảnh và lưu vào vector database với progress bar.")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/48/chat.png", width=50)
    st.subheader("Hỏi Đáp Thông Minh")
    st.markdown("Truy vấn tự nhiên và nhận câu trả lời dựa trên tài liệu, kèm source.")
    st.markdown('</div>', unsafe_allow_html=True)

# Phần Hướng Dẫn Sử Dụng
st.header("Hướng Dẫn Sử Dụng")
with st.expander("Bước 1: Quản Lý File Ảnh"):
    st.markdown("""
    - Truy cập trang 'Quản Lý File Ảnh' từ sidebar.
    - Upload ảnh mới (hỗ trợ PNG, JPG, TIFF, etc.).
    - Xem danh sách ảnh hiện có dưới dạng grid thumbnail.
    - Nhập tên collection và nhấn 'Trích Xuất và Lưu' để xử lý.
    """)

with st.expander("Bước 2: Hỏi Đáp"):
    st.markdown("""
    - Truy cập trang 'Trợ Lý Hỏi Đáp'.
    - Nhập câu hỏi liên quan đến tài liệu pháp lý.
    - Chọn collection (nếu khác default).
    - Nhận câu trả lời với trích dẫn source.
    """)

# Phần Công Nghệ Stack (với icons)
st.header("Công Nghệ Sử Dụng")
tech_cols = st.columns(4)
tech_stacks = [
    ("AWS Textract", "https://img.icons8.com/color/48/amazon-web-services.png"),
    ("OpenAI", "./images/openai-white.png"),
    ("Qdrant", "https://img.icons8.com/color/48/database.png"),  # Placeholder icon cho Qdrant
    ("Streamlit", "https://img.icons8.com/color/48/streamlit.png")
]

for idx, (name, icon_url) in enumerate(tech_stacks):
    with tech_cols[idx]:
        st.markdown('<div class="tech-icon">', unsafe_allow_html=True)
        st.image(icon_url, width=50)
        st.markdown(f"**{name}**")
        st.markdown('</div>', unsafe_allow_html=True)

# Phần Liên Hệ hoặc Footer
st.markdown("---")
st.markdown("""
### Liên Hệ
Nếu bạn có phản hồi hoặc cần hỗ trợ, liên hệ tại: cybersoft.codingcamp@gmail.com  
Cảm ơn bạn đã sử dụng hệ thống! 🚀
""", unsafe_allow_html=True)

st.caption("© 2026 Cybersoft AI Engineer. All rights reserved.")