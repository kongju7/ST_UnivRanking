import streamlit as st 

st.set_page_config(
    page_title = "QS2024",
)


st.markdown(
    """

# QS 세계대학평가 2024 
  
  
[QS 세계대학평가 2024년 자료](https://www.topuniversities.com/world-university-rankings)를 활용하여 시각화한 결과를 제공합니다.   
왼쪽 사이트바의 메뉴를 클릭하거나,   
아래의 링크를 클릭하면 해당 지역별 주요 대학 분포 결과를 확인하실 수 있습니다.   
  
  
- [World](/World) : 전세계 600위권 주요 대학 분포  
- [Asia](/Asia) : 아시아권 주요 대학 분포 
- [Korea](/Korea) : 국내 주요 대학 분포 
- [KU](/KU) : 고려대와 아시아 주요 대학 평가 지표별 점수 비교     
    """
)


with st.sidebar:
    st.image('./images/DATA_KU.jpg', width = 100)
