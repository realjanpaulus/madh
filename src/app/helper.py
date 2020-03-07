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


# ===================== #
# Quiz helper functions #
# ===================== #


def find_json():
	""" Returns all json-files of the current grandparent
		directory in a dictionary. 
	"""
	return dict([(p.name, p) for p in path.rglob("*.json")])

def load_quiz(quiz_name: str,
			  subject: Optional[str] = "algebra") -> dict:
	""" Loads specific quiz by name from respective json quiz file. """
	json_files = find_json()

	if subject == "algebra":
		with open(json_files["algebra_quiz.json"], "r") as json_file:
			dic = json.load(json_file)
	elif subject == "calculus":
		with open(json_files["calculus_quiz.json"], 'r') as f:
			dic = json.load(f)
	try:
		return dic[quiz_name]
	except KeyError:
		return {"description": "ACHTUNG: Quiz konnte nicht geladen werden.",
				"options": {"a": "",
							"b": "",
							"c": "",
							"d": ""},
				"correct_answer": "d"}



def create_quiz(quiz_name: str,
				subject: Optional[str] = "algebra"):
	""" Creates a quiz by quiz_name and subject."""

	quiz = load_quiz(quiz_name, subject)
	
	description = quiz["description"]
	options = list(quiz["options"].keys())
	options_description = quiz["options"] # Options + its descriptions
	correct_answer = quiz["correct_answer"]

	if correct_answer not in options:
		options.append(correct_answer)

	correct_answer_index = options.index(correct_answer)

	# build clickable radio buttons
	
	options_numbers = [(element, i) for i, element in enumerate(options)]
	# radio_options: ("Option1", 0), ("Option2", 1), ... #
	radio_options = widgets.RadioButtons(options = options_numbers,
										 description = '',
										 disabled = False)

	# numbered_answers: {0: "answer1", 1: "answer2", ...}
	numbered_answers = {v: k for k, v in dict(radio_options.options).items()}

	# show description
	description_out = widgets.Output()
	with description_out:
		display(Markdown(description))

	d = {}

	def check_selection(foo):
		selected_option = int(radio_options.value)
		if selected_option == correct_answer_index:
			s = "<span style='font-weight: bold; color: #28a428; background-color: #ffffff;'>Richtig.</span>"
		else:
			s = "<span style='font-weight: bold; color: #d23838; background-color: #ffffff;'>Falsch.</span>"
		s = s + " " + options_description[numbered_answers[selected_option]]
	
		with feedback_out:
			clear_output()
			#display(Markdown(s))
			d[quiz_name] = (selected_option, s)
			print(d)

	feedback_out = widgets.Output()
	check = widgets.Button(description="Abschicken")
	
	check.on_click(check_selection)
	
	return widgets.VBox([description_out, radio_options, check, feedback_out])


#TODO
def collect_quizzes():
	return [create_quiz("cquiz_1_1", "calculus"), 
			create_quiz("cquiz_1_1", "calculus")]

