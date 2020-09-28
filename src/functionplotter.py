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

def exponential_function(a, x):
	if a == 0:
		a = 1e-10
	return np.power(a, x)

def linear_function(m, b, x):
	return m*x + b

def logarithmic_function(a, x):
	if a == 0:
		a = 1e-10
	return np.log(x) / np.log(a)

def normal_parabola(a, c, d, x):
	return a*((x-d)**2) + c

def power_function(a, n, x):
	return a * np.power(x, n)

def quadratic_function(a, b, c, x):
	return a*(x**2) + b * x + c

def trigonometric_function(sct, x):
	if sct == "Kosinus":
		return np.cos(x)
	elif sct == "Sinus":
		return np.sin(x)
	elif sct == "Tangens":
		return np.tan(x)

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
	""" Computes a function given by name."""

	x = np.linspace(space[0],space[1],num=100)

	if function == "constant" and len(kwargs) > 0:
		y = constant_function(kwargs["v1"], x)
	elif function == "exponential" and len(kwargs) > 0:
		y = exponential_function(kwargs["v1"], x)
	elif function == "linear" and len(kwargs) > 1:
		y = linear_function(kwargs["v1"], kwargs["v2"], x)
	elif function == "logarithmic" and len(kwargs) > 0:
		import warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		y = logarithmic_function(kwargs["v1"], x)
	elif function == "normal_parabola" and len(kwargs) > 2:
		y = normal_parabola(kwargs["v1"], kwargs["v2"], kwargs["v3"], x)
	elif function == "power" and len(kwargs) > 1:
		y = power_function(kwargs["v1"], kwargs["v2"], x)
	elif function == "quadratic" and len(kwargs) > 2:
		y = quadratic_function(kwargs["v1"], kwargs["v2"], kwargs["v3"], x)
	elif function == "trigonometric" and len(kwargs) > 0:
		x = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
		y = trigonometric_function(kwargs["v1"], x)
	

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	coordinate_system(ax, space[0],space[1]) 
	plt.plot(x, y)
	plt.grid()
	plt.show()
		
def get_slider(value_names = ["x", "w"], 
			   space = (-10.0, 10.0), 
			   slider_step = 1.0):
	""" Returns a slider element in a list for 
		every value in value_names.
	"""
	if "cos" in value_names or "sin" in value_names or "tan" in value_names:
		return [widgets.SelectionSlider(value="Kosinus", 
										options=["Kosinus", "Sinus", "Tangens"],
										description=f"{i}",
										disabled=False,
										continuous_update=False,
										orientation='horizontal',
										readout=True,) for i in ["Funktion"]]
	else:	
		return [widgets.FloatSlider(value=0, 
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


# ============ #
# plt function #
# ============ #

def plt_function(function = "constant", 
				 space=(-10.0, 10.0), 
				 slider_step = 1.0):
	""" Plot function by function name. """
	available_functions = ["constant", "exponential", "linear", "logarithmic", 
						   "normal_parabola", "power", "quadratic", "trigonometric"]
	
	if function in available_functions:
		if function == "constant":
			value_names = ["c", "x"]
		elif function == "exponential":
			value_names = ["a"]
		elif function == "linear":
			value_names = ["m", "b"]
		elif function == "logarithmic":
			value_names = ["a"]
		elif function == "normal_parabola":
			value_names = ["a", "c", "d"]
		elif function == "power":
			value_names = ["a", "n"]
		elif function == "quadratic":
			value_names = ["a", "b", "c"]
		elif function == "trigonometric":
			value_names = ["cos", "sin", "tan"]
		
		sliders = get_slider(value_names, space=space, slider_step=slider_step)
		kwargs = {'v{}'.format(i+1):slider for i, slider in enumerate(sliders)}
		interact(get_function, function=fixed(function), space=fixed(space), **kwargs)
	else:
		print(f"Function '{function}' is unknown.")

