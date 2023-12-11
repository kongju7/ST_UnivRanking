import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import country_converter as coco

# ------------------------------------------------------------------------------------------------
# [2] Asia 

st.set_page_config(page_title = "Asia")

st.title("QS 세계대학평가 2024")
st.subheader("Ⅱ. 아시아 주요 대학")

# ------------------------------------------------------------------------------------------------

with st.sidebar:
    st.image('./images/DATA_KU.jpg', width = 100)


# ------------------------------------------------------------------------------------------------

st.markdown("※ 아래의 제목[탭]을 누르면 다른 시각화 자료를 확인할 수 있습니다.")

# ------------------------------------------------------------------------------------------------


ASIA_PATH = './datasets/asia_df24.xlsx'
asia_df24 = pd.read_excel(ASIA_PATH, index_col = 0)
top20_aisa_df24 = asia_df24.head(20)

# 2_1. 아시아 주요 대학 2023~24년 순위 변동

asia_rank_change = top20_aisa_df24.groupby('학교명')['순위 변동'].mean().sort_values(ascending=True)

fig2_1 = px.bar(x=asia_rank_change.index, y=asia_rank_change.values,
            text=np.round(asia_rank_change.values),
            color=asia_rank_change.values,
            color_continuous_scale='YlGn')

fig2_1.update_layout(xaxis_title='학교명',
                    yaxis_title='순위 변동',
                    height=600, width=1000)

fig2_1.update_traces(marker_line_color='black', 
                    marker_line_width=1.5, 
                    opacity=0.8)

# ------------------------------------------------------------------------------------------------

# 2_2. 총점 및 순위

cols = ['학교명', '국가','총점', '2024 RANK_ori', '2023 RANK_ori']
rank_top20_aisa_df24 = top20_aisa_df24[cols]
rank_top20_aisa_df24.columns = ['대학명', '국가','총점', '2024년 순위', '2023년 순위']
rank_top20_aisa_df24 = rank_top20_aisa_df24.reset_index(drop = True)
rank_top20_aisa_df24.index = range(1, len(rank_top20_aisa_df24) + 1)

# ------------------------------------------------------------------------------------------------

# 2_3. 평가 지표별 점수

top20_aisa_df24 = asia_df24.head(20)

compare_cols = ['학교명', '학계 평판', '고용주 평판', '교원 대비 학생 비율', '교원당 논문 피인용수', '외국인 교원 비율', 
             '외국인 학생 비율', '국제 연구 네트워크', '취업 성과', '지속가능성', '총점']
com_top20_aisa_df24 = top20_aisa_df24[compare_cols].reset_index(drop = True)
com_top20_aisa_df24.index = range(1, len(com_top20_aisa_df24) + 1)

# ------------------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["아시아 주요 대학 2023~24년 순위 변동", "총점 및 순위", "평가 지표별 점수"])
with tab1:
    st.markdown("###### [아시아 주요 대학 2023~24년 순위 변동]")
    st.plotly_chart(fig2_1, theme="streamlit", use_container_width=True)
with tab2:
    st.markdown("###### [총점 및 순위]")
    st.dataframe(rank_top20_aisa_df24)
with tab3:
    st.markdown("###### [평가 지표별 점수]")
    st.dataframe(com_top20_aisa_df24)