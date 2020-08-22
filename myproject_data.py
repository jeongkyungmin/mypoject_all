import numpy as np
import pandas as pd
import re


fruit = pd.read_excel('fruit.xlsx',sheet_name='sheet1')

condition_A=(fruit['Spec.']=='전 : 0˚↓, 후 : 1.8˚ ↑(MA)')
fruit=fruit[condition_A]

fruit = fruit[['검사 시간','모델', 'Suffix','라인','W/O','Spec.','Value']]

fruit=fruit.dropna()

print(fruit)

apple = pd.read_excel('apple.xlsx',sheet_name='sheet1')

apple = apple[['모델','Suffix','Stand P/N','Stand (Type)']]

print(apple)

friut = pd.merge(fruit, apple, how='left', on=['모델','Suffix'])

friut['검사 시간'] = pd.to_datetime(friut['검사 시간'])
friut['년월'] = friut['검사 시간'].apply(lambda x: x.strftime('%Y%m'))
friut['검사 시간'] = friut['검사 시간'].apply(lambda x: x.strftime('%m%d'))

friut=friut.dropna(axis=0)

friut.to_excel("output_merge.xlsx", index=True, encoding='utf-8')

#index() 추가 연습

friut=friut.reset_index()

print(friut)

#index() 추가 연습


#OLED 모델 축출 연습
fruit_OLED = fruit.loc[fruit.모델.str.contains("OLED")]


print(fruit_OLED)
#
# fruit_UHD=fruit.drop[fruit_OLED]
#
# print(fruit_UHD)

#OLED 모델 축출 연습

#ok/ng 판정하기
#
# grades = []
#
# for row in fruit['Value']:
#     if float(row) < 1.4:
#         grades.append('ok')
#
#     else:
#         grades.append('ng')
#
# fruit['result'] = grades
#
# print(fruit)

#ok/ng 판정하기
#
# Group by 해보기

fruit_모델 = fruit.groupby('모델')

print(fruit_모델.groups)

# for Stand P/N, group in fruit_모델:
#     print(Stand P/N) + ": " + str(len(group)))
#     print(group)
#     print()

# Group by 해보기


friut_table=pd.pivot_table(friut, index=['모델','Stand P/N','Stand (Type)'], columns='검사 시간', values='Value',aggfunc='first')

print(friut_table)

friut_table.to_excel("output_table.xlsx", index=True, encoding='utf-8')











