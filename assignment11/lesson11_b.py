import plotly.express as px
import plotly.data as pldata


df = pldata.iris(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
fig = px.scatter(df, x='sepal_length', y='petal_length', color='species',
                 title="Iris Data, Sepal vs. Petal Length", hover_data=["petal_length"])
fig.write_html("iris.html", auto_open=True)

# Do not try fig.show()!  This sometimes works, but usually it just hangs.