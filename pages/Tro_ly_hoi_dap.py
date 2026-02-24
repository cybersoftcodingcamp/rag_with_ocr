import streamlit as st
from config import DEFAULT_COLLECTION
from rag import retrieve_documents, generate_response

st.title("⚖️ Trợ Lý Pháp Lý RAG")
st.markdown("Hỏi bất kỳ câu hỏi nào liên quan đến tài liệu pháp lý của bạn.")

query = st.text_input("Nhập câu hỏi của bạn:", placeholder="Ví dụ: Quy định về hợp đồng lao động là gì?")
collection_name = st.text_input("Tên Index (Collection):", value=DEFAULT_COLLECTION)

if st.button("Gửi Câu Hỏi", icon="🚀"):
    if query:
        with st.spinner("Đang tìm kiếm và xử lý..."):
            contexts = retrieve_documents(query, collection_name)
            if not contexts:
                st.warning("Không tìm thấy tài liệu liên quan.")
            else:
                response = generate_response(query, contexts)
                st.success("Trả Lời:")
                st.markdown(response)
                
                st.subheader("Sources:")
                for ctx in contexts:
                    st.markdown(f"- {ctx['source']}")
    else:
        st.error("Vui lòng nhập câu hỏi.")