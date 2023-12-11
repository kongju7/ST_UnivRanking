import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import country_converter as coco
import folium 
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium 

# ------------------------------------------------------------------------------------------------
# [3] Korea 

st.set_page_config(page_title = "Korea")

st.title("QS 세계대학평가 2024")
st.subheader("Ⅲ. 국내 주요 대학")

# ------------------------------------------------------------------------------------------------

with st.sidebar:
    st.image('./images/DATA_KU.jpg', width = 100)

# ------------------------------------------------------------------------------------------------

st.markdown("※ 아래의 제목[탭]을 누르면 다른 시각화 자료를 확인할 수 있습니다.")

# ------------------------------------------------------------------------------------------------

KOR_PATH = './datasets/merged_kor_qs_24.xlsx'
kor_df24 = pd.read_excel(KOR_PATH, index_col=0)

# 3_1. 국내 대학 분포 지도 

m = folium.Map(location=[36.2, 127.5], tiles = 'CartoDB positron' , zoom_start=6.5) # [위도(lat), 경도(lon)]

marker_cluster = MarkerCluster().add_to(m)

for lat, long in zip(kor_df24['y'], kor_df24['x']):
    folium.Circle([lat, long], radius = 2000, color = '#005506').add_to(marker_cluster)

# ------------------------------------------------------------------------------------------------

# 3_2. 2023~24년 순위 변동
kor_rank_change = kor_df24.groupby('name_abb')['순위 변동'].mean().sort_values(ascending=True)

fig3_2 = px.bar(x=kor_rank_change.index, y=kor_rank_change.values,
            text=np.round(kor_rank_change.values),
            title='<b></b>',
            color=kor_rank_change.values,
            color_continuous_scale='YlGn')

fig3_2.update_layout(xaxis_title='학교명',
                    yaxis_title='순위 변동',
                    height=400, width=1000)

fig3_2.update_traces(marker_line_color='black', 
                    marker_line_width=1.5, 
                    opacity=0.8)

# ------------------------------------------------------------------------------------------------

# 3_3. 총점 및 순위

cols = ['학교명', '총점', '2024 RANK_ori', '2023 RANK_ori']
rank_kor_df24 = kor_df24[cols]
rank_kor_df24.columns = ['대학명', '총점', '2024년 순위', '2023년 순위']

# ------------------------------------------------------------------------------------------------

# 3_4. 평가 지표별 점수

compare_cols = ['학교명', '학계 평판', '고용주 평판', '교원 대비 학생 비율', '교원당 논문 피인용수', '외국인 교원 비율', 
             '외국인 학생 비율', '국제 연구 네트워크', '취업 성과', '지속가능성', '총점']
com_kor_df24 = kor_df24[compare_cols].reset_index(drop = True)

# ------------------------------------------------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(["국내 대학 분포 지도", "2023~24년 순위 변동", "총점 및 순위", "평가 지표별 점수"])
with tab1:
    st.markdown("###### [국내 대학 분포 지도]")
    st_data = st_folium(m, width = 500, height = 400)
with tab2:
    st.markdown("###### [2023~24년 순위 변동]")
    st.plotly_chart(fig3_2, theme="streamlit", use_container_width=True)
with tab3:
    st.markdown("###### [총점 및 순위]")
    st.dataframe(rank_kor_df24)
with tab4:
    st.markdown("###### [평가 지표별 점수]")
    st.dataframe(com_kor_df24)