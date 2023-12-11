import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import country_converter as coco

# ------------------------------------------------------------------------------------------------
# [4] Korea University

st.set_page_config(page_title = "KU")

st.title("QS 세계대학평가 2024")
st.subheader("Ⅳ. 고려대학교")

# ------------------------------------------------------------------------------------------------

with st.sidebar:
    st.image('./images/DATA_KU.jpg', width = 100)

# ------------------------------------------------------------------------------------------------

st.markdown("※ 아래의 제목[탭]을 누르면 다른 시각화 자료를 확인할 수 있습니다.")

# ------------------------------------------------------------------------------------------------


PATH = './datasets/cleaned_qs_24.xlsx'
df24 = pd.read_excel(PATH, index_col=0)

# 4_1. 아시아 주요 대학과의 평가 지표 점수 비교

corr_cols = ['학계 평판', '고용주 평판', '교원 대비 학생 비율', '교원당 논문 피인용수', '외국인 교원 비율', 
             '외국인 학생 비율', '국제 연구 네트워크', '취업 성과', '지속가능성']

def school_scores(institution_name) -> pd.DataFrame :
    institution_scores = df24[df24['학교명'] == institution_name][corr_cols].transpose()
    institution_scores.reset_index(inplace=True)
    institution_scores.columns = ['평가 지표', '점수']
    institution_scores['점수'] = institution_scores['점수'].astype(float)
    return institution_scores

korea_univ = school_scores('Korea University')
snu = school_scores('Seoul National University')
yonsei_univ = school_scores('Yonsei University')
nu_of_singapore = school_scores('National University of Singapore (NUS)') # 학교명 주의 
univ_of_tokyo = school_scores('The University of Tokyo') 


korea_univ['학교명'] = 'Korea University'
snu['학교명'] = 'Seoul National University'
yonsei_univ['학교명'] = 'Yonsei University'
nu_of_singapore['학교명'] = 'National University of Singapore'
univ_of_tokyo['학교명'] = 'University of Tokyo'

compare_univ = pd.concat([korea_univ, snu, yonsei_univ, nu_of_singapore, univ_of_tokyo], axis=0)

fig4_1 = px.line_polar(compare_univ, r='점수', theta='평가 지표',
                        color = '학교명', 
                        color_discrete_map={
                        'Korea University': '#900023', 
                        'Seoul National University': '#0F0F70', 
                        'Yonsei University': '#5B5756', 
                        'National University of Singapore': '#999696', 
                        'University of Tokyo': '#E7BC7B', 
                        }, 
                    line_close=True)
fig4_1.update_layout(template='plotly')
fig4_1.update_layout(height=500, width=1000)
fig4_1.update_polars(radialaxis=dict(dtick=20, range=[0, 100]))
fig4_1.update_traces(line=dict(width=4), selector=dict(name='Korea University'))
fig4_1.update_traces(line=dict(dash='dot'), selector=dict(name='Yonsei University'))


# ------------------------------------------------------------------------------------------------

# 4_2. 평가 지표별 점수 및 총점

compare_univs = ['Korea University',
    'Seoul National University',
    'Yonsei University',
    'National University of Singapore (NUS)',
    'The University of Tokyo']

compare_cols = corr_cols.copy()
compare_cols.append('총점')

univ_df = []

for univ in compare_univs: 
    univ_data = df24[df24['학교명'] == univ][compare_cols].transpose()
    if not univ_data.empty:
        # 열 이름 설정
        univ_data.columns = [univ]
        univ_df.append(univ_data)

# 모든 데이터를 옆으로 이어 붙임
result_df = pd.concat(univ_df, axis=1)



# ------------------------------------------------------------------------------------------------

tab1, tab2 = st.tabs(["아시아 주요 대학과의 평가 지표 점수 비교", "평가 지표별 점수 및 총점"])
with tab1:
    st.plotly_chart(fig4_1, theme=None, use_container_width=True)
with tab2:
    st.dataframe(result_df.T)