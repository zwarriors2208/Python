import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, geom_line, geom_bar
#Create a sample DataFrame using pandas
data= pd.DataFrame({
    'x':pd.Series([1,2,3,4,5,6,7,8,9,10]),
    'y':pd.Series([2,3,5,7,11,13,17,19,23,29]),
    'category': pd.Series(['A','A','A','B','B','B','A','B','A','B'])
})
#Scatter plot
s_p=(ggplot(data,aes(x='x',y='y',color='category'))+ geom_point()+ labs(title='Scatter Plot Example', x='X Axis', y='Y Axis'))
print(s_p)