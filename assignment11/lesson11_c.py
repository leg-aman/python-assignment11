from dash import Dash, dcc, html, Input, Output # Dash components you need
import plotly.express as px # Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
import plotly.data as pldata # This is only needed to give access to the Plotly built in datasets.

df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True) # This loads one of the datasets


# Initialize Dash app
app = Dash(__name__) # This creates the app object, to wich various things are added below. 
# __name__ is the name of the running Python module, which is your main module in this case

# Layout: This section creates the HTML components
app.layout = html.Div([ # This div is for the dropdown you see at the top, and also for the graph itself
    dcc.Dropdown( # This creates the dropdown
        id="stock-dropdown", # and it needs an id
        options=[{"label": symbol, "value": symbol} for symbol in df.columns], # This populates the dropdown with the list of stocks
        value="GOOG" # This is the initial value
    ),
    dcc.Graph(id="stock-price") # And the graph itself has to have an ID
])

# Callback for dynamic updates
@app.callback( # OK, now this is a decorator.  Hmm, we haven't talked about decorators in Python.  This decorator is decorating the update_graph() function.
    # Because of the decorator, the update_graph() will be called when the stock-dropdown changes, passing the value selected in the dropdown.
    Output("stock-price", "figure"),  # And ... you get the graph back
    [Input("stock-dropdown", "value")] # When you pass in the value of the dropdown.
)
def update_graph(symbol): # This function is what actually does the plot, by calling Plotly, in this case a line chart of date (which is the index) vs. the chosen stock price.
    fig = px.line(df, df.index, y=symbol, title=f"{symbol} Price")
    return fig

# Run the app
if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
    app.run(debug=True) # start the Flask web server