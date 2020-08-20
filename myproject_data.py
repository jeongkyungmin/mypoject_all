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

friut.to_excel("output_merge.xlsx", index=True, encoding='utf-8')

friut_table=pd.pivot_table(friut, index=['모델','Stand P/N','Stand (Type)'], columns='검사 시간', values='Value',aggfunc='first')

print(friut_table)

friut_table.to_excel("output_table.xlsx", index=True, encoding='utf-8')







