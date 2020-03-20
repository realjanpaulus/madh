from glob import glob
from IPython.core.display import HTML
from IPython.display import clear_output, display, Markdown
import ipywidgets as widgets
import json
from pathlib import Path
import sys
from typing import Dict, List, Optional, Tuple, Union

# grandparent path to ensure correct location of files
path = Path().cwd().parents[1]


# == Table of contents == #
# - Quiz helper functions #
# - Quiz functions        #
# ======================= #


# ===================== #
# Quiz helper functions #
# ===================== #

def formatNumber(num):
  """ Removes .0 from a float."""
  if num % 1 == 0:
    return int(num)
  else:
    return num

def clear_json(subject: str):
	""" Clears the tmp answers json file. """
	json_files = find_json()

	try:
		jsonFile = open(json_files[f"tmp_{subject}_answers.json"], mode="r")
		jdata = json.load(jsonFile)
		jsonFile.close()
		jsonFile = open(json_files[f"tmp_{subject}_answers.json"], mode="w+")
		json.dump({}, jsonFile)
		jsonFile.close()
	except KeyError:
		print(f"Thema '{subject}' ist unbekannt.")


def find_json() -> dict:
	""" Returns all json-files of the current grandparent
		directory in a dictionary. 
	"""
	return dict([(p.name, p) for p in path.rglob("*.json")])

def load_tmp(subject: Optional[str] = "algebra"):
	""" Loads tmp user json dictionary. """
	json_files = find_json()

	try:
		with open(json_files[f"tmp_{subject}_answers.json"]) as f:
			dic = json.load(f)
			return dic
	except KeyError:
		print(f"Thema '{subject}' ist unbekannt.")
	


def load_quiz(quiz_name: str,
			  quiz_number: int,
			  subject: Optional[str] = "algebra") -> dict:
	""" Loads specific quiz by name and number 
		from respective json quiz file. 
	"""
	json_files = find_json()
	try:
		filename = f"{subject}_quiz{quiz_number}.json"
		with open(json_files[filename], 'r') as f:
			dic = json.load(f)
			try:
				return dic[quiz_name]
			except KeyError:
				print(f"Quiz-Name '{quiz_name}' existiert nicht.")
	except:
		print(f"Thema '{subject}' oder Quiz-Nummer '{quiz_number}' konnten nicht geladen werden.")
	

def write_tmp(answer: str,
			  quiz_number: int,
			  description: str,
			  question: str,
			  subject: Optional[str] = "algebra"):
	""" Adds new entry to a tmp user json dictionary. """

	json_files = find_json()

	try:
		new_entry = {quiz_number : {"answer": answer,
									"description": description,
									"question": question}}
		with open(json_files[f"tmp_{subject}_answers.json"]) as f:
			dic = json.load(f)

		dic.update(new_entry)

		with open(json_files[f"tmp_{subject}_answers.json"], mode="w") as f:
			json.dump(dic, f)
	except KeyError:
		print(f"Thema '{subject}' ist unbekannt.")


# ============== #
# Quiz functions #
# ============== #


def create_quiz(quiz_name: str,
				subject: Optional[str] = "algebra",
				standalone: Optional[bool] = False,
				quiz_dic: Optional[dict] = {}):
	""" Creates a quiz by name and subject."""

	if quiz_dic:
		description = quiz_dic["description"]
		options = list(quiz_dic["options"].keys())
		options_description = quiz_dic["options"] # Options + its descriptions
		correct_answer = quiz_dic["correct_answer"]
	else: # for standalone quiz loading
		quiz = load_quiz(quiz_name, subject)
		description = quiz["description"]
		options = list(quiz["options"].keys())
		options_description = quiz["options"] # Options + its descriptions
		correct_answer = quiz["correct_answer"]
		

	if correct_answer not in options:
		options.append(correct_answer)

	correct_answer_index = options.index(correct_answer)

	## build clickable radio buttons 
	options_numbers = [(element, i) for i, element in enumerate(options)]
	# radio_options: ("Option1", 0), ("Option2", 1), ... #
	radio_options = widgets.RadioButtons(options = options_numbers,
										 description = '',
										 disabled = False)

	# numbered_answers: {0: "answer1", 1: "answer2", ...}
	numbered_answers = {v: k for k, v in dict(radio_options.options).items()}

	## show description
	description_out = widgets.Output()
	quiz_number = quiz_name.split('_')[-1]
	with description_out:
		display(Markdown(f"---\n{quiz_number}) " + description))

	button_style = "bold"

	def check_selection(b):
		selected_option = int(radio_options.value)
		if selected_option == correct_answer_index:
			s = "<span style='font-weight: bold; color: #28a428; background-color: #ffffff;'>Richtig.</span>"
		else:
			s = "<span style='font-weight: bold; color: #d23838; background-color: #ffffff;'>Falsch.</span>"
		s = s + " " + options_description[numbered_answers[selected_option]]
	
		with feedback_out:
			clear_output()
			check.style.button_color = "#d9d9d9"
			if quiz_dic:
				write_tmp(s, int(quiz_number), description, numbered_answers[selected_option], subject)
			else:
				display(Markdown(s))

	feedback_out = widgets.Output()

	check = widgets.Button(description="Abschicken")
	check.style.button_color = "#a6a6a6"
	
	check.on_click(check_selection)
	
	return widgets.VBox([description_out, radio_options, check, feedback_out])



# TODO
def start_quiz(quiz_number: int,
			   subject: Optional[str] = "algebra"):
	""" Collects and displays all quizzes by 
		a number and subject. 
	"""

	json_files = find_json()

	if subject == "algebra":
		filename = f"algebra_quiz{quiz_number}.json"
	elif subject == "calculus":
		filename = f"calculus_quiz{quiz_number}.json"
	clear_json(subject)
	with open(json_files[filename], 'r') as f:
		quizzes_dic = json.load(f)

	question_count = 0

	for k, v in quizzes_dic.items():
		display(create_quiz(k, subject=subject, quiz_dic=v))
		question_count += 1

	
	start = widgets.Button(description="Ausgewählte Antworten überprüfen", 
						   layout=widgets.Layout(width="40%"))
	output = widgets.Output()
	

	def show_answers(b):
		with output:
			clear_output()
			start.style.button_color = "#e7e7e7"
			answers = load_tmp(subject)
			right_answers = 0

			for k, v in answers.items():
				display(Markdown(f"{k}) {v['description']}"))
				display(Markdown(f"Ausgewählte Antwort: <span style='font-weight: bold'>{v['question']}</span> ")) 
				display(Markdown(f"{v['answer']}"))
				if "Richtig." in v["answer"]:
					right_answers += 1

			if len(answers) < question_count:
				if (question_count - len(answers)) == 1:
					display(Markdown("---\n" + "---\n" + f"<span style='font-weight: bold'>{right_answers}</span> von <span style='font-weight: bold'>{len(answers)}</span> beantworteten Fragen waren richtig. Sie haben <span style='font-weight: bold'>{question_count - len(answers)}</span> Frage nicht beantwortet."))
				else:
					display(Markdown("---\n" + "---\n" + f"<span style='font-weight: bold'>{right_answers}</span> von <span style='font-weight: bold'>{len(answers)}</span> beantworteten Fragen waren richtig. Sie haben <span style='font-weight: bold'>{question_count - len(answers)}</span> Fragen nicht beantwortet."))
			else:
				display(Markdown("---\n" + "---\n" + f"<span style='font-weight: bold'>{right_answers}</span> von <span style='font-weight: bold'>{len(answers)}</span> beantworteten Fragen waren richtig."))

			if right_answers == len(answers):
				display(Markdown("Glückwunsch! Sie haben alle beantworteten Fragen richtig beantwortet."))
			elif right_answers == 0:
				display(Markdown(f"Sie haben keine der beantworteten Fragen richtig beantwortet. Es wird empfohlen, die Aufgaben zu wiederholen und ggbf. das Kapitel noch einmal durchzuarbeiten."))
			elif right_answers/len(answers) < 0.75:
				display(Markdown(f"Sie haben nur {formatNumber((right_answers/len(answers))*100)}% der beantworteten Fragen richtig beantwortet. Es wird empfohlen, die Aufgaben zu wiederholen."))
			elif right_answers/len(answers) >= 0.75:
				display(Markdown(f"Sie haben {formatNumber((right_answers/len(answers))*100)}% der beantworteten Fragen richtig beantwortet. Sie können gerne fortfahren oder aber versuchen, alle Fragen richtig zu beantworten."))


	
	start.on_click(show_answers)
	start.style.button_color = "#b3b3b3"
	display(Markdown("---\n---\n"))
	display(widgets.VBox([start, output]))


