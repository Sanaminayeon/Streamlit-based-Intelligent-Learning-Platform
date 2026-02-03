# import streamlit as st
# from PIL import Image
# from paddleocr import PaddleOCR
# import numpy as np
# from io import BytesIO
# from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
# from sparkai.core.messages import ChatMessage
# import base64
# import re

# # 初始化 PaddleOCR
# ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 支持中文和英文








# # 星火认知大模型的API和认证信息
# SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
# SPARKAI_APP_ID = 'e8025f24'
# SPARKAI_API_SECRET = 'Yjc5OTRkOThkODY2NzZjMDQ2ZDE0ODgx'
# SPARKAI_API_KEY = 'd2e23d404b09b8c574b8efc074f16e43'
# SPARKAI_DOMAIN = '4.0Ultra'

# # 初始化 Spark 大模型
# def init_spark_model():
#     return ChatSparkLLM(
#         spark_api_url=SPARKAI_URL,
#         spark_app_id=SPARKAI_APP_ID,
#         spark_api_key=SPARKAI_API_KEY,
#         spark_api_secret=SPARKAI_API_SECRET,
#         spark_llm_domain=SPARKAI_DOMAIN,
#         streaming=False,
#     )

# # OCR功能，提取图像中的文本
# def extract_text_from_image(image_bytes):
#     try:
#         image = Image.open(BytesIO(image_bytes))  # 打开图像
#         img_np = np.array(image)  # 转换为NumPy数组

#         # 使用PaddleOCR进行文本提取
#         result = ocr.ocr(img_np, cls=True)
#         extracted_text = ''
#         for line in result:
#             for text in line:
#                 extracted_text += text[1][0] + '\n'
#         return extracted_text
#     except Exception as e:
#         st.error(f"图像处理失败: {e}")
#         return ""

# # 清空作业历史记录
# def clear_homework_history():
#     st.session_state.homeworks = []

# # 设置背景图的函数
# def set_background_image(image_file):
#     with open(image_file, "rb") as f:
#         data = f.read()
#     encoded_image = base64.b64encode(data).decode()
#     css = f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{encoded_image}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }}
#     </style>
#     """
#     st.markdown(css, unsafe_allow_html=True)

# # 检查并渲染LaTeX内容
# def render_latex_content(content):
#     content = re.sub(r"[^a-zA-Z0-9\s\+\-\*\/\^\(\)\.,]", "", content)
#     try:
#         st.latex(content)
#     except Exception as e:
#         st.error(f"无法渲染为LaTeX: {e}")

# # Streamlit 界面和处理逻辑
# def main():
#     st.set_page_config(page_title="搜题")

#     # 设置本地背景图
#     set_background_image("D:/myproject/ML/2024SE-Teamwork-main/src/5.png")  # 替换为你的背景图片路径

#     # 侧边栏设置
#     with st.sidebar:
#         st.title('搜题')
#         st.success('API key 已经配置!', icon='✅')
#         st.sidebar.button('清空搜索历史', on_click=clear_homework_history)

#     # 初始化作业历史记录
#     if "homeworks" not in st.session_state:
#         st.session_state.homeworks = []

#     # 上传图片进行OCR处理
#     uploaded_image = st.file_uploader("上传题目", type=["png", "jpg", "jpeg"])

#     if uploaded_image is not None:
#         # 读取上传的文件为字节流
#         image_bytes = uploaded_image.read()
#         try:
#             image = Image.open(BytesIO(image_bytes))
#             st.image(image, caption='上传的图片', use_column_width=True)

#             # 使用PaddleOCR提取图像中的文本
#             extracted_text = extract_text_from_image(image_bytes)
#             st.subheader("题目")
#             st.markdown(extracted_text)  # 以Markdown形式显示提取的文本

#             # 选择是否将提取的文本进行批改与评价
#             if st.button("分析"):
#                 st.session_state.homeworks.append({"role": "user", "content": extracted_text})
#                 with st.chat_message("user"):
#                     st.markdown(extracted_text)

#                 # 调用星火大模型进行批改与评价
#                 spark_model = init_spark_model()
#                 prompt = f"### 请对以下题目进行分析，并反馈正确的答案，请不要使用Latex格式：\n\n{extracted_text}"  # 以Markdown格式传递
#                 messages = [ChatMessage(role="user", content=prompt)]
#                 handler = ChunkPrintHandler()

#                 # 获取机器人的批改与评价
#                 response = spark_model.generate([messages], callbacks=[handler])
#                 correction_and_feedback = response.generations[0][0].text  # 提取实际批改内容

#                 # 将批改与评价结果保存到历史记录
#                 st.session_state.homeworks.append({"role": "assistant", "content": correction_and_feedback})

#                 # 显示批改与评价结果
#                 with st.chat_message("assistant"):
#                     st.markdown(correction_and_feedback)  # 以Markdown形式显示

#         except Exception as e:
#             st.error(f"无法处理上传的图片: {e}")

# if __name__ == '__main__':
#     # 检查登录状态
#     if not st.session_state.get("logged_in", False):
#         st.warning("您必须登录才能访问此页面。")
#         st.stop()  # 停止页面继续加载
#     main()

import streamlit as st
from PIL import Image
from paddleocr import PaddleOCR
import numpy as np
from io import BytesIO
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import base64
import re

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 支持中文和英文

# 星火认知大模型的API和认证信息
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
SPARKAI_APP_ID = 'e8025f24'
SPARKAI_API_SECRET = 'Yjc5OTRkOThkODY2NzZjMDQ2ZDE0ODgx'
SPARKAI_API_KEY = 'd2e23d404b09b8c574b8efc074f16e43'
SPARKAI_DOMAIN = '4.0Ultra'

# 初始化 Spark 大模型
def init_spark_model():
    return ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )

# OCR功能，提取图像中的文本
def extract_text_from_image(image_bytes):
    try:
        image = Image.open(BytesIO(image_bytes))  # 打开图像
        img_np = np.array(image)  # 转换为NumPy数组

        # 使用PaddleOCR进行文本提取
        result = ocr.ocr(img_np, cls=True)
        extracted_text = ''
        for line in result:
            for text in line:
                extracted_text += text[1][0] + '\n'
        return extracted_text
    except Exception as e:
        st.error(f"图像处理失败: {e}")
        return ""

# 清空作业历史记录
def clear_homework_history():
    st.session_state.homeworks = []

# 设置背景图的函数
def set_background_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded_image = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 检查并渲染LaTeX内容
def render_latex_content(content):
    content = re.sub(r"[^a-zA-Z0-9\s\+\-\*\/\^\(\)\.,]", "", content)
    try:
        st.latex(content)
    except Exception as e:
        st.error(f"无法渲染为LaTeX: {e}")

# Streamlit 界面和处理逻辑
def main():
    st.set_page_config(page_title="搜题")

    # 设置本地背景图
    set_background_image("D:/myproject/ML/2024SE-Teamwork-main/src/5.png")  # 替换为你的背景图片路径

    # 侧边栏设置
    with st.sidebar:
        st.title('搜题')
        st.success('API key 已经配置!', icon='✅')
        st.sidebar.button('清空搜索历史', on_click=clear_homework_history)

    # 初始化作业历史记录
    if "homeworks" not in st.session_state:
        st.session_state.homeworks = []

    # 上传图片进行OCR处理
    uploaded_image = st.file_uploader("上传题目", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # 读取上传的文件为字节流
        image_bytes = uploaded_image.read()
        try:
            image = Image.open(BytesIO(image_bytes))
            st.image(image, caption='上传的图片', use_column_width=True)

            # 使用PaddleOCR提取图像中的文本
            extracted_text = extract_text_from_image(image_bytes)
            st.subheader("题目")
            st.markdown(extracted_text)  # 以Markdown形式显示提取的文本

            # 选择是否将提取的文本进行批改与评价
            if st.button("分析"):
                # 保存上传的题目文本到历史记录中
                st.session_state.homeworks.append({"role": "user", "content": extracted_text})
                with st.chat_message("user"):
                    st.markdown(extracted_text)

                # 调用星火大模型进行批改与评价
                spark_model = init_spark_model()
                prompt = f"### 请对以下题目进行分析，并反馈正确的答案，请不要使用Latex格式：\n\n{extracted_text}"  # 以Markdown格式传递
                messages = [ChatMessage(role="user", content=prompt)]
                handler = ChunkPrintHandler()

                # 获取机器人的批改与评价
                response = spark_model.generate([messages], callbacks=[handler])
                correction_and_feedback = response.generations[0][0].text  # 提取实际批改内容

                # 将批改与评价结果保存到历史记录
                st.session_state.homeworks.append({"role": "assistant", "content": correction_and_feedback})

                # 显示批改与评价结果
                with st.chat_message("assistant"):
                    st.markdown(correction_and_feedback)  # 以Markdown形式显示

        except Exception as e:
            st.error(f"无法处理上传的图片: {e}")

    # 聊天框：与大模型直接对话
    st.subheader("对回答不满意或需要其他帮助？请在此输入")

    # 获取用户输入框，并添加发送按钮
    user_input = st.text_area("请输入您的问题或请求", height=150)
    send_button = st.button("发送")

    if send_button and user_input:
        # 将用户输入的消息添加到历史记录
        st.session_state.homeworks.append({"role": "user", "content": user_input})

        # 更新对话上下文：将上传的题目内容和大模型的回答作为上下文
        conversation_context = ""
        for message in st.session_state.homeworks:
            conversation_context += f"{message['role']}: {message['content']}\n"

        with st.chat_message("user"):
            st.markdown(user_input)

        # 调用大模型进行回答
        spark_model = init_spark_model()
        prompt = f"### 请回答以下问题，并根据之前的上下文继续回答：\n\n{conversation_context}\n{user_input}"
        messages = [ChatMessage(role="user", content=prompt)]
        handler = ChunkPrintHandler()

        # 获取机器人的回答
        response = spark_model.generate([messages], callbacks=[handler])
        answer = response.generations[0][0].text  # 提取实际回答内容

        # 将大模型的回答添加到历史记录
        st.session_state.homeworks.append({"role": "assistant", "content": answer})

        # 显示大模型的回答
        with st.chat_message("assistant"):
            st.markdown(answer)  # 以Markdown形式显示

if __name__ == '__main__':
    # 检查登录状态
    if not st.session_state.get("logged_in", False):
        st.warning("您必须登录才能访问此页面。")
        st.stop()  # 停止页面继续加载
    main()


