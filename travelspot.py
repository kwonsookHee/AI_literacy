import random
import streamlit as st
 
def shop():
  menu =st.radio('메뉴선택',['옷and화장품', '신발', 'k-pop 굿즈', '가구'])

  if menu=='옷and화장품':
    a=["동대문 닭한마리 골목","순미네 행복게장","도깨비 불고기","청도미나리식당"]
    st.write(f'동대문:{random.choice(a)}')
  elif menu=='신발':
    b=["더 써드햄","쭈꾸미234","동키호테","성수두부","만동제과"]
    st.write(f'신발:{random.choice(b)}')
  elif menu=='k-pop 굿즈':
    c=["명동교자","목멱산방","강남면옥","남포면옥","하동관"]
    st.write(f'k-pop 굿즈:{random.choice(c)}')
  elif menu=='가구':
    d=["일산칼국수","청담특양평해장국","옥소반","청산별곡","조선초가한끼"]
    st.write(f'가구:{random.choice(d)}')


def history(): # 역사 탐방 함수 정의
    pal=['덕수궁','경북궁','경희궁','창경궁','창덕궁']
    musium=['전쟁기념관','국립중앙박물관','국립민속박물관','서울역사박물관','국립 고궁 박물관','대한민국 역사 박물관']
    hand=['남산국악당','서울풍물 시장','남산골 한옥 마을','북촌 한옥 체험']
    menu2 =st.radio('메뉴선택',['궁궐',  '박물관',  '전통문화 체험'])

    if menu2=='궁궐':
        st.write(f'추천하는 궁궐은 {random.choice(pal)}입니다')
    elif menu2=='박물관':
        st.write(f'추천하는 박물관은 {random.choice(musium)}입니다')
    elif menu2=='전통문화 체험':
        st.write(f'추천하는 전통 체험은 {random.choice(hand)}입니다')
    else:
        st.write(f'입력 오류입니다')


def sook():
  leisure_dict = {
    '산': ['암벽등반(도봉산)', '스키(양지파인리조트)', '산악자전거(천마산)', '캠핑(난지캠핑장)', '패러글라이딩(정광산)'],
    '바다': ['서핑(화성)', '제트스키(제부도)', '수상스키(양평)', '바나나보트(가평,양평)', '웨이크보드(양평)']
  }
  choice =st.radio('메뉴선택',['산','바다'])
 

  if choice in leisure_dict:
    chosen_activity = random.choice(leisure_dict[choice])
    st.write(f'레저 추천: {chosen_activity} ')
  else:
    st.write('입력 오류')

def travle_main():
    menu = st.selectbox('여행지 선택',['쇼핑-맛집','역사 탐방','레저'])
   
    if menu=='쇼핑-맛집':
       shop()

    elif menu=='역사 탐방':
      history()
        
    elif menu=='레저':
      sook()
   
    else:
       st.write('입력오류')


#travle_main()
