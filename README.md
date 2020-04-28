# MADH: Math for Digital Humanities students


# Bedienungsanleitung

Für die Nutzung der Bedienungsanleitung wird aktuell die Offline-Nutzung empfohlen. Die folgenden Schritte müssen für die Benutzung der Tutorials ausgeführt werden:
1. Das Repository klonen / downloaden & entpacken (siehe auch "Installationsanleitung (Anfänger) / Download")
2. In das Verzeichnis *madh* des geklonten/gedownloadeten Verzeichnis mithilfe eines Terminals navigieren
3. Die Requirements des Projekts installieren (siehe "Installationsanleitung (Anfänger) / Installation des gedownloadeten Projekts")
3. Jupyter Notebook mithilfe dem Befehl `jupyter-notebook` oder `jupyter notebook` ausführen
4. Im geöffneten Browserfenster zum "Calculus" oder "Lineare Algebra"-Ordner navigieren und die darin enthaltenen Notebooks ausführen

<u>ACHTUNG</u>: Die Offline-Nutzung mit <b>Jupyter Lab</b> wird nicht unterstützt. Bei der Benutzung von Jupyter Lab können Javascript Befehle, die z.B. in Quizzen verwendet werden, nicht dargestellt werden. Für die Verwendung mit Jupyter Lab muss eine Erweiterung installiert werden (siehe <a href="https://stackoverflow.com/questions/49542417/how-to-get-ipywidgets-working-in-jupyter-lab">Stackoverflow</a>).

## Installationsanleitung (Anfänger)

### Download

Über Button <img src="src/img/clone_download.png" alt="clone_download-icon" width="60" height="12"/> in der rechten oberen Ecke dieser Seite kann das Projekt geklont oder gedownloadet werden ("Download ZIP"). Sollte es gedownloadet werden, muss das ZIP-Archiv entpackt werden. Mit dem Terminal muss in das entsprechende Verzeichnis navigiert werden (Tutorial dafür: TODO).


### Installation des gedownloadeten Projekts

Erforderlich: Python 3.6+

#### Installation mit conda (empfohlen für Anfänger) 
(TODO: Es ist sicherer eine eigene virtuelle Umgebung einzurichten, unter conda mit conda create)
Diese Option wird für Anfänger empfohlen, die **Anaconda** installiert haben.

`conda install --file requirements.txt` (TODO: requirements installieren)

#### Installation mit pip

`pip install -r requirements.txt` (TODO: requirements installieren)

