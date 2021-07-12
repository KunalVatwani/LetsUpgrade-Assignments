import plotly.express as px
import plotly.graph_objects as go

# df = px.data.iris()
# fig = px.scatter(df, x='sepal_width', y='sepal_length',color="species")
# fig.show()

# df = px.data.iris()
# fig = px.bar(df, x='sepal_width', y='sepal_length',color="species")
# fig.show()

# df = px.data.gapminder()
# fig = px.scatter(df.query('year==2007'), x='gdpPercap',y='lifeExp',size='pop',color='continent',hover_name='country',log_x=True, size_max=60)
# fig.show()

# df = px.data.gapminder()
# fig = px.line(df.query('year==2007'), x='gdpPercap',y='lifeExp',color='continent',hover_name='country',log_x=True)
# fig.show()

df = px.data.tips()
fig = px.violin(df, y='total_bill',box=True)
fig.show()