import pandas as pd
#
fruit = pd.read_excel('fruit.xlsx',sheet_name='sheet1')

condition_A=(fruit['Spec.']=='전 : 0˚↓, 후 : 1.8˚ ↑(MA)')
fruit=fruit[condition_A]

fruit = fruit[['검사 시간','모델', 'Suffix','라인','W/O','Spec.','Value']]

fruit=fruit.dropna()

print(fruit)

apple = pd.read_excel('apple.xlsx',sheet_name='sheet1')

apple = apple[['모델','Suffix','Stand P/N','Stand (Type)']]

print(apple.head())

friut = pd.merge(fruit, apple, how='left', on=['모델','Suffix'])

print(friut)

friut.to_excel("output_merge.xlsx", index=False, encoding='utf-8')

