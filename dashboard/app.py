import dash
import dash_bootstrap_components as dbc




app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions']=True
app.config.suppress_callback_exceptions=True
app.suppress_callback_exceptions=True
#server = app.server

