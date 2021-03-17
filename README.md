<h1><img  src="src/logo.png" alt="logo" width="98" height="24" style="float: left;">&nbsp;&nbsp;Math for Digital Humanities students</h1>



Das **MADH** (= Math for Digital Humanities students) Projekt ist eine Mathe-Tutorialreihe für Studierende der Digital Humanities. Mathe-Kenntnisse in den ausgewählten Bereichen **Lineare Algebra** und **Calculus** sollen aufgefrischt, erweitert und eingegrenzt werden. Es wird empfohlen, zuerst das Tutorial zur "Linearen Algebra" durchzugehen, bevor das Tutorial "Calculus" angegangen wird, da dies ab der zweiten Hälfte auf dem Linearen Algebra Tutorial aufbaut.

Bei Problemen mit der Tutorialreihe sollte entweder ein *Issue* auf Github aufgemacht werden oder eine Mail an die folgende Adresse gesendet werden: [madhwuerzburg@gmail.com](madhwuerzburg@gmail.com)


# Bedienungsanleitung

Für die Nutzung der Bedienungsanleitung wird die Offline-Nutzung empfohlen. Die folgenden Schritte müssen für die Benutzung der Tutorials ausgeführt werden:
1. Das Repository klonen / downloaden & entpacken (siehe auch "Installationsanleitung (Anfänger) / Download").
2. In das Verzeichnis *madh* des geklonten/gedownloadeten Verzeichnis mithilfe eines Terminals navigieren.
3. Die Requirements des Projekts installieren (siehe "Installationsanleitung (Anfänger) / Installation des gedownloadeten Projekts").
3. Jupyter Notebook mithilfe des Befehls `jupyter-notebook` oder `jupyter notebook` ausführen.
4. Im geöffneten Browserfenster zum "Calculus" oder "Lineare Algebra"-Ordner navigieren und die darin enthaltenen Notebooks ausführen.

<u>ACHTUNG</u>: Die Offline-Nutzung mit <b>Jupyter Lab</b> wird nicht unterstützt. Bei der Benutzung von Jupyter Lab können Javascript Befehle, die z.B. in Quizzen verwendet werden, nicht dargestellt werden. Für die Verwendung mit Jupyter Lab muss eine Erweiterung installiert werden (siehe <a href="https://stackoverflow.com/questions/49542417/how-to-get-ipywidgets-working-in-jupyter-lab">Stackoverflow</a>).

## Installationsanleitung (Anfänger)

### Download

Über Button <img src="Calculus/img/clone_download.png" alt="clone_download-icon" width="60" height="12"/> in der rechten oberen Ecke dieser Seite kann das Projekt geklont oder gedownloadet werden ("Download ZIP"). Sollte es gedownloadet werden, muss das ZIP-Archiv entpackt werden. Mit dem Terminal muss in das entsprechende Verzeichnis navigiert werden.


### Installation des gedownloadeten Projekts

Erforderlich: Python 3.6+

#### Installation mit conda (empfohlen für Anfänger)
Diese Option wird für Anfänger empfohlen, die **Anaconda** installiert haben.

`conda install -r requirements.txt`

#### Installation mit pip

`pip install -r requirements.txt`

## Requirements

```
ipywidgets
typing
ipython
numpy
matplotlib
mpl_toolkits
scipy
```


## Unterstütze Systeme

* Windows 10
* MacOS Catalina
* Manjaro

