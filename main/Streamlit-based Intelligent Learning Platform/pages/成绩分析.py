import pandas as pd
import streamlit as st
import numpy as np
import warnings
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import base64

warnings.filterwarnings('ignore')

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
plt.rcParams["font.family"] = "SimHei"  # 设置字体为 SimHei（黑体）
plt.rcParams["font.size"] = 14  # 设置字体大小为 14
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

# Streamlit 界面和处理逻辑
def main():
    st.set_page_config(page_title="学生成绩和排名分析系统")

    # 设置本地背景图
    set_background_image("D:/myproject/ML/2024SE-Teamwork-main/src/6.png")  # 替换为你的背景图片路径

    # 侧边栏设置
    with st.sidebar:
        st.title('学生成绩和排名分析系统')
        st.success('API key 已经配置!', icon='✅')

    # 成绩单文件上传
    st.subheader("上传历次成绩单 (CSV/Excel)")
    grade_file = st.file_uploader(" ", type=["csv", "xlsx"])

    # 排名表文件上传
    st.subheader("上传历次排名 (CSV)")
    rank_file = st.file_uploader(" ", type="csv")

    grade_df, rank_df = None, None

    # 读取成绩单文件
    if grade_file is not None:
        if grade_file.name.endswith(".csv"):
            grade_df = pd.read_csv(grade_file)
        elif grade_file.name.endswith(".xlsx"):
            grade_df = pd.read_excel(grade_file)

        # 显示成绩单表格内容
        st.write("### 学生成绩单预览")
        st.write(grade_df)

        # 1. 折线图：用户可以选择最多三个科目显示每次考试成绩变化
        st.subheader("科目成绩趋势图")
        subject_options = grade_df.columns.tolist()
        selected_subjects = st.multiselect("选择科目以查看趋势", subject_options, default=subject_options[:3])
        if selected_subjects:
            df_selected = grade_df[selected_subjects]
            st.line_chart(df_selected)

        # 2. 平均成绩趋势图
        st.subheader("平均成绩趋势图")
        grade_df['平均分'] = grade_df.mean(axis=1)
        st.bar_chart(grade_df['平均分'])

        # 3. 各科目成绩分布直方图
        st.subheader("各科目成绩分布直方图")
        columns = st.columns(2)
        colors = sns.color_palette("husl", len(grade_df.columns) - 1).as_hex()
        for i, column in enumerate(grade_df.columns):
            if column != '平均分':
                with columns[i % 2]:
                    fig, ax = plt.subplots()
                    sns.histplot(grade_df[column], kde=True, color=colors[i], ax=ax)
                    ax.set_title(f'{column} 成绩分布')
                    st.pyplot(fig)

        # 4. 各科目成绩箱线图
        st.subheader("各科目成绩箱线图")
        fig_box = px.box(grade_df.iloc[:, :-1], title="各科目成绩箱线图")
        st.plotly_chart(fig_box)

        # 5. 各科目成绩热力图
        st.subheader("各科目成绩热力图")
        fig_heatmap = px.imshow(grade_df.iloc[:, :-1].T, title="各科目成绩热力图", color_continuous_scale=px.colors.sequential.Viridis)
        st.plotly_chart(fig_heatmap)

        # 6. 成绩占比饼图
        st.subheader("成绩占比饼图")
        selected_row = st.selectbox("选择行以查看各科目成绩占比", grade_df.index)
        row_data = grade_df.iloc[selected_row, :-1]
        fig_pie = px.pie(names=row_data.index, values=row_data.values, title=f"第 {selected_row + 1} 次考试成绩占比")
        st.plotly_chart(fig_pie)

        # 7. 成绩散点图：对比两科成绩
        st.subheader("科目成绩散点图")
        x_axis = st.selectbox("选择 X 轴科目", subject_options)
        y_axis = st.selectbox("选择 Y 轴科目", subject_options, index=1)
        scatter_chart = alt.Chart(grade_df).mark_circle(size=200).encode(
            x=alt.X(x_axis, title=x_axis),
            y=alt.Y(y_axis, title=y_axis),
            color=alt.Color(x_axis, scale=alt.Scale(scheme='blueorange'))
        ).properties(title=f'{x_axis} 与 {y_axis} 成绩对比')
        st.altair_chart(scatter_chart, use_container_width=True)

        # 8. 科目平均成绩条形图
        st.subheader("各科目平均成绩条形图")
        df_avg = grade_df.mean().reset_index()
        df_avg.columns = ['科目', '平均成绩']
        fig_bar = px.bar(df_avg, x='科目', y='平均成绩', title="各科目平均成绩")
        st.plotly_chart(fig_bar)

    # 读取排名表文件
    if rank_file is not None:
        rank_df = pd.read_csv(rank_file)
        st.write("### 学生排名表预览")
        st.write(rank_df)

        # 排名数据雷达图
        st.subheader("排名表雷达图")
        subjects = rank_df.columns.tolist()
        row = st.number_input("输入行号以查看排名百分比", min_value=1, max_value=len(rank_df), value=1) - 1
        total_students = st.number_input("总学生人数", min_value=1, value=100)
        if row < len(rank_df):
            rankings = rank_df.iloc[row].values
            percentages = [(total_students - rank) / total_students * 100 for rank in rankings]
            fig = px.line_polar(r=percentages, theta=subjects, line_close=True)
            fig.update_traces(fill='toself')
            st.plotly_chart(fig)

    # 传输数据给大模型并分析
    if grade_df is not None and rank_df is not None:
        grade_data_json = grade_df.to_json(orient="split")
        rank_data_json = rank_df.to_json(orient="split")

        if st.button("分析"):
            st.subheader("分析")
            spark_model = init_spark_model()
            prompt = f"""### 请对以下学生的历次成绩变化和排名情况，针对学科学习侧重点提出建议：
            \n\n成绩单数据：\n{grade_data_json}\n\n排名表数据：\n{rank_data_json}"""
            messages = [ChatMessage(role="user", content=prompt)]
            handler = ChunkPrintHandler()

            # 调用星火模型进行分析和建议生成
            response = spark_model.generate([messages], callbacks=[handler])
            analysis_and_plan = response.generations[0][0].text  # 提取分析结果与学习计划

            # 显示分析结果与学习计划
            st.markdown(analysis_and_plan)

if __name__ == '__main__':
    # 检查登录状态
    if not st.session_state.get("logged_in", False):
        st.warning("您必须登录才能访问此页面。")
        st.stop()  # 停止页面继续加载
    main()
