import pandas as pd
df = pd.read_csv('000608358.csv', encoding="shift-jis")
#print(df.head())
#print(df.tail())
#print(df[['sityouson-name3']])
#print(df.iloc[:, :-1])

#print(df[df['ken-code'] > 30])  #県コードが30以上のものをすべて表示
#print(df.describe()) # 平均、最大値、最小値などの数値をすべて表示