import plotly.graph_objects as go
import numpy as np
#generate synthetic data
months=['January','February','March','April','May','June','July','August','September', 'October', 'November', 'December']
sales=np.random.randint(50,500,size=12)
line_fig=go.Figure()
line_fig.add_trace(go.Scatter(x=months, y=sales, mode='lines+markers',name='Sales'))
line_fig.update_layout(title='Monthly Sales Data',xaxis_title='Months',yaxis_title='Sales')
line_fig.write_image('line_plot.png')