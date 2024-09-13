import pandas as pd
import numpy as np

df = pd.DataFrame("shopping.csv")
print(df.head(10))
df = df.dropna()
