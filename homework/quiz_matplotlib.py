import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False

data = {
  '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
  '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
  '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270],
  '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)

# quiz1. 영화 데이터를 활용하여 x축은 영화, y축은 평점인 막대 그래프를 만드시오.
plt.bar(df.영화,df.평점)
plt.show()

# quiz2. 앞에서 만든 막대 그래프에 제시된 세부 사항을 적용하시오.
# 제목 : 국내 Top 8 영화 평점 정보
# x축 label : 영화 , 값은 90도 회전
# y축 label : 평점
plt.bar(df.영화,df.평점)
plt.title("국내 Top 8 영화 평점 정보")
plt.xlabel("영화")
plt.xticks(rotation=90)
plt.ylabel("평점")
plt.show()

# quiz3. 개봉 연도별 평균 평점 변화 추이를 꺾은선 그래프로 그리시오. 
group = df.groupby(df["개봉 연도"])
grade = group.평점.mean()
plt.plot(grade.index,grade)
plt.show()

# quiz4. 앞에서 만든 막대 그래프에 제시된 세부 사항을 적용하시오.
# marker : o
# x축눈금 : 5년 단위(2005 ~ 2020)
# y축 범위 : 최소 7 최대 10
group = df.groupby(df["개봉 연도"]).mean()
plt.plot(group.index,group.평점,marker="o")
plt.xticks([year for year in range(2005,2021,5)])
plt.ylim(7,10)
plt.show()

# quiz5. 평점이 9점 이상인 영화의 비율을 확인할 수 있는 원 그래프를 제시된 세부 사항을 적용하여 그리시오.
# label : 9점 이상 / 9점 미만
# 퍼센트 : 소수점 첫째자리가지 표시
# 범례 : 그래프 우측에 표시
group = df.groupby(df.평점>=9)
filt = group.영화.count().sort_index(ascending=False)
labels=["9점 이상","9점 미만"]
plt.pie(filt,labels=labels,autopct="%.1f%%")
plt.legend(loc='right')
plt.show()