# Anleitung zur Benutzung der Tutorialreihe

Hier wird eine Einführung zur Benutzung der **Calculus**-Tutorialreihe gegeben, welches die Verwendung der Kapitel erleichtern sollte. Diese Informationen hier sind identisch mit dem Notebook `Kapitel 0 - Anleitung zur Benutzung der Tutorialreihe`.

## Zum Begriff und weiteren englischen Begriffen

**Calculus** ist der *englische* Begriff für die **Differentialrechnung**, die in deutschsprachigen Gebieten zusammen mit der *Integralrechnung* unter der Bezeichnung **Infinitesimalrechnung** zusammengefasst wird. Eine oft in deutschen Universitäten verwendete vergleichbare Bezeichnung für Calculus ist **Analysis II**, wobei **Analysis I** dann für *Lineare Algebra* steht. Eine wirkliche allgemeingültige Bezeichnung gibt es leider nicht, weshalb hier der englische Begriff **Calculus** verwendet wurde. Ein weiterer Grund für die Verwendung des englischen Begriffs ist die bessere Orientierung nach dem Durcharbeiten dieser Tutorialreihe. Da Sie diese Tutorialreihe vermutlich im Rahmen Ihres Digital Humanities Studium bearbeiten werden, werden die meisten Texte, die Sie in Ihrem Studium lesen werden, auf Englisch sein; vor allem die neusten Paper und die wichtigsten Fachbücher werden primär auf Englisch veröffentlicht. Ihnen sollten deshalb die englischen Begriffe geläufig sein. Um Ihnen den Umstieg dann zu erleichtern, wurden bei der Einführung der wichtigsten Konzepte in dieser Tutorialreihe neben der Nennung des deutschen Namens auch oft der englische Name genannt. In einigen Fällen wird, wenn der englische Begriff weitaus populärer und omnipräsenter ist, primär der englische Begriff verwendet (z.B. bei **Gradient Descent** in Kapitel 10); ansonsten werden doch vorzugsweise die deutschen Begriffe verwendet, um eine gewisse Homogenität in den erläuternden Texten zu bewahren.

## Benötigtes Vorwissen

Um diese Tutorialreihe nutzen zu können, muss ein mathematisches Grundwissen vorliegen. Dieses geht jedoch nicht über das Schulwissen hinaus. Die ersten Kapitel dieser Tutorialreihe wiederholen zudem beinahe ausschließlich Schulstoff, was Ihnen dabei helfen soll, ihr Wissen aufzufrischen und an manchen Stellen auszubauen. Sollten Dinge innerhalb eines Kapitels auftreten, welches Sie nicht verstehen, da Ihnen das nötige Vorwissen fehlt, sollten Sie diese Wissenslücke <u>selbstständig</u> schließen. Lernplattformen wie <a href="https://www.mathebibel.de/">https://www.mathebibel.de/</a> bieten sich dafür hervorragend an.

Ab etwa Kapitel 7 sollten sie die Grundkenntnisse zur **Linearen Algebra** verinnerlicht haben. Bis zu diesem Zeitpunkt können Sie also die Tutorialreihe als eigenständige Tutorialreihe betrachten. Es wird jedoch empfohlen, die diesem Projekt ebenfalls beiliegende Tutorialreihe zur Linearen Algebra <u>vor</u> oder mindestens während dieser Tutorialreihe zu bearbeiten.

Ansonsten sollten Sie Grundkenntnisse in **Python3** und der Benutzung von **Jupyter Notebooks** haben, da diese Tutorials nur in Jupyter Notebooks erstellt worden sind. Ab und zu stoßen Sie auf Python-Code innerhalb von Code-Zellen, den Sie ausführen müssen. Dort müssen Sie jedoch meistens nur kleine Änderungen vornehmen wie das Ändern eines Boolean-Werts. 


## Aufbau der Tutorialreihe

Die folgenden Kapitel sind in dieser Tutorialreihe enthalten (das aktuelle Kapitel nicht berücksichtigt):<br>

<i>01 - Einführung zu Funktionen<br>
02 - Rationale Funktionen<br>
03 - Weitere Funktionstypen<br>
04 - Steigung berechnen<br>
05 - Ableitungsregeln<br>
06 - Multivariate Funktionen und partielle Ableitungen<br>
07 - Gradient, Jacobi- und Hesse-Matrix<br>
08 - Multivariate Kettenregel<br>
09 - Taylorreihen<br>
10 - Gradient Descent</i><br>

Die Kapitel sind **kontinuierlich** aufgebaut, d.h. alle Kapitel sollten nacheinander durchgenommen werden. Die Kapitel lassen sich in zwei große Themenkomplexe bzw. Schwierigkeiten aufteilen:<br>

Kapitel 01 - 05: **Einsteigerkapitel zu Funktionen**<br>
Kapitel 06 - 10: **Fortgeschrittene Kapitel zu Ableitungen**<br>

Die Kapitel 1 bis 5 sind die Einsteigerkapitel dieser Tutorialreihe, da sie im Grunde nur den in der Schule behandelten Stoff zu Calculus wiederholen. Trotzdem sind diese sehr wichtig und sollten nicht übersprungen werden, da sie die Grundlage für die fortgeschritteneren Themen in Kapitel 6 bis 10 bilden. Verweise auf diese Kapitel in späteren Kapiteln sind nicht unüblich, nach Abschluss von Kapitel 5 sollten auch die Ableitungsregeln auf Funktionen angewendet werden können. Diese Kapitel können jedoch ohne großes mathematisches Vorwissen verwendet werden. Dieser Einsteigerkapitel teilen sich inhaltlich wiederum in zwei Teile auf: Während es in Kapitel 1 bis 3 um Funktionen und ihren Aufbau geht, behandeln Kapitel 4 und 5 die Idee und die Rechenregeln von Ableitungen.

Die Kapitel 6 bis 10 benötigen jedoch Vorwissen zur **Linearen Algebra**, weshalb zuvor das ebenfalls diesem Projekt beiliegende Tutorial zur Linearen Algebra <u>vor</u> der Bearbeitung dieser Kapitel durchgenommen werden sollte. Die wichtigsten benötigten Konzepte der Linearen Algebra werden zu Beginn von Kapitel 7 aufgelistet, da diese ab diesem Kapitel benötigt werden. Auch diese Kapitel lassen sich in zwei weitere Themen unterteilen: In Kapitel 6 bis 8 geht es um multivariate Funktionen und ihre Ableitungen. Kapitel 9 und 10 bilden schließlich den Abschluss der Tutorialreihe und behandeln die Annäherung bzw. Approximation von Funktionen und ihren Lösungen.


## Aufbau eines Kapitels

Ein Kapitel beginnt immer mit der **Kapitelübersicht**, welches die folgenden Dinge beinhaltet:
- **Kurzbeschreibung des Kapitelinhalts**
- **Abschnittsübersicht** mit Links zu den Abschnitten eines Kapitels
- **Quizübersicht** mit Links zu den Quizzen (wenn vorhanden)
- **Übersicht zu den behandelten Themen**, welches auch als eine Art Index des Kapitels fungiert

Die Abschnitte selbst bestehen meist aus Erklärungen in Textform. Weitere wichtige Elemente sind **interaktive Funktionsgraphen**, die mithilfe von Code-Zellen ausgeführt werden. Diese enthalten Python-Code und rufen eine Funktion auf, mit der die Graphen geplottet werden und mit welchen Sie dann interagieren können. Ändern Sie bitte nichts in dieser Code-Zelle, außer Sie erhalten die entsprechende Anweisung. Ebenfalls in Code-Zellen befinden sich die Funktionsaufrufe, mit denen die **Quizze** ausgeführt werden. Diese sollten Sie ebenfalls nicht verändern. Ab und zu gibt es weiterführende Links zu **YouTube-Videos**, in denen Rechenwege detailliert durchgeführt und erläutert werden.


Ein zentrales Element innerhalb der Abschnitte sind bestimmte **Felder**, die je nach Farbe des Rahmens eine andere Bedeutung haben. Beispiele dieser Felder befinden sich in `Kapitel 0 - Anleitung zur Benutzung der Tutorialreihe`.

## Verwendung eines Kapitels

Bevor Sie mit der Arbeit an einem Kapitel beginnen, sollten Sie immer zuerst alle Zellen des Notebooks ausführen. Idealerweise, indem sie in der oberen Menüleiste ```Cell --> Run all``` ausführen. Manchmal kann es sein, dass einzelne Zellen Bilder oder andere Dinge merkwürdig darstellen. Führen Sie dann einfach einzelne Zellen nochmals aus, da Jupyter manchmal Probleme damit hat, externe Inhalte zu laden. Vor allem die Werkzeugkästen werden teilweise merkwürdig dargestellt.

**Quizze** tauchen in zwei verschiedenen Varianten auf:
- Die erste Variante erscheint innerhalb eines *Aufgaben*-Blocks. In diesem gibt es meistens nur eine Frage und eine versteckte Antwort, welche Sie mithilfe eines Buttons aufdecken können. 
- Die andere Variante sind die interaktiven Quizze, welche durch Funktionsaufrufe (z.B. `start_quiz(12, "calculus")`) in Code-Zellen ausgeführt werden. Diese Quizze sind Single-Choice Quizze, Sie können zu jeder Frage nur eine Antwort auswählen. Bei der Frage müssen Sie, nachdem Sie eine Antwort ausgewählt haben, auf den Button "Abschicken" klicken. Der Button sollte dann ausgegraut werden. Sie können die Antwort dann immer noch ändern, Sie müssen dafür nur eine andere Antwort auswählen und dann erneut auf "Abschicken" klicken. Sind Sie mit Ihren Antworten zufrieden, drücken Sie den Button "Ausgewählte Antworten überprüfen" am Ende des Quiz. Dort wird angezeigt, wieviele Fragen Sie richtig beantwortet haben und Sie erhalten Feedback zu Ihren Antworten. Sie können ein Quiz beliebig oft durchführen.

Ein Beispielquiz sehen Sie in `Kapitel 0 - Anleitung zur Benutzung der Tutorialreihe`.





