

# import streamlit as st
# import requests
# import pandas as pd
# import base64

# # FastAPI 服务器地址
# API_URL = "http://127.0.0.1:8000/questions"

# if not st.session_state.get("logged_in", False):
#     st.warning("您必须登录才能访问此页面。")
#     st.stop()  # 停止页面继续加载
# st.title("题库查询")

# def get_image_as_base64(image_file):
#     with open(image_file, "rb") as f:
#         return base64.b64encode(f.read()).decode()

# # 读取本地背景图片并转换为 Base64
# background_image_file = "D:/myproject/ML/2024SE-Teamwork-main/src/2.png"  # 替换为你的本地背景图文件
# image_base64 = get_image_as_base64(background_image_file)

# # 添加背景图的 CSS
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
#     </style>
#     """,
#     unsafe_allow_html=True
# )




# # 添加自定义CSS样式
# st.markdown(
#     """
#     <style>
#     .question-card {
#         border: 1px solid #e0e0e0;
#         border-radius: 12px;
#         padding: 20px;
#         margin-bottom: 20px;
#         box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
#         background: linear-gradient(135deg, #f0f4f8, #ffffff);
#         transition: transform 0.3s ease, box-shadow 0.3s ease;
#     }
#     .question-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
#     }
#     .question-title {
#         font-size: 20px;
#         font-weight: bold;
#         color: #333;
#         margin-bottom: 8px;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         color: #007ACC;
#     }
#     .question-content {
#         # font-size: 16px;
#         # color: #444;
#         # margin-bottom: 8px;
#         # line-height: 1.6;
#         font-size: 16px;
#     font-weight: bold;
#     color: #000;
#     background-color: #f0f8ff;
#     padding: 10px;
#     border-radius: 4px;
#     margin-bottom: 15px;
#     }
#     .question-label {
#         font-weight: bold;
#         color: #555;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# # 获取题库数据函数
# def fetch_questions():
#     try:
#         response = requests.get(API_URL)
#         response.raise_for_status()
#         questions = response.json()
#         return pd.DataFrame(questions)
#     except requests.exceptions.RequestException as e:
#         st.error(f"无法获取题库数据: {e}")
#         return pd.DataFrame()

# # 重新加载数据
# if st.button("刷新题库"):
#     st.cache_data.clear()  # 清除缓存
#     questions_df = fetch_questions()
# else:
#     questions_df = fetch_questions()

# # 加载题库数据并显示
# if not questions_df.empty:
#     # 获取所有题目类型并添加类型筛选器
#     question_types = questions_df["type"].unique()
#     selected_type = st.selectbox("选择题目类型", ["全部"] + list(question_types))

#     # 根据选择的题目类型筛选难度
#     if selected_type != "全部":
#         filtered_by_type = questions_df[questions_df["type"] == selected_type]
#         difficulties = filtered_by_type["difficulty"].unique()
#         selected_difficulty = st.selectbox("选择题目难度", ["全部"] + sorted(difficulties))

#         # 根据选择的难度筛选数据
#         if selected_difficulty != "全部":
#             filtered_questions = filtered_by_type[filtered_by_type["difficulty"] == selected_difficulty]
#         else:
#             filtered_questions = filtered_by_type
#     else:
#         filtered_questions = questions_df

#     # 逐个显示题目数据，强调题目ID和内容
#     st.write("题库数据：")
#     for index, row in filtered_questions.iterrows():
#         # 使用HTML和CSS来美化显示
#         st.markdown(
#             f"""
#             <div class="question-card">
#                 <div class="question-title">题目ID: {row['id']}</div>
#                 <div class="question-content"><span class="question-label">题目内容:</span> {row['content']}</div>
#                 <div class="question-content"><span class="question-label">答案:</span> {row['answer']}</div>
#                 <div class="question-content"><span class="question-label">难度:</span> {row['difficulty']}</div>
#                 <div class="question-content"><span class="question-label">类型:</span> {row['type']}</div>
#                 <div class="question-content"><span class="question-label">供题用户ID:</span> {row['user_id']}</div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
# else:
#     st.warning("题库中暂无数据或无法连接到服务器。")


import streamlit as st
import requests
import pandas as pd
import base64

# FastAPI 服务器地址
API_URL = "http://127.0.0.1:8000/questions"

if not st.session_state.get("logged_in", False):
    st.warning("您必须登录才能访问此页面。")
    st.stop()  # 停止页面继续加载
st.title("题库查询")

def get_image_as_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 读取本地背景图片并转换为 Base64
background_image_file = "D:/myproject/ML/2024SE-Teamwork-main/src/6.png"  # 替换为你的本地背景图文件
image_base64 = get_image_as_base64(background_image_file)

# 添加背景图的 CSS
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
    </style>
    """,
    unsafe_allow_html=True
)

# 添加自定义CSS样式
st.markdown(
    """
    <style>
    .question-card {
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        background: linear-gradient(135deg, #f0f4f8, #ffffff);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .question-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
    }
    .question-title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #007ACC;
    }
    .question-content {
        # font-size: 16px;
        # color: #444;
        # margin-bottom: 8px;
        # line-height: 1.6;
        font-size: 16px;
        font-weight: bold;
        color: #000;
        background-color: #f0f8ff;
        padding: 10px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .question-label {
        font-weight: bold;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True
)

# 获取题库数据函数
def fetch_questions():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        questions = response.json()
        return pd.DataFrame(questions)
    except requests.exceptions.RequestException as e:
        st.error(f"无法获取题库数据: {e}")
        return pd.DataFrame()

# 重新加载数据
if st.button("刷新题库"):
    st.cache_data.clear()  # 清除缓存
    questions_df = fetch_questions()
else:
    questions_df = fetch_questions()

# 加载题库数据并显示
if not questions_df.empty:
    # 获取所有题目类型和科目，并添加筛选器
    question_types = questions_df["type"].unique()
    subjects = questions_df["subject"].unique()

    selected_type = st.selectbox("选择题目类型", ["全部"] + list(question_types))
    selected_subject = st.selectbox("选择题目科目", ["全部"] + list(subjects))  # 新增科目筛选器

    # 根据选择的题目类型筛选
    if selected_type != "全部":
        filtered_by_type = questions_df[questions_df["type"] == selected_type]
    else:
        filtered_by_type = questions_df

    # 根据选择的题目科目筛选
    if selected_subject != "全部":
        filtered_questions = filtered_by_type[filtered_by_type["subject"] == selected_subject]
    else:
        filtered_questions = filtered_by_type

    # 如果需要按难度进一步筛选（可选）
    if selected_type != "全部" or selected_subject != "全部":
        st.write(f" **{selected_type}**   **{selected_subject}**  ")
    
    # 逐个显示题目数据，强调题目ID和内容
    st.write("题库数据：")
    for index, row in filtered_questions.iterrows():
        # 使用HTML和CSS来美化显示
        st.markdown(
            f"""
            <div class="question-card">
                <div class="question-title">题目ID: {row['id']}</div>
                <div class="question-content"><span class="question-label">科目:</span> {row['subject']}</div>  <!-- 显示科目 -->
                <div class="question-content"><span class="question-label">题目内容:</span> {row['content']}</div>
                <div class="question-content"><span class="question-label">答案:</span> {row['answer']}</div>
                <div class="question-content"><span class="question-label">难度:</span> {row['difficulty']}</div>
                <div class="question-content"><span class="question-label">类型:</span> {row['type']}</div>
                <div class="question-content"><span class="question-label">供题用户ID:</span> {row['user_id']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.warning("题库中暂无数据或无法连接到服务器。")
