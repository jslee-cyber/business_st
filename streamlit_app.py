import streamlit as st
st.markdown("""
<h5 style="text-align:center; color:gray;">일상/고민</h5>
<h2 style="text-align:center;">서울의 교통체증, 숫자로 풀어보기</h2>
""", unsafe_allow_html=True)
st.write('')
# 프로필 사진 + 작성자 정보 (왼쪽 정렬)
col1, col2, col3, col4 = st.columns([0.035, 0.15, 0.45, 0.1])

with col1:
    st.image("./data/photo.png", width=30) 
with col2:
    st.markdown("**C431195 이준성**")

with col3:
    st.markdown("<span style='color:gray;'>2025. 6. 17. 17:00</span>", unsafe_allow_html=True)

with col4:
    st.button("이웃추가")

st.divider()
st.write("###### 운전을 시작한지 어느덧 1년. \n자칭 '운전 고수'가 되었지만, 한 가지 고민이 생겼다.  \n그건 바로 서울의 무서운 교통체증.  \n초보 시절엔 앞만 보느라 몰랐던 교통체증이, 지금은 일상의 작지만 큰 스트레스가 되었다.  \n막히는 퇴근시간 속 차에 앉아있자니, 문득 이런 궁금증이 생겼다. ")
st.write('')
st.write('##### "지금 서울에 차가 몇 대나 있을까?"\n')
st.write('')

st.image("./data/1920px.jpg", caption='가끔은 걷는 게 빠를 것 같다는 생각이 든다. (사진= flickr)', use_container_width=True)
st.write('')
st.write('')
st.write("###### 가장 막히는 때, 서울에 차가 몇 대 있는지 알 수 있는 방법은 없을까?\n측정하기 어려운 정보라 그런지, 아무리 검색해도 찾을 수가 없었다. 여기저길 헤매던 중, 마침 서울시에서 교통량을 전수조사해 공개한 자료를 발견했다.\n바로 TOPIS(서울시 교통정보센터)에서 제공하는 <2023 서울시 교통량 조사자료>. 궁금하면 아래 링크로 들어가 연도별 통계를 살펴보자. ")
st.markdown(
    '''
    - [연도별 서울시 교통량 조사자료](https://topis.seoul.go.kr/refRoom/openRefRoom_2.do)
    '''
    )
st.write('')
st.write('')
st.text('자료를 살펴보니 다음과 같은 내용을 알 수 있었다.')
st.write('')
col1, col2, col3 = st.columns(3) # 3개의 컬럼 생성
col1.metric ("서울시 일평균 교통량", "1026.5만 대") 
col2.metric("주요도로 개수", "139개") 
col3.metric("주요도로 당 평균 차선 개수", "8차선")

st.write('')
st.write('')
st.text('총 차선 수가 139 × 8=1112(개)라고 해보자. 검색해보니 차선 1개의 용량은 시간 당 약 1000대이며 통상 도로용량의 50% 이상 차면 교통혼잡으로 인식한다고 한다. 그럼 다음과 같은 식이 나온다.')
st.info('1112(개) × 1000(대/시간) × 0.5(혼잡도) = 55.6만대', icon="💡")
st.write('')
st.write('')
'''그렇다. **시간당 55.6만 대 이상의 교통량이 존재할 때** 서울시가 교통체증을 겪는 것이다. 뿌듯한 발견이 아닐 수 없다. 하지만 여기에서 멈추기는 아쉽다. 한 발 더 나아가, '실제로' 서울의 혼잡 시간대에 존재하는 교통량을 구해보자.
'''  
st.write('')
st.text('일단 시간대별 교통량을 알아야 한다. 앞서 살펴본 교통량 자료에서 정보를 추출하여, 다음과 같이 그래프를 만들어봤다.')
st.write('')
st.write('')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = "fonts/malgun-gothic.ttf"
fontprop = fm.FontProperties(fname=font_path)

# matplotlib 한글 설정
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False

time_labels = [
    "00-01", "01-02", "02-03", "03-04", "04-05", "05-06", "06-07", "07-08", "08-09", "09-10",
    "10-11", "11-12", "12-13", "13-14", "14-15", "15-16", "16-17", "17-18", "18-19", "19-20",
    "20-21", "21-22", "22-23", "23-24"
]

traffic_volume = [
    192, 137, 107, 92, 133, 287, 468, 586, 602, 571, 546, 534,
    522, 536, 545, 555, 576, 587, 572, 516, 466, 443, 393, 293
]

plt.figure(figsize=(12, 6))
plt.bar(time_labels, traffic_volume)
plt.title("서울시 시간대별 교통량 (주중)", fontproperties=fontprop)
plt.xlabel("시간대", fontproperties=fontprop)
plt.ylabel("교통량 (천 대)", fontproperties=fontprop)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

st.write('')
st.write('')
st.text('주중 통계이고 단위는 천 대다. 앞서 구했듯, 서울시의 교통체증은 시간당 55.6만 대 이상의 차량이 존재할 때 발생한다. 그래프 상에서 막대가 556 위로 그려지는 시간대는 총 6개로, 이때의 교통량을 모두 합하면 총 349.4만대이다.')
st.write('')
'''주말엔 어떨까. 다시 자료를 살펴보자. 주중 일평균 교통량은 1025.9만 대, 주말 일평균 교통량은 898.6만대라고 한다. 이 비율을 고려하면 주말에는 307.5만대가 교통혼잡에 연루된다고 할 수 있고, 다시 주중 일수와 주말 일수의 비율을 고려하면 **결론적으로 하루 총 337.4만대가 서울의 교통혼잡을 유발**한다고 볼 수 있다.
'''
st.write('')
st.write('')
st.write('')

'''그렇다. 서울은 **하루의 4분의 1일**을 교통체증에 시달리며, 시간대에 따라 55.6만 대를 훌쩍 넘은 **60만 대**까지도 거리로 나온다. 하루종일로 따지면 **340만 대**에 달하는 차량이 뒤엉켜 혼잡을 유발한다.\n
'''
st.write('')
'''\n숫자로 보니, 명확하다.
'''
st.write('')
st.divider()
st.write('')
st.write('##### 그렇다면 교통체증, 얼마나 무서운 걸까?')
'''나 하나도 힘든데, 사회 전체로 봤을 때는 어떤 피해를 만들어내고 있을까.
'''
st.write('')
st.write('')
col1, col2, col3 = st.columns(3) 
col1.metric("연간 총 사회적 비용", "약 64조 원") 
col2.metric("연간 총 시간가치의 손실", "약 50조 원") 
col3.metric("OECD 연간 교통사고 사망자 수", "6위")
st.caption("출처: 한국교통연구원, ʻ국가 교통정책 평가지표 조사사업’ (2023) / 도로교통공단, ʻOECD 회원국 교통사고 비교’ (2021)")
st.write('')
st.write('')
'''꽤 충격적인 수치다. 연간 64조 원이면 현대중공업(HD 현대)의 재작년도 매출액과 맞먹는 금액이다. 이런 돈이 매년 도로 위에 버려진다고 해도 과언이 아닌 것이다.'''
st.text('교통사고 또한 교통체증과 밀접한 관련이 있다. 교통량이 많고 혼잡할수록 사고가 발생할 확률이 높다. 우리나라는 교통사고 사망자 수, 특히 이 중 보행자 비율로는 전세계 상위권이다. 교통체증이 얼마나 심각한지, 그리고 얼마나 위험한지 간접적으로 보여주는 지표다.')
'''환경 문제는 말할 것도 없다. 교통체증으로 인해 차량이 정체되면 연료 소모가 증가하고, 이는 대기오염을 악화시킨다는 건 상식이다. 그래서 전세계 도시들이 골머리를 앓는다. 규모가 작은 도시들 중엔 자동차와 아예 이별한 곳들도 있다. 교통체증 없는 삶, 상상할 수 있겠는가.'''
st.write('')
st.write('')
st.write('')
st.image("./data/spain.jpeg", caption='차 없는 도시, 스페인의 폰테베드라. (사진= Planetizen)', use_container_width=True)
st.write('')
st.write('')
st.image("./data/brazil.jpeg", caption='버스로 모든 것을 대체한 브라질의 꾸리찌바. (사진= ETRI WEBZINE)', use_container_width=True)
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.markdown('#### 마치며...')
st.write('')
'''그간 교통체증을 줄이기 위해 수많은 노력이 있어왔다는 점은 분명하다. 대중교통 개선, 도로 확충 등의 인프라 투자로 상당부분 개선된 것이 사실이다. 머지 않아 전기차와 자율주행차의 대중화로 환경오염과 사고발생 확률이 크게 줄어들 것이란 전망도 있다. 하지만 당장의 문제를 무시할 수는 없다. **하루 337.4만 대를 어떻게 해야 할 것인가.** 서울시의 고민도 클 것이다. 
\n서울을 폰테베드라나 꾸리찌바로 만들 수는 없다. 규모나 인구밀도 면에서 비교 자체가 어렵다. 서울의 교통체증을 줄이려면, :green[**운전자 개개인의 행동변화가 이루어지는 수 밖에 없다.**] 이동 시간대를 조절하거나 차선변경을 최소화하는 등 교통흐름을 방해하지 않으려는 노력부터, 여유 있는 날에는 대중교통과 도보를 이용하는 등 개인 수준의 근본적인 변화가 필요하다. 일단 나부터 이러한 노력을 시작해보려 한다. 이 글을 본 당신도, 자동차에 조금 소홀해지면 어떨까. 오랜만에 타는 버스, 가까운 목적지로 힘차게 내딛는 걸음이 일상에 산뜻한 즐거움이 될 수 있을 것이다.
'''
st.write('')

st.divider()
col1, col2 = st.columns([0.5,0.07])
with col1:
    st.button("♥ 공감")
with col2:
    st.button(" ➦ 공유")





