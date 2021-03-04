from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import axes3d
from scipy.misc import derivative

import typing
from typing import Optional
from utils import to_int
import warnings

# ==================== #
# functional equations #
# ==================== #


def broken_rational_function(a, b, n, m, a0, b0, x):
	return ((a * np.power(x, n))+a0)/((b * np.power(x, m))+b0)

@np.vectorize
def constant_function(c, x):
	return c

def exponential_function(a, x):
	return np.power(a, x)

def irrational_function(n, a, x):
	if n == 0:
		n = n + 0.0001
	return a*x**(1/float(n))

def linear_function(m, b, x):
	return m*x + b

def logarithmic_function(a, x):
	return np.log(x) / np.log(a)


def multivariate_function1(x, y):
	return x*y

def multivariate_function2(x, y):
	part1 = 3*((1-x)**2)
	part2 = np.exp(-(x**2)-((y+1)**2))
	part3 = 10*((x/5) -(x**3) -(y**5))
	part4 = np.exp(-(x**2)-(y**2))
	part5 = np.exp(-(x+1)**2-(y**2))
	return (part1 * part2) - (part3 * part4) - ((1/3) * part5)

def normal_parabola(a, c, d, x):
	return a*((x-d)**2) + c

def power_function(a, n, x):
	return a * np.power(x, n)

def quadratic_function(a, b, c, x):
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
	"""Plots an cartesian coordinate system."""

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


def get_3D_function(name = "multivariate1", space=(-10.0, 10.0), contour_plot=False):
	""" Computes a 3D function given by name."""

	x = np.linspace(space[0],space[1],num=100)
	y = np.linspace(space[0],space[1],num=100)
	label = "Funktion"

	X, Y = np.meshgrid(x, y)

	if name == "multivariate1":
		zs = np.array([multivariate_function1(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
		Z = zs.reshape(X.shape)
		label = "$f(x,y) = x \\cdot y$"
	elif name == "multivariate2":
		zs = np.array([multivariate_function2(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
		Z = zs.reshape(X.shape)
		label = "$f(x,y) = 3(1-x)^{2} \\cdot e^{(-x^{2} - (y+1)^{2})} -10(\\frac{x}{5}-x^{3}-y^{5}) \\cdot e^{(-x^{2}-y^{2})}-\\frac{1}{3}\\cdot e^{-(x+1)^{2}-y^{2}}$"
	

	if contour_plot == True:
		X, Y = np.meshgrid(x, y)
		Z = multivariate_function2(X,Y)
		fig, ax = plt.subplots(dpi=100)
		plt.contour(X, Y, Z, 15, colors="black", linewidths=0.5)
		plt.contourf(X, Y, Z, 15, cmap="viridis")
		plt.colorbar()
		plt.title(label)
		plt.show()
	else:
		fig = plt.figure(dpi=100)
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_surface(X, Y, Z, cmap="viridis")

		ax.set_xlabel('x-Achse')
		ax.set_ylabel('y-Achse')
		ax.set_zlabel('z-Achse')

		plt.title(label)
		plt.grid()
		plt.show()


def get_function(name = "constant", space=(-10.0, 10.0), d1=False, d2=False, d3=False, **kwargs):
	""" Computes a function given by name."""
	
	x = np.linspace(space[0],space[1],num=100)
	label = "Funktion"
	
	if name == "broken_rational" and len(kwargs) > 5:
		# ignoring zero value warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		x = np.linspace(space[0],space[1],num=1000)

		a = to_int(kwargs["v1"])
		b = to_int(kwargs["v2"])
		n = to_int(kwargs["v3"])
		m = to_int(kwargs["v4"])
		a0 = to_int(kwargs["v5"])
		b0 = to_int(kwargs["v6"])

		if a == 0:
			counter = f'{{{a0}}}'
		elif a == 1:
			if a0 < 0:
				counter = f'x^{{{n}}} - {{{abs(a0)}}}'
			else:
				counter = f'x^{{{n}}} + {{{a0}}}'
		else:
			if a0 < 0:
				counter = f'{{{a}}} \\cdot x^{{{n}}} - {{{abs(a0)}}}'
			else:
				counter = f'{{{a}}} \\cdot x^{{{n}}} + {{{a0}}}'

		if b == 0:
			denominator = f'{{{b0}}}'
		elif b == 1:
			if b0 < 0:
				denominator = f'x^{{{m}}} - {{{abs(b0)}}}'
			else:
				denominator = f'x^{{{m}}} + {{{b0}}}'
		else:
			if b0 < 0:
				denominator = f'{{{b}}} \\cdot x^{{{m}}} - {{{abs(b0)}}}'
			else:
				denominator = f'{{{b}}} \\cdot x^{{{m}}} + {{{b0}}}'

		label = f'$f(x) = \\dfrac{{{counter}}}{{{denominator}}}$'
		y = broken_rational_function(a, b, n, m, a0, b0, x)

		# See: https://stackoverflow.com/questions/36870842/
		# 	   graphing-any-rational-functions-in-python-considering-the-asymptotes
		utol = 50.
		ltol = -50.
		y[y>utol] = np.nan
		y[y<ltol] = -np.nan
	elif name == "constant" and len(kwargs) > 0:
		c = to_int(kwargs["v1"])
		label = f'$f(x) = {{{c}}}$'
		y = constant_function(c, x)
	elif name == "exponential" and len(kwargs) > 0:
		# ignoring zero value warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		a = to_int(kwargs["v1"])
		label = f'${{{a}}}^x$'
		y = exponential_function(a, x)
	elif name == "irrational" and len(kwargs) > 1:
		# ignoring zero value warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		x = np.linspace(space[0],space[1],num=10000)
		n = to_int(kwargs["v1"])
		a = to_int(kwargs["v2"])
		label = f'$\\sqrt[{n}]{{{{{a}}} \\cdot x}}$'
		y = irrational_function(n, a, x)

		# See: https://stackoverflow.com/questions/36870842/
		# 	   graphing-any-rational-functions-in-python-considering-the-asymptotes
		utol = 50.
		ltol = -50.
		y[y>utol] = np.nan
		y[y<ltol] = -np.nan
	elif name == "linear" and len(kwargs) > 1:
		m = to_int(kwargs["v1"])
		b = to_int(kwargs["v2"])
		label = f'$f(x) = {{{m}}}x + {{{b}}}$'
		y = linear_function(m, b, x)
	elif name == "logarithmic" and len(kwargs) > 0:
		# ignoring zero value warnings
		warnings.filterwarnings("ignore", category=RuntimeWarning) 
		x = np.linspace(space[0],space[1],num=10000)
		a = to_int(kwargs["v1"])
		label = f'$f(x) = \\log_{{{a}}} \\: x$'
		y = logarithmic_function(a, x)
	elif name == "normal_parabola" and len(kwargs) > 2:
		a = to_int(kwargs["v1"])
		c = to_int(kwargs["v2"])
		d = to_int(kwargs["v3"])
		label = f'$f(x) = {{{a}}} + ((x-{{{d}}})^2) + {{{c}}}$'
		y = normal_parabola(a, c, d, x)
	elif name == "power" and len(kwargs) > 1:
		x = np.linspace(space[0],space[1],num=1000)
		a = to_int(kwargs["v1"])
		n = to_int(kwargs["v2"])
		label = f'$f(x) = {{{a}}} \\cdot x^{{{n}}}$'
		y = power_function(a, n, x)

		# See: https://stackoverflow.com/questions/36870842/
		# 	   graphing-any-rational-functions-in-python-considering-the-asymptotes
		utol = 50.
		ltol = -50.
		y[y>utol] = np.nan
		y[y<ltol] = -np.nan
	elif name == "quadratic":
		a = to_int(kwargs["v1"])
		b = to_int(kwargs["v2"])
		c = to_int(kwargs["v3"])
		label = f'$f(x) = {{{a}}}x^2 + {{{b}}}x + {{{c}}}$'
		y = quadratic_function(a, b, c, x)
	elif name == "trigonometric" and len(kwargs) > 0:
		x = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
		mapping = {"Kosinus": "\\cos", "Sinus": "\\sin", "Tangens": "\\tan"}
		sct = kwargs["v1"]
		label = f'${{{mapping[sct]}}} \\: x$'
		y = trigonometric_function(sct, x)


	### plotting ###

	fig = plt.figure(dpi=100)
	ax = fig.subplots()
	coordinate_system(ax, space[0],space[1]) 
	ax.plot(x, y, label=label)

	if d1:
		# first derivative
		y1 = np.gradient(y, x)
		if name == "trigonometric" and sct == "Tangens":
			# See: https://stackoverflow.com/questions/36870842/
			# 	   graphing-any-rational-functions-in-python-considering-the-asymptotes
			utol = 50.
			ltol = -50.
			y1[y1>utol] = np.nan
			y1[y1<ltol] = -np.nan

		ax.plot(x, y1, label="Erste Ableitung")
		
	if d2:
		# first derivative
		y1 = np.gradient(y, x)
		# second derivative
		y2 = np.gradient(y1, x)
		if name == "trigonometric" and sct == "Tangens":
			# See: https://stackoverflow.com/questions/36870842/
			# 	   graphing-any-rational-functions-in-python-considering-the-asymptotes
			utol = 50.
			ltol = -50.
			y2[y2>utol] = np.nan
			y2[y2<ltol] = -np.nan

		ax.plot(x, y2, label="Zweite Ableitung")

	if d3:
		# first derivative
		y1 = np.gradient(y, x)
		# second derivative
		y2 = np.gradient(y1, x)
		# third derivative
		y3 = np.gradient(y2, x)
		if name == "trigonometric" and sct == "Tangens":
			# See: https://stackoverflow.com/questions/36870842/
			# 	   graphing-any-rational-functions-in-python-considering-the-asymptotes
			utol = 50.
			ltol = -50.
			y3[y3>utol] = np.nan
			y3[y3<ltol] = -np.nan

		ax.plot(x, y3, label="Dritte Ableitung")
		
	plt.legend(fancybox=True, framealpha=1.)
	plt.grid()
	plt.show()

		
def get_slider(value_names: Optional[list] = ["x", "w"], space: Optional[tuple] = (-10.0, 10.0), slider_step: Optional[float] = 1.0, startvalue: Optional[int] = 0) -> list:
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
										readout=True,) 
				for i in ["Funktion"]]
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
	d1: Optional[bool] = False, 
	d2: Optional[bool] = False, 
	d3: Optional[bool] = False,
	use_3D: Optional[bool] = False,
	contour_plot: Optional[bool] = False) -> None:
	""" Plot function by function name. 

	Args:
		name: name of the function.
		space: starting and stopping value for np.linspace, stored in a tuple.
		slider_step: value for slider steps.
		startvalue: starting value for the slider steps.
		d1: True for plotting the first derivative.
		d2: True for plotting the second derivative.
		d3: True for plotting the third derivative.
		use_3D: True for plotting 3D plots.
		contour_plot: True for plotting a contour plot. 'use_3D' must also be True.
	Returns:
		None
	"""
	available_functions = ["broken_rational", "broken", "br", "br",
						   "constant", "c", "con",
						   "exponential", "e", "exp", 
						   "irrational", "i", "root", "r",
						   "linear", "li", "lin",
						   "logarithmic", "lo", "log",
						   "normal_parabola", "np", "norm_par", "parab", "parabola",
						   "power", "p", "pow",
						   "quadratic", "q", "quad",
						   "trigonometric", "t", "tri", "trig"]

	available_3D_functions = ["multivariate1", "multi1", "multivariate2", "multi2"]
	
	if name in available_functions:

		# broken rational
		if name in ["broken_rational", "broken", "br", "br"]:
			name = "broken_rational"
			value_names = ["a", "b", "n", "m", "a0", "b0"]

		# constant
		if name in ["constant", "c", "con"]:
			name = "constant"
			value_names = ["c", "x"]

		# exponential
		elif name in ["exponential", "e", "exp"]:
			name = "exponential"
			value_names = ["a"]

		# irrational / root
		elif name in ["irrational", "i", "root", "r"]:
			name = "irrational"
			value_names = ["n", "a"]

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
				 d2=fixed(d2), 
				 d3=fixed(d3), 
				 **kwargs)
	
	elif name in available_3D_functions:
		get_3D_function(name = name, space=space, contour_plot=contour_plot)
	else:
		print(f"Function '{name}' is unknown.")








