

# import streamlit as st
# import requests
# import base64

# # FastAPI 后端完整接口 URL
# REGISTER_API = "http://127.0.0.1:8000/register"
# LOGIN_API = "http://127.0.0.1:8000/login"
# CREATE_POST_API = "http://127.0.0.1:8000/create_post"
# GET_POSTS_API = "http://127.0.0.1:8000/posts"
# ADD_REPLY_API = "http://127.0.0.1:8000/posts/{post_id}/replies"
# GET_REPLIES_API = "http://127.0.0.1:8000/posts/{post_id}/replies"


# def get_image_as_base64(image_file):
#     with open(image_file, "rb") as f:
#         return base64.b64encode(f.read()).decode()

# # 读取本地背景图片并转换为 Base64
# background_image_file = "D:/myproject/ML/2024SE-Teamwork-main/src/3.png"  # 替换为你的本地背景图文件
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

# # HTML & CSS 样式
# st.markdown(""" 
#     <style>
#         .main-container {
#             max-width: 800px;
#             margin: 2rem auto;
#             padding: 2rem;
#             border-radius: 12px;
#             background-color: #f4f8fb;
#             box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
#         }

#         .title {
#             color: #2e3a4a;
#             font-size: 2.2em;
#             font-weight: 700;
#             text-align: center;
#             padding: 0.5em 0;
#             margin-bottom: 1em;
#             border-bottom: 3px solid #a6c1e1;
#         }

#         .section-header {
#             font-size: 1.5em;
#             color: #3a5f7d;
#             margin-bottom: 0.5em;
#             border-bottom: 2px solid #3a5f7d;
#             padding-bottom: 0.3em;
#             font-weight: 600;
#         }

#         .post-container {
#             border: 1px solid #d9e2ec;
#             padding: 1.5em;
#             margin: 1.5em 0;
#             border-radius: 8px;
#             background-color: #ffffff;
#             box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
#         }
        
#         .post-title { font-size: 1.3em; font-weight: bold; color: #333; }
#         .post-id { font-size: 0.9em; color: #888; margin-top: -5px; }
        
#         .post-content { font-size: 1em; color: #555; margin-top: 5px; }
        
#         .reply-container {
#             margin-top: 10px;
#             padding: 10px;
#             background-color: #f7f7f9;
#             border-radius: 5px;
#             border-left: 3px solid #6c757d;
#         }

#         .reply-author { color: #6c757d; font-weight: bold; }
#         .reply-content { color: #333; font-size: 0.95em; margin-top: 5px; }
        
#         input[type="text"], input[type="password"], textarea {
#             width: 100%;
#             padding: 0.8em;
#             margin: 0.3em 0;
#             border: 1px solid #a6c1e1;
#             border-radius: 6px;
#             font-size: 1em;
#         }
#             .reply-box {
#             margin-top: 15px;
#             padding: 15px;
#             background-color: #e9f5fb;
#             border: 1px solid #b0d4e1;
#             border-radius: 8px;
#             box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
#         }

#         .reply-box-title {
#             font-size: 1.1em;
#             font-weight: bold;
#             color: #3a5f7d;
#         }

#         .reply-box-content {
#             font-size: 1em;
#             color: #555;
#             margin-top: 8px;
#         }

#         input[type="text"], input[type="password"], textarea {
#             width: 100%;
#             padding: 0.8em;
#             margin: 0.3em 0;
#             border: 1px solid #a6c1e1;
#             border-radius: 6px;
#             font-size: 1em;
#         }











            

#         .stButton button {
#             background-color: #3a5f7d;
#             color: #fff;
#             padding: 0.8em 1.2em;
#             border-radius: 8px;
#             font-weight: 600;
#         }
        
#         .stButton button:hover {
#             background-color: #2e4d64;
#         }

#         .footer {
#             font-size: 0.9em;
#             color: #6c757d;
#             text-align: center;
#             padding: 1em 0;
#             border-top: 1px solid #ddd;
#             margin-top: 2em;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # 检查登录状态的函数
# def check_login():
#     if "logged_in" not in st.session_state:
#         st.session_state["logged_in"] = False
#     if "user_id" not in st.session_state:
#         st.session_state["user_id"] = None
#     if "username" not in st.session_state:
#         st.session_state["username"] = None

# # 用户注册功能
# def register():
#     st.markdown('<div class="section-header">用户注册</div>', unsafe_allow_html=True)
#     username = st.text_input("用户名", key="reg_username")
#     password = st.text_input("密码", type="password", key="reg_password")

#     if st.button("注册"):
#         if username and password:
#             response = requests.post(REGISTER_API, json={"username": username, "password": password})
#             if response.status_code == 200:
#                 st.markdown('<div class="success-message">注册成功！请登录。</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="error-message">注册失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown('<div class="warning-message">请输入用户名和密码。</div>', unsafe_allow_html=True)

# # 用户登录功能
# def login():
#     st.markdown('<div class="section-header">用户登录</div>', unsafe_allow_html=True)
#     username = st.text_input("用户名", key="login_username")
#     password = st.text_input("密码", type="password", key="login_password")

#     if st.button("登录"):
#         if username and password:
#             response = requests.post(LOGIN_API, json={"username": username, "password": password})
#             if response.status_code == 200:
#                 user_data = response.json()
#                 st.session_state["logged_in"] = True
#                 st.session_state["user_id"] = user_data.get("user_id")
#                 st.session_state["username"] = username
#                 st.markdown('<div class="success-message">登录成功！</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="error-message">登录失败：{response.json().get("detail", "用户名或密码错误")}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown('<div class="warning-message">请输入用户名和密码。</div>', unsafe_allow_html=True)

# # 发帖功能
# def create_post():
#     st.markdown('<div class="section-header">发布新帖子</div>', unsafe_allow_html=True)
#     title = st.text_input("标题", key="post_title")
#     content = st.text_area("内容", key="post_content")
#     subject = st.selectbox("选择学科标签", ["语文", "数学", "英语", "物理", "化学", "生物"])

#     if st.button("发布"):
#         user_id = st.session_state.get("user_id")
#         if title and content and subject and user_id:
#             post_data = {
#                 "title": title,
#                 "content": content,
#                 "subject": subject,
#                 "user_id": user_id
#             }
#             response = requests.post(CREATE_POST_API, json=post_data)
#             if response.status_code == 200:
#                 st.markdown('<div class="success-message">帖子发布成功！</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="error-message">发布失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
#         elif not user_id:
#             st.markdown('<div class="error-message">请先登录。</div>', unsafe_allow_html=True)
#         else:
#             st.markdown('<div class="warning-message">标题、内容和学科标签不能为空！</div>', unsafe_allow_html=True)



# def view_replies(post_id):
#     response = requests.get(GET_REPLIES_API.format(post_id=post_id))
#     if response.status_code == 200:
#         replies = response.json()
#         if replies:
#             for index, reply in enumerate(replies, start=1):  # 使用 enumerate 进行排序并加上楼层数
#                 st.markdown(f"""
#                     <div class="reply-box">
#                         <div class="reply-box-title">楼层 {index} - 回复者ID {reply['user_id']}:</div>
#                         <div class="reply-box-content">{reply['content']}</div>
#                     </div>
#                 """, unsafe_allow_html=True)

# def add_reply(post_id):
#     st.markdown('<div class="section-header">添加回复</div>', unsafe_allow_html=True)
#     reply_content = st.text_input("回复内容", key=f"reply_content_{post_id}")
#     user_id = st.session_state.get("user_id")

#     if st.button("回复", key=f"reply_button_{post_id}"):
#         if reply_content and user_id:
#             reply_data = {"content": reply_content, "post_id": post_id, "user_id": user_id}
#             response = requests.post(ADD_REPLY_API.format(post_id=post_id), json=reply_data)
#             if response.status_code == 200:
#                 st.markdown('<div class="success-message">回复成功！</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="error-message">回复失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown('<div class="warning-message">回复内容不能为空！</div>', unsafe_allow_html=True)


# def view_posts():
#     st.markdown('<div class="section-header">所有帖子</div>', unsafe_allow_html=True)
#     selected_subject = st.selectbox("按学科标签筛选帖子", ["全部", "语文", "数学", "英语", "物理", "化学", "生物"])

#     response = requests.get(GET_POSTS_API)
#     if response.status_code == 200:
#         posts = response.json()
#         filtered_posts = [post for post in posts if post["subject"] == selected_subject] if selected_subject != "全部" else posts
#         for post in filtered_posts:
#             st.markdown(f"""
#                 <div class="post-container">
#                     <div class="post-id">帖子ID: {post["id"]}</div>
#                     <div class="post-title">{post["title"]} ({post["subject"]})</div>
#                     <div class="post-content">{post["content"]}</div>
#                     <div class="post-content">发帖人 ID: {post["user_id"]}</div>
#             """, unsafe_allow_html=True)
#             view_replies(post["id"])  # 显示帖子回复
#             if st.session_state["logged_in"]:
#                 add_reply(post["id"])  # 添加回复
#             st.markdown("</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="error-message">无法获取帖子：{response.text}</div>', unsafe_allow_html=True)






# # 主页面逻辑
# def main():
#     # st.markdown('<div class="main-container">', unsafe_allow_html=True)
#     st.markdown('<div class="title">AI EDU BBS</div>', unsafe_allow_html=True)

#     check_login()

#     # 创建菜单
#     menu = ["发帖", "查看帖子"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     if st.session_state["logged_in"]:
#         st.markdown(f'<div class="section-header">欢迎, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
        

        
#         if choice == "发帖":
#             create_post()
#         elif choice == "查看帖子":
#             view_posts()

        

#     st.markdown('<div class="footer">AI EDU © 2024. All rights reserved.</div>', unsafe_allow_html=True)

# if __name__ == "__main__":
#      # 检查登录状态
#     if not st.session_state.get("logged_in", False):
#         st.warning("您必须登录才能访问此页面。")
#         st.stop()  # 停止页面继续加载
#     main()






import streamlit as st
import requests
import base64

# FastAPI 后端完整接口 URL
REGISTER_API = "http://127.0.0.1:8000/register"
LOGIN_API = "http://127.0.0.1:8000/login"
CREATE_POST_API = "http://127.0.0.1:8000/create_post"
GET_POSTS_API = "http://127.0.0.1:8000/posts"
ADD_REPLY_API = "http://127.0.0.1:8000/posts/{post_id}/replies"
GET_REPLIES_API = "http://127.0.0.1:8000/posts/{post_id}/replies"


def get_image_as_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 读取本地背景图片并转换为 Base64
background_image_file = "D:/myproject/ML/2024SE-Teamwork-main/src/3.png"  # 替换为你的本地背景图文件
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

# HTML & CSS 样式
st.markdown(""" 
    <style>
        .main-container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            border-radius: 12px;
            background-color: #ffffff;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            opacity: 0.9;
        }

        .title {
            color: #2e3a4a;
            font-size: 2.2em;
            font-weight: 700;
            text-align: center;
            padding: 0.5em 0;
            margin-bottom: 1em;
            border-bottom: 3px solid #a6c1e1;
        }

        .section-header {
            font-size: 1.5em;
            color: #3a5f7d;
            margin-bottom: 0.5em;
            border-bottom: 2px solid #3a5f7d;
            padding-bottom: 0.3em;
            font-weight: 600;
        }

        .post-container {
            border: 1px solid #d9e2ec;
            padding: 1.5em;
            margin: 1.5em 0;
            border-radius: 8px;
            background-color: #ffffff;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.05);
            opacity: 0.9;
        }
        
        .post-title { font-size: 1.3em; font-weight: bold; color: #333; }
        .post-id { font-size: 0.9em; color: #888; margin-top: -5px; }
        
        .post-content { font-size: 1em; color: #555; margin-top: 5px; }
        
        .reply-container {
            margin-top: 10px;
            padding: 10px;
            background-color: #f7f7f9;
            border-radius: 5px;
            border-left: 3px solid #6c757d;
        }

        .reply-author { color: #6c757d; font-weight: bold; }
        .reply-content { color: #333; font-size: 0.95em; margin-top: 5px; }
        
        input[type="text"], input[type="password"], textarea {
            width: 100%;
            padding: 0.8em;
            margin: 0.3em 0;
            border: 1px solid #a6c1e1;
            border-radius: 6px;
            font-size: 1em;
        }
            .reply-box {
            margin-top: 15px;
            padding: 15px;
            background-color: #e9f5fb;
            border: 1px solid #b0d4e1;
            border-radius: 8px;
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
        }

        .reply-box-title {
            font-size: 1.1em;
            font-weight: bold;
            color: #3a5f7d;
        }

        .reply-box-content {
            font-size: 1em;
            color: #555;
            margin-top: 8px;
        }

        input[type="text"], input[type="password"], textarea {
            width: 100%;
            padding: 0.8em;
            margin: 0.3em 0;
            border: 1px solid #a6c1e1;
            border-radius: 6px;
            font-size: 1em;
        }

        .stButton button {
            background-color: #3a5f7d;
            color: #fff;
            padding: 0.8em 1.2em;
            border-radius: 8px;
            font-weight: 600;
        }
        
        .stButton button:hover {
            background-color: #2e4d64;
        }

        .footer {
            font-size: 0.9em;
            color: #6c757d;
            text-align: center;
            padding: 1em 0;
            border-top: 1px solid #ddd;
            margin-top: 2em;
        }
            
        .stExpander {
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 8px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 1em;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# 检查登录状态的函数
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = None
    if "username" not in st.session_state:
        st.session_state["username"] = None

# 用户注册功能
def register():
    st.markdown('<div class="section-header">用户注册</div>', unsafe_allow_html=True)
    username = st.text_input("用户名", key="reg_username")
    password = st.text_input("密码", type="password", key="reg_password")

    if st.button("注册"):
        if username and password:
            response = requests.post(REGISTER_API, json={"username": username, "password": password})
            if response.status_code == 200:
                st.markdown('<div class="success-message">注册成功！请登录。</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="error-message">注册失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-message">请输入用户名和密码。</div>', unsafe_allow_html=True)

# 用户登录功能
def login():
    st.markdown('<div class="section-header">用户登录</div>', unsafe_allow_html=True)
    username = st.text_input("用户名", key="login_username")
    password = st.text_input("密码", type="password", key="login_password")

    if st.button("登录"):
        if username and password:
            response = requests.post(LOGIN_API, json={"username": username, "password": password})
            if response.status_code == 200:
                user_data = response.json()
                st.session_state["logged_in"] = True
                st.session_state["user_id"] = user_data.get("user_id")
                st.session_state["username"] = username
                st.markdown('<div class="success-message">登录成功！</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="error-message">登录失败：{response.json().get("detail", "用户名或密码错误")}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-message">请输入用户名和密码。</div>', unsafe_allow_html=True)

# 发帖功能
def create_post():
    st.markdown('<div class="section-header">发布新帖子</div>', unsafe_allow_html=True)
    title = st.text_input("标题", key="post_title")
    content = st.text_area("内容", key="post_content")
    subject = st.selectbox("选择学科标签", ["语文", "数学", "英语", "物理", "化学", "生物"])

    if st.button("发布"):
        user_id = st.session_state.get("user_id")
        username = st.session_state.get("username")
        if title and content and subject and user_id:
            post_data = {
                "title": title,
                "content": content,
                "subject": subject,
                "user_id": user_id,
                "username": username
            }
            response = requests.post(CREATE_POST_API, json=post_data)
            if response.status_code == 200:
                st.markdown('<div class="success-message">帖子发布成功！</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="error-message">发布失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
        elif not user_id:
            st.markdown('<div class="error-message">请先登录。</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-message">标题、内容和学科标签不能为空！</div>', unsafe_allow_html=True)

def view_replies(post_id):
    response = requests.get(GET_REPLIES_API.format(post_id=post_id))
    if response.status_code == 200:
        replies = response.json()
        if replies:
            for index, reply in enumerate(replies, start=1):  # 使用 enumerate 进行排序并加上楼层数
                st.markdown(f"""
                    <div class="reply-box">
                        <div class="reply-box-title">楼层 {index} - 回复者 {reply['username']}:</div>
                        <div class="reply-box-content">{reply['content']}</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="no-replies">暂无回复</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="error-message">无法获取回复：{response.text}</div>', unsafe_allow_html=True)

# 添加回复
def add_reply(post_id):
    st.markdown('<div class="section-header">添加回复</div>', unsafe_allow_html=True)
    reply_content = st.text_input("回复内容", key=f"reply_content_{post_id}")
    user_id = st.session_state.get("user_id")

    if st.button("回复", key=f"reply_button_{post_id}"):
        if reply_content and user_id:
            reply_data = {"content": reply_content, "post_id": post_id, "user_id": user_id}
            response = requests.post(ADD_REPLY_API.format(post_id=post_id), json=reply_data)
            if response.status_code == 200:
                st.markdown('<div class="success-message">回复成功！</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="error-message">回复失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-message">回复内容不能为空！</div>', unsafe_allow_html=True)

# 视图所有帖子
def view_posts():
    st.markdown('<div class="section-header">所有帖子</div>', unsafe_allow_html=True)
    selected_subject = st.selectbox("按学科标签筛选帖子", ["全部", "语文", "数学", "英语", "物理", "化学", "生物"])

    # 获取帖子列表
    response = requests.get(GET_POSTS_API)
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = [post for post in posts if post["subject"] == selected_subject] if selected_subject != "全部" else posts
        
        for post in filtered_posts:
            with st.expander(f"{post['title']} ({post['subject']})"):
                st.markdown(f"""
                <div class="post-container">
                    <div class="post-id">帖子ID: {post["id"]}，发帖人: {post["username"]}</div>
                    <div class="post-content">{post["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # 显示该帖子的所有回复
                view_replies(post["id"])
                
                # 添加回复
                if st.session_state.get("logged_in"):
                    add_reply(post["id"])

    else:
        st.markdown(f'<div class="error-message">无法获取帖子：{response.text}</div>', unsafe_allow_html=True)

# def view_replies(post_id):
#     response = requests.get(GET_REPLIES_API.format(post_id=post_id))
#     if response.status_code == 200:
#         replies = response.json()
#         if replies:
#             for index, reply in enumerate(replies, start=1):  # 使用 enumerate 进行排序并加上楼层数
#                 st.markdown(f"""
#                     <div class="reply-box">
#                         <div class="reply-box-title">楼层 {index} - 回复者 {reply['username']}:</div>
#                         <div class="reply-box-content">{reply['content']}</div>
#                     </div>
#                 """, unsafe_allow_html=True)

# def add_reply(post_id):
#     st.markdown('<div class="section-header">添加回复</div>', unsafe_allow_html=True)
#     reply_content = st.text_input("回复内容", key=f"reply_content_{post_id}")
#     user_id = st.session_state.get("user_id")

#     if st.button("回复", key=f"reply_button_{post_id}"):
#         if reply_content and user_id:
#             reply_data = {"content": reply_content, "post_id": post_id, "user_id": user_id}
#             response = requests.post(ADD_REPLY_API.format(post_id=post_id), json=reply_data)
#             if response.status_code == 200:
#                 st.markdown('<div class="success-message">回复成功！</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="error-message">回复失败：{response.json().get("detail", "未知错误")}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown('<div class="warning-message">回复内容不能为空！</div>', unsafe_allow_html=True)


# def view_posts():
#     st.markdown('<div class="section-header">所有帖子</div>', unsafe_allow_html=True)
#     selected_subject = st.selectbox("按学科标签筛选帖子", ["全部", "语文", "数学", "英语", "物理", "化学", "生物"])

#     response = requests.get(GET_POSTS_API)
#     if response.status_code == 200:
#         posts = response.json()
#         filtered_posts = [post for post in posts if post["subject"] == selected_subject] if selected_subject != "全部" else posts
#         for post in filtered_posts:
#             with st.expander(f"{post['title']} ({post['subject']})"):
#                 st.markdown(f"""
#                 <div class="post-container">
#                     <div class="post-id">帖子ID: {post["id"]}，发帖人: {post["username"]}</div>
#                     <div class="post-content">{post["content"]}</div>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 view_replies(post["id"])  # 显示帖子回复
#                 if st.session_state["logged_in"]:
#                     add_reply(post["id"])  # 添加回复
#     else:
#         st.markdown(f'<div class="error-message">无法获取帖子：{response.text}</div>', unsafe_allow_html=True)



# 主页面逻辑
def main():
    
    st.markdown('<div class="title">AI EDU BBS</div>', unsafe_allow_html=True)

    check_login()

    # 创建菜单
    menu = ["发帖", "查看帖子"]
    choice = st.sidebar.selectbox("Menu", menu)

    if st.session_state["logged_in"]:
        st.markdown(f'<div class="section-header">欢迎, {st.session_state["username"]}!</div>', unsafe_allow_html=True)
        

        
        if choice == "发帖":
            create_post()
        elif choice == "查看帖子":
            view_posts()
        

    st.markdown('<div class="footer">AI EDU © 2024. All rights reserved.</div>', unsafe_allow_html=True)
    

if __name__ == "__main__":
     # 检查登录状态
    if not st.session_state.get("logged_in", False):
        st.warning("您必须登录才能访问此页面。")
        st.stop()  # 停止页面继续加载
    main()
