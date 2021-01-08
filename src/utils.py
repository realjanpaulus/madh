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



def hide_code():
	"""Hide jupyter notebook code cells."""
	toggle_code_str = """
	<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show/Hide Code Cell"></form>
	"""

	toggle_code_prepare_str = """
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide();
        } else {
            $('div.cell.code_cell.rendered.selected div.input').show();
        }
    }
    </script>"""
	display(HTML(toggle_code_prepare_str + toggle_code_str))



def to_int(n):
	""" Checks if float is integer and converts it if necessary."""
	if n.is_integer():
		n = int(n)
	return n


