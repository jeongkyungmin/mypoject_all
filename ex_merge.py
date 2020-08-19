import pandas as pd
#
fruit = pd.read_excel('fruit.xlsx',sheet_name='sheet1')

print(fruit.head())

apple = pd.read_excel('apple.xlsx',sheet_name='sheet1')

apple = apple[['모델','Suffix','Stand P/N','Stand (Type)']]

print(apple.head())

friut = pd.merge(fruit, apple, how='left', on=['모델','Suffix'])

print(friut)

friut.to_excel("output_merge.xlsx", index=False, encoding='utf-8')

