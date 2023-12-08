import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.io as pio
## Country Code ## 
import country_converter as coco

# matplotlib defaults
plt.style.use("seaborn-v0_8-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)

from matplotlib import font_manager, rc 
font_path = 'C://Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family=font)

import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title = "World",
)


st.title("QS 세계대학평가 2024")

st.subheader("전세계 600위권 대학")

with st.sidebar:
    file = st.file_uploader(".txt .pdf .docx 형식의 파일을 업로드하세요.", 
                            type = ["pdf", "txt", "docx"])

# ------------------------------------------------------------------------------------------------

PATH = './datasets/cleaned_qs_24.xlsx'
df24 = pd.read_excel(PATH, index_col=0)

# 1. 전세계 대학 분포 지도 

country_codes = coco.convert(df24['국가'], to='ISO3')
country_codes = pd.Series(country_codes)
university_location = country_codes.value_counts()

fig1 = px.choropleth(locations=university_location.index,
                    color=university_location.values,
                    color_continuous_scale=px.colors.sequential.YlGn)
fig1.update_layout(height=500, width=800)
fig1.update_layout(template='simple_white')

# ------------------------------------------------------------------------------------------------
# 2. 국가별 대학 평균 총점 상위 20위권 국가
top20_score_country = df24.groupby('국가')['총점'].mean().sort_values(ascending=False)[:20]

fig2 = px.bar(x=top20_score_country.index, y=top20_score_country.values,
            text=np.round(top20_score_country.values),
            color=top20_score_country.values,
            color_continuous_scale='YlGn')

fig2.update_layout(xaxis_title='국가',
                  yaxis_title='평균 총점',
                  height=450, width=1000, 
                 )
fig2.update_traces(marker_line_color='black', 
                  marker_line_width=1.5, 
                  opacity=0.8)


# ------------------------------------------------------------------------------------------------

# top 20개 대학과 고려대학교 
top20_df24 = df24[:20]
korea_df24 = df24.loc[df24['학교명'] == 'Korea University']
top20_df24_with_korea = pd.concat([top20_df24, korea_df24])

top20_rank_change = top20_df24_with_korea.groupby('학교명')['순위 변동'].mean().sort_values(ascending=True)

fig3 = px.bar(x=top20_rank_change.index, y=top20_rank_change.values,
            text=np.round(top20_rank_change.values),
            color=top20_rank_change.values,
            color_continuous_scale='YlGn')

fig3.update_layout(xaxis_title='학교명', 
                   yaxis_title='순위 변동',
                   height=600, width=1000)

fig3.update_traces(marker_line_color='black', 
                  marker_line_width=1.5, 
                  opacity=0.8)

# ------------------------------------------------------------------------------------------------





# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["1. 전세계 대학 분포 지도", "상위 20위권 국가" , "2023~24년 주요 대학 순위 변동"])
with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
with tab3:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)