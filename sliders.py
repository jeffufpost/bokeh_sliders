''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

# Set up data
# population
p = 500000 #population of canton geneva for example p = S+E+I+R

# number of days
t = 300

# Initialize data
sus = np.zeros(t, dtype=int)
exp = np.zeros(t, dtype=int)
inf = np.zeros(t, dtype=int)
ded = np.zeros(t, dtype=int)
rec = np.zeros(t, dtype=int)

# State of population
sus[0] = p - 100
exp[0] = 100
inf[0] = 0
rec[0] = 0
ded[0] = 0

# state of epidemic
beta = 4             # 1/Time between contacts = number of contacts per day = 10?
#mu = 0.01           # death rate due to disease (or CFR)
#mut = 0.0714        # time to death due to disease = 1/14 days
gamma = 0.0378       # 1/average time to recover from symptom onset = 1/14 days
sigma = 0.052

# time delays
m = 5  # 5 days of incubation
n = 14 # 14 days from onset of symptoms to recovery (or death)

def infection(S, E, I, R, p, i):
    for t in range (1, i):
        sus[t], exp[t], inf[t], rec[t] = sus[t-1] - (beta * sus[t-1] * inf[t-1])/p, exp[t-1] + (beta * sus[t-1] * inf[t-1])/p - sigma * exp[t-1-m], inf[t-1] + sigma * exp[t-1-m] - gamma * inf[t-1-n], rec[t-1] + gamma * inf[t-1-n]

infection(sus, exp, inf, rec, p, t)

# Set up plot
plot = figure()

x = range(len(sus))

plot.line(x, sus)


# Set up widgets
# text = TextInput(title="title", value='my sine wave')
# offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
# amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
# phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
# freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)
#

# Set up callbacks
# def update_title(attrname, old, new):
#     plot.title.text = text.value
#
# text.on_change('value', update_title)
#
# def update_data(attrname, old, new):

    # Get the current slider values
    # a = amplitude.value
    # b = offset.value
    # w = phase.value
    # k = freq.value
    #
    # Generate the new curve
#     x = np.linspace(0, 4*np.pi, N)
#     y = a*np.sin(k*x + w) + b
#
#     source.data = dict(x=x, y=y)
#
# for w in [offset, amplitude, phase, freq]:
#     w.on_change('value', update_data)
#

# Set up layouts and add to document
# inputs = column(text, offset, amplitude, phase, freq)
#
 curdoc().add_root(row(inputs, plot, width=800))
 curdoc().title = "Sliders"
