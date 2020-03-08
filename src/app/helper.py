from glob import glob
from IPython.core.display import HTML
from IPython.display import display, Markdown
from IPython.display import clear_output
import ipywidgets as widgets
import json
from pathlib import Path
import sys
from typing import Dict, List, Optional, Tuple, Union

# grandparent path to ensure correct location of files
path = Path().cwd().parents[1]

def css_styling():
	"""Loads css styles."""
	css_files = dict([(p.name, p) for p in path.rglob("*.css")])
	styles = open(css_files["custom.css"], "r").read()
	return HTML(styles)


