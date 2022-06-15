from statistics import mode
from dash import Dash, dcc, html, Input, Output
import numpy as np
import plotly.graph_objects as go
from pyparsing import line

app = Dash(__name__)

# STATE



# GUI
app.layout = html.Div([
    html.H1('Biegelinie'),
    html.Div([
        html.Div('konstante Streckenlast q:' ),
        dcc.Input(id='editfield_q', value='0', type='number'),
    ]),
    dcc.Graph(id='plot_beamequation')

])

# CALLBACKS
@app.callback(
    Output('plot_beamequation', 'figure'),
    Input('editfield_q', 'value'))
def update_figure(q):
    fig = go.Figure()        
    if q != None:
        x,y =  compute_beam(q)
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))

    return fig

# BACKEND
def compute_beam(q):
    q = float(q)
    l = 1.0
    EI = 1.0
    x = np.linspace(0, l)
    y = q/(24*EI)*(x**4 -2 * l * x**3 + l**3 * x)
    return x,y

if __name__ == '__main__':
    app.run_server(debug=True)