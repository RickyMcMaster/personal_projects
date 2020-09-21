# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='Fertility (children per woman)', y_axis_label='Female Literacy (% population)', tools='pan, zoom_in, zoom_out')

p.circle([1,5,8,3,6,9,8,2,9,2],
         [5,4,6,5,4,6,5,4,6,4])

output_file('dummy_scatter.html')

show(p)