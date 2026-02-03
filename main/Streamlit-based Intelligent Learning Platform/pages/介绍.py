import streamlit as st
import base64

# 设置页面配置
st.set_page_config(page_title="欢迎界面", layout="centered")

# 欢迎页主要内容
st.title("欢迎使用AI EDU")
st.write("点击下方展开栏获取更多信息.  \nTips：请点击右上角展开栏(三个点)切换成Dark模式获得更好的视觉效果")
    
with st.expander("关于“成绩分析"):
    st.write("1.请分别上传您的历次成绩单以及排名表。  \n2.上传后便会显示可视化图表。  \n3.点击“分析”按钮即可获取分析结果。")

with st.expander("关于“搜题”"):
    st.write("1.您可以上传含有题目的图片，系统会自动识别题目内容。  \n2.点击搜题按钮，稍作等待可以就能获取答案")

with st.expander("关于“论坛”"):
    st.write("1.您可以在论坛中发布任何问题，并选择学科标签来准确定位科目。  \n2.在导航页左下角，您可以自由切换发帖与查看帖子两个页面。  \n注意：请勿发布任何与学习无关的内容，否则将被删帖并封禁！")
with st.expander("关于“题库”"):
    st.write("1.您可以选择所需题型，系统会自动展示对应的题库。")
# 获取本地图像的 Base64 编码
def get_image_as_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 读取本地背景图片并转换为 Base64
background_image_file = "D:\\myproject\\ML\\2024SE-Teamwork-main\src\\7.png"  # 替换为你的本地背景图文件
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
    .welcome-text {{
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Cursive'; /* 设置花体字体 */
    }}
    .enter-button {{
        display: flex;
        justify-content: center;
    }}
    .enter-button button {{
        font-size: 20px;
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }}
    .enter-button button:hover {{
        background-color: #0056b3;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 欢迎界面内容
st.markdown('<div class="welcome-text">感谢使用！</div>', unsafe_allow_html=True)
