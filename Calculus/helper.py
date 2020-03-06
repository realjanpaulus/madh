from IPython.core.display import HTML


def css_styling():
	"""Loads css styles."""
	styles = open("./styles/custom.css", "r").read()
	return HTML(styles)