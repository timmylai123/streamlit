import streamlit as st
import os

# 设置页面标题
st.set_page_config(page_title="文件下载服务")

# 定义文件目录
FILE_DIR = r"C:\Users\laiyu\Desktop\streamlit\files"

st.title("文件下载服务")

# 添加调试信息
st.write(f"文件目录: {FILE_DIR}")
st.write(f"目录是否存在: {os.path.exists(FILE_DIR)}")

def get_file_list():
    try:
        return [f for f in os.listdir(FILE_DIR) if os.path.isfile(os.path.join(FILE_DIR, f))]
    except Exception as e:
        st.error(f"获取文件列表时出错: {str(e)}")
        return []

# 获取文件列表
files = get_file_list()

if not files:
    st.warning("没有可供下载的文件。")
else:
    st.write("可下载的文件：")
    for file in files:
        file_path = os.path.join(FILE_DIR, file)
        file_size = os.path.getsize(file_path)
        
        # 显示文件大小
        size_str = f"{file_size / 1024:.2f} KB" if file_size < 1024 * 1024 else f"{file_size / 1024 / 1024:.2f} MB"
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{file} ({size_str})")
        with col2:
            with open(file_path, "rb") as f:
                st.download_button(
                    label="下载",
                    data=f,
                    file_name=file,
                    mime="application/octet-stream"
                )

st.write("页面加载完成")
