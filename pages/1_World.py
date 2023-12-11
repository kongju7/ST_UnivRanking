import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import country_converter as coco

# ------------------------------------------------------------------------------------------------
# [1] World 

st.set_page_config(page_title = "World")

st.title("QS 세계대학평가 2024")
st.subheader("Ⅰ. 전세계 600위권 대학")

# ------------------------------------------------------------------------------------------------

with st.sidebar:
    st.image('./images/DATA_KU.jpg', width = 100)

# ------------------------------------------------------------------------------------------------

st.markdown("※ 아래의 제목[탭]을 누르면 다른 시각화 자료를 확인할 수 있습니다.")

# ------------------------------------------------------------------------------------------------

PATH = './datasets/cleaned_qs_24.xlsx'
df24 = pd.read_excel(PATH, index_col=0)

# 1_1. 전세계 대학 분포 지도 

country_codes = coco.convert(df24['국가'], to='ISO3')
country_codes = pd.Series(country_codes)
university_location = country_codes.value_counts()

fig1_1 = px.choropleth(locations=university_location.index,
                    color=university_location.values,
                    color_continuous_scale=px.colors.sequential.YlGn)
fig1_1.update_layout(height=500, width=800)
fig1_1.update_layout(template='simple_white')

# ------------------------------------------------------------------------------------------------
# 1_2. 국가별 대학 평균 총점 상위 20위권 국가
top20_score_country = df24.groupby('국가')['총점'].mean().sort_values(ascending=False)[:20]

fig1_2 = px.bar(x=top20_score_country.index, y=top20_score_country.values,
            text=np.round(top20_score_country.values),
            color=top20_score_country.values,
            color_continuous_scale='YlGn')

fig1_2.update_layout(xaxis_title='국가',
                  yaxis_title='평균 총점',
                  height=400, width=1000, 
                 )
fig1_2.update_traces(marker_line_color='black', 
                  marker_line_width=1.5, 
                  opacity=0.8)


# ------------------------------------------------------------------------------------------------

# 1_3. 주요 대학 2023~24년 순위 변동
top20_df24 = df24[:20]
korea_df24 = df24.loc[df24['학교명'] == 'Korea University']
top20_df24_with_korea = pd.concat([top20_df24, korea_df24])

top20_rank_change = top20_df24_with_korea.groupby('학교명')['순위 변동'].mean().sort_values(ascending=True)

fig1_3 = px.bar(x=top20_rank_change.index, y=top20_rank_change.values,
            text=np.round(top20_rank_change.values),
            color=top20_rank_change.values,
            color_continuous_scale='YlGn')

fig1_3.update_layout(xaxis_title='학교명', 
                   yaxis_title='순위 변동',
                   height=600, width=1000)

fig1_3.update_traces(marker_line_color='black', 
                  marker_line_width=1.5, 
                  opacity=0.8)

# ------------------------------------------------------------------------------------------------


# 1_4. 평가 지표별 점수

compare_cols = ['학교명', '학계 평판', '고용주 평판', '교원 대비 학생 비율', '교원당 논문 피인용수', '외국인 교원 비율', 
             '외국인 학생 비율', '국제 연구 네트워크', '취업 성과', '지속가능성', '총점']
com_df24 = top20_df24_with_korea[compare_cols].reset_index(drop = True)


# ------------------------------------------------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(["전세계 대학 분포 지도", "상위 20위권 국가", "주요 대학 2023~24년 순위 변동", "주요 대학 평가 지표별 점수 및 총점"])
with tab1:
    st.markdown("###### [전세계 대학 분포 지도]")
    st.plotly_chart(fig1_1, theme="streamlit", use_container_width=True)
with tab2:
    st.markdown("###### [상위 20위권 국가]")
    st.plotly_chart(fig1_2, theme="streamlit", use_container_width=True)
with tab3:
    st.markdown("###### [주요 대학 2023~24년 순위 변동]")
    st.plotly_chart(fig1_3, theme="streamlit", use_container_width=True)
with tab4:
    st.markdown("###### [주요 대학 평가 지표별 점수 및 총점]")
    st.dataframe(com_df24)
    
