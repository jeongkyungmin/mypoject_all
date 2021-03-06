import numpy as np
import pandas as pd
import re

fruit = pd.read_excel('fruit.xlsx',sheet_name='sheet1')

condition_A=(fruit['Spec.']=='전 : 0˚↓, 후 : 1.8˚ ↑(MA)')
fruit=fruit[condition_A]

fruit = fruit[['검사 시간','모델','Suffix','라인','W/O','Spec.','Value']]

fruit = fruit.rename({'Spec.':'Spec','모델':'Model'},axis='columns')

fruit=fruit.dropna()

print("컬럼추출&빈행삭제" + fruit)

apple = pd.read_excel('apple.xlsx',sheet_name='sheet1')

apple = apple[['모델','Suffix','인치시리즈','Stand P/N','Stand (Type)']]

apple = apple.rename({'Stand P/N':'Stand No','Stand (Type)':'Stand','모델':'Model'},axis='columns')

print("신발 종류"+ apple)

fruit = pd.merge(fruit, apple, how='left', on=['Model','Suffix'])

print("fruit과 apple을 merge했어요!..그래야 fruit와 apple을 이용해서 Value값의 구분자로 쓸수 있어요!!" + fruit)

##지금은 신발이 없는것이 있어 날리지만 나중에는 찾아서 복원합니다.
fruit=fruit.dropna()

fruit=fruit.reset_index()

fruit['검사 시간'] = pd.to_datetime(fruit['검사 시간'])
fruit['년월'] = fruit['검사 시간'].apply(lambda x: x.strftime('%Y%m'))
fruit['검사 시간'] = fruit['검사 시간'].apply(lambda x: x.strftime('%m%d'))

fruit.to_excel("output_merge.xlsx", index=True, encoding='utf-8')

print(fruit)

##OLED/UHD 모델 추출 연습
# fruit_OLED = fruit.loc[fruit['Model'].str.contains('OLED')]
#
# print(fruit_OLED)
#
# print(fruit['Model'].str.contains('OLED'))
#
# a = []
# for row in fruit['Model']:
#     if fruit_OLED.Models[row] =='False':
#         a.append('OLED')
#
#     else:
#         a.append('UHD')
#
# fruit['제품군'] = a
#
# print(fruit)
##OLED/UHD 모델 추출 연습

## ok/ng 판정하기

print(fruit['Value'].count())
print(type(float(fruit['Value'].values[0])))

result = []
for row in range(fruit['Value'].count()):
    if float(fruit['Value'].values[row]) > 0.4 and float(fruit['Value'].values[row]) < 1.4:
        result.append('OK')

    else:
        result.append('NG')

fruit['result'] = result

print(fruit.columns)

fruit=fruit[['index','검사 시간','W/O','인치시리즈','Value','result','Stand No','Stand', 'Model', 'Suffix','라인','Spec',
        '년월']]

print(fruit)

fruit.to_excel("result.xlsx", index=True, encoding='utf-8')

# ## graph와 함께 보이는 정보는 아래와 같습니다.

graph_data=fruit[['검사 시간','W/O','인치시리즈','Value','result','Stand No','Stand']]

# ## 이제 모델별로 그래프를 그립니다.
# print(graph_data.groupby('인치시리즈').size())
# graph_data_cnt = pd.DataFrame({'count' : graph_data.groupby('인치시리즈').size()}).reset_index()
# print(graph_data_cnt)

인치시리즈_graph_data= graph_data.groupby('인치시리즈').get_group('32LM63').reset_index()
print(인치시리즈_graph_data)

# graph=graph_data[['인치시리즈','Value']]
# 인치시리즈_graph= graph.groupby('인치시리즈').get_group('32LM63').reset_index()
# print(인치시리즈_graph)
#
# print(인치시리즈_graph['Value'])
# print(type(인치시리즈_graph['Value']))


import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib
font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

x = 인치시리즈_graph_data['검사 시간']
y = 인치시리즈_graph_data['Value']

# fig = plt.figure(figsize=(5, 3))
# ax = fig.add_subplot(1,1,1)
#
# ax.set_xlim(-1,10)
# ax.set_ylim(5,-5)

plt.plot(x,y,'ok', label='32LM63')
plt.legend()

yposition = [1.4,0.4]
for yc in yposition:
    plt.axhline(y=yc, color='r', linestyle='--')

plt.xlabel('날짜')
plt.ylabel('각도')
plt.title('인치 모델별 기울기')

plt.show()




# ## pivot 해보기 : 이건 필요 없을것 같다. 다음 공부를 위해 남겨는 둡니다.

# fruit_table=pd.pivot_table(fruit, index=['Model','Stand','Stand No'], columns='index', values='Value',aggfunc='first')
#
# fruit_table.to_excel("output_table.xlsx", index=True, encoding='utf-8')
# print(fruit_table)


