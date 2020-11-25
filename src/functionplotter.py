from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MaxNLocator
from scipy.misc import derivative

#todo
from sympy import *
import sympy as sym

import typing
from typing import Optional
import warnings

# ==================== #
# functional equations #
# ==================== #

@np.vectorize
def constant_function(c, x):
	return c

def exponential_function(a, x):
	return np.power(a, x)

def linear_function(m, b, x):
	return m*x + b

def logarithmic_function(a, x):
	return np.log(x) / np.log(a)

def normal_parabola(a, c, d, x):
	return a*((x-d)**2) + c

def power_function(a, n, x):
	return a * np.power(x, n)

# todo: passt das?
def quadratic_function(x, a=1, b=2, c=3):
	return a*(x**2) + (b * x) + c

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


def get_function(name = "constant", space=(-10.0, 10.0), d1=False, **kwargs):
	""" Computes a function given by name."""
	
	x = np.linspace(space[0],space[1],num=100)

	if name == "constant" and len(kwargs) > 0:
		y = constant_function(kwargs["v1"], x)
		if d1: y1 = constant_function(0, x)
	elif name == "exponential" and len(kwargs) > 0:
		# ignoring zero value warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		y = exponential_function(kwargs["v1"], x)
	elif name == "linear" and len(kwargs) > 1:
		y = linear_function(kwargs["v1"], kwargs["v2"], x)
		if d1: y1 = constant_function(kwargs["v1"], x)
	elif name == "logarithmic" and len(kwargs) > 0:
		# ignoring zero value warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		x = np.linspace(space[0],space[1],num=10000)
		y = logarithmic_function(kwargs["v1"], x)
	elif name == "normal_parabola" and len(kwargs) > 2:
		y = normal_parabola(kwargs["v1"], kwargs["v2"], kwargs["v3"], x)
	elif name == "power" and len(kwargs) > 1:
		y = power_function(kwargs["v1"], kwargs["v2"], x)
	elif name == "quadratic":

		#todo 	and len(kwargs) > 2:
		#TODO: fixing derivative
		#TODO: extra slider?
		#TODO: fixed quadratic function?
		
		if d1:
			

			#y = quadratic_function(x, 1, 2, 3)
			y = quadratic_function(x, kwargs["v1"], kwargs["v2"], kwargs["v3"])
			#y1 = derivative(y, x, dx=1e-06)
			y1 = np.gradient(y, x)

			"""todo
			t = Symbol('x') 
			y = kwargs["v1"]*(x**2) + (kwargs["v2"] * x) + kwargs["v3"]
			y1 = sym.diff(y, x)
			print(y1)
			"""

		else:
			#todo: geändert reihenfolge
			y = quadratic_function(x, kwargs["v1"], kwargs["v2"], kwargs["v3"])



	elif name == "trigonometric" and len(kwargs) > 0:
		x = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
		y = trigonometric_function(kwargs["v1"], x)
	
	if d1:
		fig = plt.figure()
		ax = fig.subplots()
		coordinate_system(ax, space[0],space[1]) 
		ax.plot(x, y, x, y1)

		plt.grid()
		plt.show()
	
	else:
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		coordinate_system(ax, space[0],space[1]) 
		plt.plot(x, y)

		plt.grid()
		plt.show()

		
def get_slider(value_names: Optional[list] = ["x", "w"], 
			   space: Optional[tuple] = (-10.0, 10.0), 
			   slider_step: Optional[float] = 1.0,
			   startvalue: Optional[int] = 0) -> list:
	""" Returns a slider element in a list for every value in value_names.

	Args:
		value_names: list of function parameter names.
		space: starting and stopping value for np.linspace, stored in a tuple.
		slider_step: value for slider steps.
		startvalue: starting value for the slider steps.
	Returns:
		list of slider elements.
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
		return [widgets.FloatSlider(value=startvalue, 
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


# =================== #
# (main) plt function #
# =================== #

def plt_function(name: Optional[str] = "constant", 
				 space: Optional[tuple] = (-10.0, 10.0), 
				 slider_step: Optional[float] = 1.0,
				 startvalue: Optional[float] = 0,
				 d1: Optional[bool] = False) -> None:
	""" Plot function by function name. 

	Args:
		name: name of the function.
		space: starting and stopping value for np.linspace, stored in a tuple.
		slider_step: value for slider steps.
		startvalue: starting value for the slider steps.
		d1: True for plotting the first derivative.
	Returns:
		None
	"""
	available_functions = ["constant", "c", "con",
						   "exponential", "e", "exp", 
						   "linear", "li", "lin",
						   "logarithmic", "lo", "log",
						   "normal_parabola", "np", "norm_par", "parab", "parabola",
						   "power", "p", "pow",
						   "quadratic", "q", "quad",
						   "trigonometric", "t", "tri", "trig"]
	
	if name in available_functions:
		# constant
		if name in ["constant", "c", "con"]:
			name = "constant"
			value_names = ["c", "x"]

		# exponential
		elif name in ["exponential", "e", "exp"]:
			name = "exponential"
			value_names = ["a"]

		# linear
		elif name in ["linear", "li", "lin"]:
			name = "linear"
			value_names = ["m", "b"]

		# logarithmic
		elif name in ["logarithmic", "lo", "log"]:
			name = "logarithmic"
			value_names = ["a"]

		# normal parabola
		elif name in ["normal_parabola", "np", "norm_par", "parab", "parabola"]:
			name = "normal_parabola"
			value_names = ["a", "c", "d"]

		# power
		elif name in ["power", "p", "pow"]:
			name = "power"
			value_names = ["a", "n"]

		# quadratic
		elif name in ["quadratic", "q", "quad"]:
			name = "quadratic"
			value_names = ["a", "b", "c"]
			
			#todo
			#if d1: value_names = []


		# trigonometric
		elif name in ["trigonometric", "t", "tri", "trig"]:
			name = "trigonometric"
			value_names = ["cos", "sin", "tan"]
		
		sliders = get_slider(value_names, 
							 space=space, 
							 slider_step=slider_step, 
							 startvalue=startvalue)
		kwargs = {'v{}'.format(i+1):slider for i, slider in enumerate(sliders)}
		interact(get_function, 
				 name=fixed(name), 
				 space=fixed(space), 
				 d1=fixed(d1), 
				 **kwargs)
	else:
		print(f"Function '{name}' is unknown.")








