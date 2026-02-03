import streamlit as st
import requests
import base64


# FastAPI 后端 URL
REGISTER_API = "http://127.0.0.1:8000/register"
LOGIN_API = "http://127.0.0.1:8000/login"
LOGOUT_API = "http://127.0.0.1:8000/logout"  # 假设后端有这个登出端点










def get_image_as_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 读取本地背景图片并转换为 Base64
background_image_file = "D:\myproject\ML\\2024SE-Teamwork-main\src\\4.png"  # 替换为你的本地背景图文件
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
    <style>
    """,
    unsafe_allow_html=True
)











# 检查登录状态的函数
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False  # 初始化为未登录状态

# 登出功能
def logout():
    # 发送登出请求给后端
    payload = {"username": st.session_state["username"]}
    response = requests.post(LOGOUT_API, json=payload)

    if response.status_code == 200:
        st.session_state["logged_in"] = False  # 清除登录状态
        st.session_state["username"] = None  # 清除用户名
        st.success("You have been logged out!")
    else:
        st.error("Logout failed. Please try again.")

# 添加自定义CSS样式
def add_custom_styles():
    st.markdown("""
    <style>
        /* 整体背景 */
        body {
            background: linear-gradient(135deg, #74EBD5 0%, #ACD8E5 100%);
            font-family: 'Arial', sans-serif;
            overflow-x: hidden;
            padding: 0;
            margin: 0;
        }
        .stApp {
            background-color: transparent;
        }

        /* 页面标题 */
        .title {
            color: #4A90E2;
            text-align: center;
            font-size: 96px;
            font-weight: 700;
            margin-top: 50px;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2);
            letter-spacing: 1px;
            transition: all 0.4s ease-in-out;
        }
        .title:hover {
            color: #0062cc;
            text-shadow: 5px 5px 8px rgba(0, 0, 0, 0.3);
        }

        /* 侧边栏 */
        .sidebar .sidebar-content {
            background-color: #4A90E2;
            color: white;
            padding: 30px 20px;
            border-radius: 15px;
            box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
        }

        /* 按钮 */
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

        /* 输入框 */
        .stTextInput input {
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 12px 18px;
            font-size: 16px;
            width: 100%;
            margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease-in-out;
        }
        .stTextInput input:focus {
            border-color: #4A90E2;
            box-shadow: 0px 0px 10px rgba(74, 144, 226, 0.6);
        }

        # /* 表单卡片 */
        # .card {
        #     background-color: white;
        #     border-radius: 15px;
        #     box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.1);
        #     padding: 30px;
        #     margin-bottom: 50px;
        #     transition: all 0.3s ease;
        # }
        # .card:hover {
        #     transform: translateY(-5px);
        #     box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.15);
        # }

        /* 标题和副标题 */
        .stSubheader {
            font-size: 28px;
            font-weight: 600;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
            letter-spacing: 1px;
            transition: all 0.3s ease;
        }
        .stSubheader:hover {
            color: #0062cc;
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

        /* 页脚 */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-top: 40px;
            font-weight: 600;
        }
        .footer a {
            color: #4A90E2;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        .footer a:hover {
            color: #0062cc;
        }


        /* 扩展的背景动画 */
        .background-animation {
            background: radial-gradient(circle at 50%, #74EBD5 0%, #ACD8E5 100%);
            animation: background-shift 10s infinite linear;
        }
        @keyframes background-shift {
            0% {
                background: radial-gradient(circle at 50%, #74EBD5 0%, #ACD8E5 100%);
            }
            50% {
                background: radial-gradient(circle at 50%, #ACD8E5 0%, #74EBD5 100%);
            }
            100% {
                background: radial-gradient(circle at 50%, #74EBD5 0%, #ACD8E5 100%);
            }
        }

    </style>
    """, unsafe_allow_html=True)

# Streamlit 页面
def main():
    add_custom_styles()  # 添加自定义样式

    st.markdown('<h1 class="title rotate">AI EDU</h1>', unsafe_allow_html=True)

    # 检查登录状态
    check_login()

    # 如果用户已登录，显示登出按钮和主页面内容
    if st.session_state["logged_in"]:
        # st.subheader(f"Welcome, {st.session_state['username']}! (User ID: {st.session_state['user_id']})")
        st.markdown(
     f"""
        <div style="background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;">
            <h1 style="color: #fff; font-size: 50px; text-align: center;">Welcome, {st.session_state['username']}! (User ID: {st.session_state['user_id']})</h1>
        </div>
        """,
        unsafe_allow_html=True
)


        if st.button("Logout"):
            logout()  # 调用登出功能
        return  # 已登录时停止显示登录和注册表单

    # 选择功能：登录或注册
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    # 用户注册界面
    if choice == "Register":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Register")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            if username and password:
                payload = {"username": username, "password": password}
                response = requests.post(REGISTER_API, json=payload)
                if response.status_code == 200:
                    st.success("Registration successful!")
                else:
                    st.error("Error: " + response.json()["detail"])
            else:
                st.warning("Please enter both username and password.")
        st.markdown('</div>', unsafe_allow_html=True)

    # 用户登录界面
    elif choice == "Login":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username and password:
                payload = {"username": username, "password": password}
                response = requests.post(LOGIN_API, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    st.session_state["logged_in"] = True  # 设置登录状态
                    st.session_state["username"] = username  # 保存用户名
                    st.session_state["user_id"] = data.get("user_id")  # 保存用户 ID
                    st.success("Login successful!")
                else:
                    st.error("Error: " + response.json()["detail"])
            else:
                st.warning("Please enter both username and password.")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
