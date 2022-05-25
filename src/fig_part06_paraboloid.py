import numpy as np
import plotly.graph_objects as go

# generate grid
r = np.linspace(0, 5, 101)
phi = np.linspace(0, 2*np.pi, 101)
grid_r, grid_phi = np.meshgrid(r, phi) 
x = grid_r * np.cos(grid_phi)
y = grid_r * np.sin(grid_phi)

# evaluate function
z = 0.5 * (x**2 + y**2) 

# plot
fig = go.Figure()
fig.add_trace(go.Surface(z=z, x=x, y=y, colorscale='viridis'))
fig.update_layout(title='Paraboloid f(x,y)=x^2 + y^2', 
xaxis_title='x-Achse', yaxis_title='y-Achse')

fig.write_html('fig_part06_paraboloid.html')
