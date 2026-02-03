
# import streamlit as st
# import requests
# import base64
# import json
# import pandas as pd

# # FastAPI 服务器地址
# API_URL = "http://127.0.0.1:8000/questions/bulk_add"
# DELETE_QUESTION_API_URL = "http://127.0.0.1:8000/questions"
# DELETE_POST_API_URL = "http://127.0.0.1:8000/posts"
# user_id = st.session_state.get("user_id", None)  # 从session_state获取User ID

# if user_id != 1:
#     st.warning("您没有权限访问此页面。")
#     st.stop()  # 停止页面继续加载
# # 将图片文件转换为 Base64 编码
# def get_image_as_base64(image_file):
#     with open(image_file, "rb") as f:
#         return base64.b64encode(f.read()).decode()

# # 读取本地背景图片并转换为 Base64
# background_image_file = r"D:\\myproject\\ML\\2024SE-Teamwork-main\src\\1.png"  # 替换为你的本地背景图文件路径
# image_base64 = get_image_as_base64(background_image_file)

# # 添加背景图和蒙版的 CSS
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url('data:image/jpeg;base64,{image_base64}');
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         height: 100vh;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         color: white;
#     }}
    
#     /* 蒙版效果 */
#     .stApp::before {{
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background: rgba(0, 0, 0, 0.5);  /* 半透明黑色蒙版 */
#         z-index: -1;  /* 将蒙版置于背景图和内容之间 */
#     }}

#     /* 内容区域 */
#     .content {{
#         position: relative;
#         z-index: 1;
#         text-align: center;
#     }}
#     </style>
#     """, unsafe_allow_html=True
# )

# # 添加自定义CSS样式
# def add_custom_styles():
#     st.markdown("""
#     <style>
#         /* 整体背景 */
#         body {
#             background: linear-gradient(135deg, #74EBD5 0%, #ACD8E5 100%);
#             font-family: 'Arial', sans-serif;
#             margin: 0;
#             padding: 0;
#         }
#         .stApp {
#             background-color: transparent;
#         }

#         /* 标题样式 */
#         h1 {
#             font-size: 100px;
#             text-align: center;
#             color: #fff;
#             font-weight: 600;
#             margin-top: 30px;
#             text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
#         }

#         /* 输入框和选择框 */
#         .stTextInput input, .stTextArea textarea, .stSelectbox select, .stNumberInput input {
#             border-radius: 8px;
#             border: 1px solid #DDD;
#             padding: 12px 18px;
#             font-size: 16px;
#             margin-bottom: 20px;
#             width: 100%;
#             transition: all 0.3s ease-in-out;
#         }
#         .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus, .stNumberInput input:focus {
#             border-color: #4A90E2;
#             box-shadow: 0px 0px 10px rgba(74, 144, 226, 0.6);
#         }

#         /* 按钮样式 */
#         .stButton button {
#             background-color: #4A90E2;
#             color: white;
#             border: none;
#             padding: 14px 28px;
#             border-radius: 8px;
#             font-size: 18px;
#             cursor: pointer;
#             transition: background-color 0.3s ease, transform 0.2s ease;
#             box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
#         }
#         .stButton button:hover {
#             background-color: #357ABD;
#             transform: translateY(-3px);
#             box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
#         }

#         /* 信息反馈框 */
#         .stSuccess, .stError, .stWarning {
#             font-size: 18px;
#             padding: 15px;
#             border-radius: 8px;
#             margin-bottom: 20px;
#             box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
#         }
#         .stSuccess {
#             background-color: #d3f9d8;
#             border-left: 5px solid #4CAF50;
#         }
#         .stError {
#             background-color: #f8d7da;
#             border-left: 5px solid #dc3545;
#         }
#         .stWarning {
#             background-color: #fff3cd;
#             border-left: 5px solid #ffc107;
#         }

#         /* 旋转动画 */
#         @keyframes rotate {
#             0% {
#                 transform: rotate(0deg);
#             }
#             100% {
#                 transform: rotate(360deg);
#             }
#         }
#         .rotate {
#             display: inline-block;
#             animation: rotate 3s infinite linear;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # FastAPI 请求的API
# st.title("Management")

# # 添加样式
# add_custom_styles()

# # 添加分页选项
# page = st.radio("选择操作", ["添加题目", "删除题目","删除帖子"])

# # 添加题目功能
# if page == "添加题目":


# # 提示用户上传Excel文件
#  uploaded_file = st.file_uploader("上传题库Excel文件", type=["xlsx"])

# # 如果文件上传了，处理上传的文件
#  if uploaded_file is not None:
#     # 读取 Excel 文件
#     try:
#         df = pd.read_excel(uploaded_file)
#         st.write("Excel 文件内容：")
#         st.dataframe(df.head())  # 显示前几行数据，帮助用户检查文件内容

#         # 检查是否包含必要的列
#         required_columns = ["content", "answer", "difficulty", "type", "user_id",""]
#         if not all(col in df.columns for col in required_columns):
#             st.error(f"Excel 文件缺少必要的列：{', '.join(required_columns)}")
#         else:
#             # 允许用户确认提交数据
#             if st.button("确认提交"):
#                 # 将数据转换为字典形式，准备发送到后端
#                 questions = df[required_columns].to_dict(orient="records")

#                 # 发送 POST 请求到 FastAPI 后端
#                 response = requests.post(API_URL, json=questions)

#                 # 处理后端响应
#                 if response.status_code == 200:
#                     st.success("题库已成功批量导入！")
#                 else:
#                     st.error(f"导入失败：{response.json().get('detail', '未知错误')}")
#     except Exception as e:
#         st.error(f"文件读取失败：{e}") 

# # 删除题目功能
# elif page == "删除题目":
#     st.markdown('<div class="content">', unsafe_allow_html=True)
#     with st.form("delete_question_form", clear_on_submit=True):
#         st.header("删除题目")
#         question_id = st.number_input("题目ID", min_value=1, step=1)
#         delete_submitted = st.form_submit_button("删除题目")
        
#     # 如果删除表单提交
#     if delete_submitted:
#         # 发送删除请求到FastAPI
#         try:
#             delete_url = f"{DELETE_QUESTION_API_URL}/{question_id}"
#             response = requests.delete(delete_url)
#             if response.status_code == 200:
#                 st.success("题目删除成功！")
#             else:
#                 st.error(f"删除题目失败：{response.json().get('detail')}")
#         except requests.exceptions.RequestException as e:
#             st.error(f"请求失败: {e}")
#     st.markdown('</div>', unsafe_allow_html=True)

# elif page == "删除帖子":
#   post_id = st.number_input("输入要删除的帖子ID", min_value=1, step=1)
#   if st.button("删除帖子"):
#     # 构建请求URL
#     delete_url = f"{DELETE_POST_API_URL}/{post_id}"

#     # 发送删除请求
#     try:
#         response = requests.delete(delete_url)
#         if response.status_code == 200:
#             st.success("帖子删除成功！")
#         else:
#             st.error(f"删除帖子失败：{response.json().get('detail')}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"请求失败: {e}")


# import streamlit as st
# import requests
# import base64
# import json
# import pandas as pd

# # FastAPI 服务器地址
# API_URL = "http://127.0.0.1:8000/questions/bulk_add"
# DELETE_QUESTION_API_URL = "http://127.0.0.1:8000/questions"
# DELETE_POST_API_URL = "http://127.0.0.1:8000/posts"
# user_id = st.session_state.get("user_id", None)  # 从session_state获取User ID

# if user_id != 1:
#     st.warning("您没有权限访问此页面。")
#     st.stop()  # 停止页面继续加载
# # 将图片文件转换为 Base64 编码
# def get_image_as_base64(image_file):
#     with open(image_file, "rb") as f:
#         return base64.b64encode(f.read()).decode()

# # 读取本地背景图片并转换为 Base64
# background_image_file = "D:/myproject/ML/2024SE-Teamwork-main/src/6.png"  # 替换为你的本地背景图文件路径
# image_base64 = get_image_as_base64(background_image_file)

# # 添加背景图和蒙版的 CSS
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url('data:image/jpeg;base64,{image_base64}');
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         height: 100vh;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         color: white;
#     }}
    
#     /* 蒙版效果 */
#     .stApp::before {{
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background: rgba(0, 0, 0, 0.5);  /* 半透明黑色蒙版 */
#         z-index: -1;  /* 将蒙版置于背景图和内容之间 */
#     }}

#     /* 内容区域 */
#     .content {{
#         position: relative;
#         z-index: 1;
#         text-align: center;
#     }}
#     </style>
#     """, unsafe_allow_html=True
# )

# # 添加自定义CSS样式
# def add_custom_styles():
#     st.markdown("""
#     <style>
#         /* 整体背景 */
#         body {
#             background: linear-gradient(135deg, #74EBD5 0%, #ACD8E5 100%);
#             font-family: 'Arial', sans-serif;
#             margin: 0;
#             padding: 0;
#         }
#         .stApp {
#             background-color: transparent;
#         }

#         /* 标题样式 */
#         h1 {
#             font-size: 100px;
#             text-align: center;
#             color: #fff;
#             font-weight: 600;
#             margin-top: 30px;
#             text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
#         }

#         /* 输入框和选择框 */
#         .stTextInput input, .stTextArea textarea, .stSelectbox select, .stNumberInput input {
#             border-radius: 8px;
#             border: 1px solid #DDD;
#             padding: 12px 18px;
#             font-size: 16px;
#             margin-bottom: 20px;
#             width: 100%;
#             transition: all 0.3s ease-in-out;
#         }
#         .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus, .stNumberInput input:focus {
#             border-color: #4A90E2;
#             box-shadow: 0px 0px 10px rgba(74, 144, 226, 0.6);
#         }

#         /* 按钮样式 */
#         .stButton button {
#             background-color: #4A90E2;
#             color: white;
#             border: none;
#             padding: 14px 28px;
#             border-radius: 8px;
#             font-size: 18px;
#             cursor: pointer;
#             transition: background-color 0.3s ease, transform 0.2s ease;
#             box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
#         }
#         .stButton button:hover {
#             background-color: #357ABD;
#             transform: translateY(-3px);
#             box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
#         }

#         /* 信息反馈框 */
#         .stSuccess, .stError, .stWarning {
#             font-size: 18px;
#             padding: 15px;
#             border-radius: 8px;
#             margin-bottom: 20px;
#             box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
#         }
#         .stSuccess {
#             background-color: #d3f9d8;
#             border-left: 5px solid #4CAF50;
#         }
#         .stError {
#             background-color: #f8d7da;
#             border-left: 5px solid #dc3545;
#         }
#         .stWarning {
#             background-color: #fff3cd;
#             border-left: 5px solid #ffc107;
#         }

#         /* 旋转动画 */
#         @keyframes rotate {
#             0% {
#                 transform: rotate(0deg);
#             }
#             100% {
#                 transform: rotate(360deg);
#             }
#         }
#         .rotate {
#             display: inline-block;
#             animation: rotate 3s infinite linear;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # FastAPI 请求的API
# st.title("Management")

# # 添加样式
# add_custom_styles()

# # 添加分页选项
# page = st.radio("选择操作", ["添加题目", "删除题目","删除帖子"])

# # 添加题目功能
# if page == "添加题目":


# # 提示用户上传Excel文件
#  uploaded_file = st.file_uploader("上传题库Excel文件", type=["xlsx"])

# # 如果文件上传了，处理上传的文件
#  if uploaded_file is not None:
#     # 读取 Excel 文件
#     try:
#         df = pd.read_excel(uploaded_file)
#         st.write("Excel 文件内容：")
#         st.dataframe(df.head())  # 显示前几行数据，帮助用户检查文件内容

#         # 检查是否包含必要的列
#         required_columns = ["content", "answer", "difficulty", "type", "user_id", "subject"]
#         if not all(col in df.columns for col in required_columns):
#             st.error(f"Excel 文件缺少必要的列：{', '.join(required_columns)}")
#         else:
#             # 允许用户确认提交数据
#             if st.button("确认提交"):
#                 # 将数据转换为字典形式，准备发送到后端
#                 questions = df[required_columns].to_dict(orient="records")
#                 # 发送 POST 请求到 FastAPI 后端
#                 response = requests.post(API_URL, json=questions)
#                 # 处理后端响应
#                 if response.status_code == 200:
#                     st.success("题库已成功批量导入！")
#                 else:
#                     st.error(f"导入失败：{response.json().get('detail', '未知错误')}")
#     except Exception as e:
#         st.error(f"文件读取失败：{e}")


# # 删除题目功能
# elif page == "删除题目":
#     st.markdown('<div class="content">', unsafe_allow_html=True)
#     with st.form("delete_question_form", clear_on_submit=True):
#         st.header("删除题目")
#         question_id = st.number_input("题目ID", min_value=1, step=1)
#         delete_submitted = st.form_submit_button("删除题目")
        
#     # 如果删除表单提交
#     if delete_submitted:
#         # 发送删除请求到FastAPI
#         try:
#             delete_url = f"{DELETE_QUESTION_API_URL}/{question_id}"
#             response = requests.delete(delete_url)
#             if response.status_code == 200:
#                 st.success("题目删除成功！")
#             else:
#                 st.error(f"删除题目失败：{response.json().get('detail')}")
#         except requests.exceptions.RequestException as e:
#             st.error(f"请求失败: {e}")
#     st.markdown('</div>', unsafe_allow_html=True)

# elif page == "删除帖子":
#   post_id = st.number_input("输入要删除的帖子ID", min_value=1, step=1)
#   if st.button("删除帖子"):
#     # 构建请求URL
#     delete_url = f"{DELETE_POST_API_URL}/{post_id}"

#     # 发送删除请求
#     try:
#         response = requests.delete(delete_url)
#         if response.status_code == 200:
#             st.success("帖子删除成功！")
#         else:
#             st.error(f"删除帖子失败：{response.json().get('detail')}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"请求失败: {e}")










import streamlit as st
import requests
import base64
import json
import pandas as pd

# FastAPI 服务器地址
API_URL = "http://127.0.0.1:8000/questions/bulk_add"
DELETE_QUESTION_API_URL = "http://127.0.0.1:8000/questions"
DELETE_POST_API_URL = "http://127.0.0.1:8000/posts"

DELETE_QUESTION_API_URL = "http://127.0.0.1:8000/questions"
DELETE_POST_API_URL = "http://127.0.0.1:8000/posts"
GET_QUESTIONS_API_URL = "http://127.0.0.1:8000/questions"
GET_POSTS_API_URL = "http://127.0.0.1:8000/posts"
GET_REPLIES_API = "http://127.0.0.1:8000/posts/{post_id}/replies"

user_id = st.session_state.get("user_id", None)  # 从session_state获取User ID

if user_id != 1:
    st.warning("您没有权限访问此页面。")
    st.stop()  # 停止页面继续加载
# 将图片文件转换为 Base64 编码
def get_image_as_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 读取本地背景图片并转换为 Base64
background_image_file = "D:/myproject/ML/2024SE-Teamwork-main/src/6.png"  # 替换为你的本地背景图文件路径
image_base64 = get_image_as_base64(background_image_file)

# 添加背景图和蒙版的 CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{image_base64}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
    }}
    
    /* 蒙版效果 */
    .stApp::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);  /* 半透明黑色蒙版 */
        z-index: -1;  /* 将蒙版置于背景图和内容之间 */
    }}

    /* 内容区域 */
    .content {{
        position: relative;
        z-index: 1;
        text-align: center;
    }}
    </style>
    """, unsafe_allow_html=True
)

# 添加自定义CSS样式
def add_custom_styles():
    st.markdown("""
    <style>
        /* 整体背景 */
        body {
            background: linear-gradient(135deg, #74EBD5 0%, #ACD8E5 100%);
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }
        .stApp {
            background-color: transparent;
        }

        /* 标题样式 */
        h1 {
            font-size: 100px;
            text-align: center;
            color: #fff;
            font-weight: 600;
            margin-top: 30px;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }

        /* 输入框和选择框 */
        .stTextInput input, .stTextArea textarea, .stSelectbox select, .stNumberInput input {
            border-radius: 8px;
            border: 1px solid #DDD;
            padding: 12px 18px;
            font-size: 16px;
            margin-bottom: 20px;
            width: 100%;
            transition: all 0.3s ease-in-out;
        }
        .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus, .stNumberInput input:focus {
            border-color: #4A90E2;
            box-shadow: 0px 0px 10px rgba(74, 144, 226, 0.6);
        }

        /* 按钮样式 */
        .stButton button {
            background-color: #4A90E2;
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton button:hover {
            background-color: #357ABD;
            transform: translateY(-3px);
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
        }

        /* 信息反馈框 */
        .stSuccess, .stError, .stWarning {
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stSuccess {
            background-color: #d3f9d8;
            border-left: 5px solid #4CAF50;
        }
        .stError {
            background-color: #f8d7da;
            border-left: 5px solid #dc3545;
        }
        .stWarning {
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
        }

        /* 旋转动画 */
        @keyframes rotate {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }
        .rotate {
            display: inline-block;
            animation: rotate 3s infinite linear;
        }
    </style>
    """, unsafe_allow_html=True)

# FastAPI 请求的API
st.title("Management")

# 添加样式
add_custom_styles()

# 添加分页选项
page = st.radio("选择操作", ["添加题目", "删除题目","删除帖子"])

# 添加题目功能
if page == "添加题目":


# 提示用户上传Excel文件
 uploaded_file = st.file_uploader("上传题库Excel文件", type=["xlsx"])

# 如果文件上传了，处理上传的文件
 if uploaded_file is not None:
    # 读取 Excel 文件
    try:
        df = pd.read_excel(uploaded_file)
        st.write("Excel 文件内容：")
        st.dataframe(df.head())  # 显示前几行数据，帮助用户检查文件内容

        # 检查是否包含必要的列
        required_columns = ["content", "answer", "difficulty", "type", "user_id", "subject"]
        if not all(col in df.columns for col in required_columns):
            st.error(f"Excel 文件缺少必要的列：{', '.join(required_columns)}")
        else:
            # 允许用户确认提交数据
            if st.button("确认提交"):
                # 将数据转换为字典形式，准备发送到后端
                questions = df[required_columns].to_dict(orient="records")
                # 发送 POST 请求到 FastAPI 后端
                response = requests.post(API_URL, json=questions)
                # 处理后端响应
                if response.status_code == 200:
                    st.success("题库已成功批量导入！")
                else:
                    st.error(f"导入失败：{response.json().get('detail', '未知错误')}")
    except Exception as e:
        st.error(f"文件读取失败：{e}")


elif page == "删除题目":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.header("删除题目")
    
    # 获取题目列表
    try:
        response = requests.get(GET_QUESTIONS_API_URL)
        if response.status_code == 200:
            questions = response.json()
            question_options = [f"ID: {q['id']} - {q['content']}" for q in questions]
            question_to_delete = st.selectbox("选择要删除的题目", question_options)
            
            if question_to_delete:
                # 获取选择的题目的ID
                question_id = int(question_to_delete.split(" - ")[0].split(": ")[1])
                selected_question = next(q for q in questions if q['id'] == question_id)
                
                # 显示题目的详细信息
                st.write("### 题目内容")
                st.write(f"**题目 ID**: {selected_question['id']}")
                st.write(f"**题目内容**: {selected_question['content']}")
                st.write(f"**正确答案**: {selected_question['answer']}")
                st.write(f"**难度**: {selected_question['difficulty']}")
                st.write(f"**类型**: {selected_question['type']}")
                st.write(f"**学科**: {selected_question['subject']}")
                
                delete_submitted = st.button("删除题目")
                
                if delete_submitted:
                    delete_url = f"{DELETE_QUESTION_API_URL}/{question_id}"
                    try:
                        delete_response = requests.delete(delete_url)
                        if delete_response.status_code == 200:
                            st.success("题目删除成功！")
                        else:
                            st.error(f"删除题目失败：{delete_response.json().get('detail')}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"请求失败: {e}")
        else:
            st.error("无法获取题目列表。")
    except requests.exceptions.RequestException as e:
        st.error(f"请求失败: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# 删除帖子功能
elif page == "删除帖子":
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.header("删除帖子")
    
    # 获取帖子列表
    try:
        response = requests.get(GET_POSTS_API_URL)
        if response.status_code == 200:
            posts = response.json()
            post_options = [f"ID: {p['id']} - {p['title']}" for p in posts]
            post_to_delete = st.selectbox("选择要删除的帖子", post_options)
            
            if post_to_delete:
                # 获取选择的帖子的ID
                post_id = int(post_to_delete.split(" - ")[0].split(": ")[1])
                selected_post = next(p for p in posts if p['id'] == post_id)
                
                # 显示帖子的详细信息
                st.write("### 帖子内容")
                st.write(f"**帖子 ID**: {selected_post['id']}")
                st.write(f"**帖子标题**: {selected_post['title']}")
                st.write(f"**帖子内容**: {selected_post['content']}")
                st.write(f"**学科**: {selected_post['subject']}")
                st.write(f"**用户 ID**: {selected_post['user_id']}")
                
                # 获取该帖子的所有回复
                try:
                    reply_response = requests.get(GET_REPLIES_API.format(post_id=post_id))
                    if reply_response.status_code == 200:
                        replies = reply_response.json()
                        if replies:
                            st.write("### 回复内容")
                            for reply in replies:
                                st.write(f"- **回复 ID**: {reply['id']}")
                                st.write(f"  **回复内容**: {reply['content']}")
                                st.write(f"  **用户 ID**: {reply['user_id']}")
                        else:
                            st.write("没有回复。")
                    else:
                        st.error(f"无法获取该帖子的回复：{reply_response.json().get('detail')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"请求失败: {e}")
                
                delete_submitted = st.button("删除帖子")
                
                if delete_submitted:
                    delete_url = f"{DELETE_POST_API_URL}/{post_id}"
                    try:
                        delete_response = requests.delete(delete_url)
                        if delete_response.status_code == 200:
                            st.success("帖子删除成功！")
                        else:
                            st.error(f"删除帖子失败：{delete_response.json().get('detail')}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"请求失败: {e}")
        else:
            st.error("无法获取帖子列表。")
    except requests.exceptions.RequestException as e:
        st.error(f"请求失败: {e}")

    st.markdown('</div>', unsafe_allow_html=True)