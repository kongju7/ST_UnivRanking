import streamlit as st 

st.set_page_config(
    page_title = "QS2024",
)

st.markdown("""
   
# QS 세계대학평가 2024
   
[QS 세계대학평가 2024년 자료](https://www.topuniversities.com/world-university-rankings)를 활용하여 시각화한 결과를 제공합니다.   
왼쪽 사이트바의 메뉴를 클릭하거나,   
아래의 링크를 클릭하면 해당 지역별 주요 대학 분포 결과를 확인하실 수 있습니다.  

- <a href="/World" target="_self">World</a> : 전세계 600위권 주요 대학 분포 
- <a href="/Asia" target="_self">Asia</a> : 아시아권 주요 대학 분포 
- <a href="/Korea" target="_self">Korea</a> : 국내 주요 대학 분포 
- <a href="/KU" target="_self">KU</a> : 고려대와 아시아 주요 대학 평가 지표별 점수 비교
            """, unsafe_allow_html=True)



with st.sidebar:
    st.image('./images/DATA_KU.jpg', width = 100)
