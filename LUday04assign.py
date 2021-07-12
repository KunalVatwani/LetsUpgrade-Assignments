#Q1). What is plotly?
#A1). Plotly is an interactive open source library in python which helps in data representation and visualization. it supports various different types of charts and graphs.

#Q2). Where is plotly used?
#A2). It is used in making bar graphs, line plots, pie charts, scatter plots, etc and simplifies the data analysation process.

#Q3).Make a pie chart of india's car companies market share % value
# import plotly.graph_objects as go
# company = ['Maruti Suzuki', 'Hyundai', 'Tata', 'Kia', 'Mahindra', 'Renault']
# shares = [50,17.4,7,5.8,5.6,3.3]
# fig = go.Figure(data=(go.Pie(labels = company, values = shares)))
# fig.show()

#Q4). plot a bar chart with india's covid 19 active cases
# import plotly.express as px
# states = ['Maharashtra','Kerela','Karnataka','Tamil Nadu','Andhra Pradseh','Uttar Pradesh']
# cases = [119442, 115327, 36760, 32307, 28680, 1594]
# fig = px.bar(x=states, y=cases)
# fig.show()

#Q5). plot a line chart with india's active covid 19 case recovery
import plotly.express as px
months = ['july','August','September','October','November', 'December', 'January', 'February', 'March','April']
recovery = [96.75, 97.73,98.15, 98.38,98.46, 98.50,98.53,98.55,98.59,98.65]
fig = px.line(x=months, y=recovery, title='Recovery rate in India')
fig.show()
