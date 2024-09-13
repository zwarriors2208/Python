import pandas as pd
df=pd.read_csv('A.csv')
print(df.head(1))

# #ensure the datatype of dates
print(df.info())
df = pd.to_datetime(df['Date'])
print(df.info())
m = df.isna().sum()
print(m)
Q1 = df['High'].quantile(0.25)
Q3 = df['High'].quantile(0.75)
IQR = Q3 - Q1
lb = Q1- IQR * 1.5
hb = Q3+ IQR * 1.5
print(df[df['High']<hb & df['High']>lb].count())

