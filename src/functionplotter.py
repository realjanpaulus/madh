from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MaxNLocator


# ==================== #
# functional equations #
# ==================== #

@np.vectorize
def constant_function(c, x):
	return c

# ================ #
# helper functions #
# ================ #

def coordinate_system(ax, neg_dim, pos_dim):

	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.set_xlim([neg_dim,pos_dim])
	ax.set_ylim([neg_dim,pos_dim])
	ax.xaxis.set_major_locator(MaxNLocator(integer=True))
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))


def get_function(function = "constant", space=(-10.0, 10.0), **kwargs):
	if function == "constant" and len(kwargs) > 0:
		x = np.linspace(space[0],space[1],num=100)
		
		y = constant_function(kwargs["v1"], x)
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		coordinate_system(ax, space[0],space[1]) 
		plt.plot(x, y)
		plt.grid()
		plt.show()
		
def get_slider(value_names = ["x", "w"], 
			   space = (-10.0, 10.0), 
			   slider_step = 1.0):
	
	if len(value_names) == 1:
		sliders = [widgets.FloatSlider(value=0, 
									   min=space[0], 
									   max=space[1],
									   step=slider_step,
									   description=f'{value_names[0]}',
									   disabled=False,
									   continuous_update=False,
									   orientation='horizontal',
									   readout=True,
									   readout_format='.1f',) 
				   for i in range(len(value_names))]
	else:
		sliders = [widgets.FloatSlider(value=0, 
									   min=space[0], 
									   max=space[1],
									   step=slider_step,
									   description=f'{value_names[i]}',
									   disabled=False,
									   continuous_update=False,
									   orientation='horizontal',
									   readout=True,
									   readout_format='.1f',) 
				   for i in range(len(value_names))]
		
	return sliders


# ============ #
# plt function #
# ============ #

def plt_function(function = "constant", 
				 space=(-10.0, 10.0), 
				 slider_step = 1.0):
	""" Plot function by function name. """
	available_functions = ["constant"]
	if function == "constant":
		value_names = ["c", "x"]
		sliders = get_slider(value_names, space=space, slider_step=slider_step)
	
	if function in available_functions:
		kwargs = {'v{}'.format(i+1):slider for i, slider in enumerate(sliders)}
		interact(get_function, function=fixed(function), space=fixed(space), **kwargs)
	else:
		print(f"Function '{function}' is not known.")