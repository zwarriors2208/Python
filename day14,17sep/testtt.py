import pandas as pd

t = input('path:')
df = pd.read_csv(t)
x = df.describe()
print(x)