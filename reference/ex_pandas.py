# import pandas as pd
#
# df = pd.read_excel('fruit.xlsx',sheet_name='sheet1')
#
# print(df)

###위에 처럼해도 되고 아래 display를 사용해도 됩니다.###

import pandas as pd

from IPython.display import display, HTML

#엑셀 파일 불러오기
df = pd.read_excel('fruit.xlsx', sheet_name='sheet1')

condition_A=(df['Spec.']=='전 : 0˚↓, 후 : 1.8˚ ↑(MA)')
df=df[condition_A]

df = df[['검사 시간','모델', 'Suffix','라인','W/O','Spec.','Value']]

new_df=df.dropna()

display(new_df)

new_df.to_excel("output.xlsx", index=False, encoding='utf-8')