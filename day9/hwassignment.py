import pandas as pd
import numpy as np

df = pd.read_csv("retail_sales.csv")

# print(df.head(10))
# c = df.isna().sum()
# print(c, c.describe())
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
print(df["Date"].dtype)
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
print(f"iqr -- {IQR},{Q1},{Q3}")
lb =  Q1- 1.5 * IQR
ub = Q3 + 1.5 * IQR
# print(df[df["Sales"]>ub].count(),"\n", lb)
# print(df[df["Sales"]<lb].count(),"\n", lb)
# df[df["Sales"]<lb | df["Sales"]>ub].dropna()
print
#