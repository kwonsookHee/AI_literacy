import pandas as pd
# 판다스의 데이터프레임 이용한 차트 작성
#df.plot(kind='bar',x='필드',y='필드')
import matplotlib.pyplot  as plt
import numpy as np
import streamlit as st

# 한글 글꼴
plt.rc('font',family = 'malgun gothic')
 
def basic():
       # 파일 불러오기
       df = pd.read_csv('data/한국전력공사_지역별 전기차 현황정보_20230331.csv',encoding='EUC_kr')

       # 피벗 해제(열의 데이터로 변환)
       df_melt = pd.melt(df,id_vars='기준일',value_vars=['서울', '인천', '경기', '강원', '충북', '충남', '대전', '세종', '경북', '대구', '전북',
              '전남', '광주', '경남', '부산', '울산', '제주', '합계'],var_name='지역',value_name='자동차수')

       #년,월 파생변수 생성
       df_melt['년']=df_melt['기준일'].str[:4]
       df_melt['월']=df_melt['기준일'].str[5:7]

       return df_melt

def region_mean(df_melt):

       # ***************************************************
       #지역별, 년도별 자동차수 평균계산 = pivot_table
       year_region_da = round(pd.pivot_table(df_melt,index='년',columns='지역',values='자동차수',aggfunc='mean'))
       st.dataframe(year_region_da)
        
       year_region_da=year_region_da.T
       # 행의 데이터 추출,df[(조건) | (조건)] ,df[(조건) &조건]
       region_query=year_region_da[year_region_da.index != '합계']

       # 데이터 프레임 이용한 차트
       #year_region_da.plot(kind='bar',rot=0)
       ax = region_query.plot(kind='bar',rot=0)
       fig = ax.get_figure()
       st.pyplot(fig)


def mean_2023(df_melt):
       # *************************************************************
       # 2023년 데이터 선택 - 행
       # df_melt 데이터프레임 이용

       df_melt_2023 = df_melt[df_melt['년'] =='2023']
       df_melt_2023 = df_melt_2023[df_melt_2023['지역'] != '합계']
       df_2023 =pd.pivot_table(df_melt_2023,index='지역',columns='월',values='자동차수',aggfunc='mean')
       st.dataframe(df_2023.T)


       ax=df_2023.plot(kind='bar',rot=0)
       fig = ax.get_figure()
       st.pyplot(fig)


def quarter_mean(df_melt):
       # ********************************************************************************
       # 2022년 분기별 분석
       # 2022년 데이터 추출
       df_2022 = df_melt[df_melt['년'] == '2022']
       df_2022['월']=df_2022['월'].astype(int)

       # 조건 비교 함수
       df_2022['분기'] = np.where((df_2022['월'] >= 1) & (df_2022['월'] <= 3), "1분기",
                            np.where ((df_2022['월'] >= 4) & (df_2022['월'] <= 6),"2분기",
                            np.where ((df_2022['월'] >= 7) & (df_2022['월'] <= 9),"3분기",
                            "4분기")))

      

       df_2022_da = round(pd.pivot_table(df_2022,index='지역',columns='분기',values='자동차수',aggfunc='mean'),0)
       st.dataframe(df_2022_da.T)

       #df_2022_da2 =df_2022.groupby(['지역','분기'])[['자동차수']].mean().reset_index()
       #print(df_2022_da2)

       # 판다스를 이용한 차트 작성
       ax =  df_2022_da.plot(kind="bar",rot=0)
       fig = ax.get_figure()
       st.pyplot(fig)
    

# main 실행 
def elec_exe():
       meau = st.selectbox('분석내용',['선택','지역별/연도별 분석','2023년 지역별 분석','2022년 분기별 분석'])
       df_melt = basic()

       if meau == '지역별/연도별 분석':
           region_mean(df_melt)   # 2023년 지역별 분석
       elif meau == '2023년 지역별 분석':
           mean_2023(df_melt)   # 2022년 분기별 분석
       elif meau == '2022년 분기별 분석':
          quarter_mean(df_melt)    
       else:
            st.image('\Ai\A01AL00804bom_VlXZ2FR.jpeg',width=500)   

      
       

# while True:
#        menu=int(input('메뉴 입력(1:지역별/년도별 분석, 2:2023분석,3:2023년 분기별 분석,0:종료)'))

#        if menu == 1 :
#         region_mean(df_melt)
#        elif  menu == 2 :
#         mean_2023(df_melt)
#        elif  menu == 3 : 
#          quarter_mean(df_melt)
#        elif  menu == 0 : 
#         break
#        else: 
#            print('입력 오류')
if __name__ == '__main__': 
  elec_exe()








# 통계:group_by
#df_2022_da2 =df_2022.groupby(['지역','분기'])[['자동차수']].mean().reset_index()



