# Final Project: CV Generator

#### Video Demo: https://youtu.be/bMwCCGnbpfU

Kurzbeschreibung:
Dieses Projekt erstellt automatisch einen einseitigen, A4-formatierten Lebenslauf (CV) aus Benutzereingaben. Aktuell erfolgt die Eingabe über die Kommandozeile. Ziel des Projekts war es, eine Grundlage zu schaffen, um den Prozess der CV-Erstellung zu vereinfachen.

Projektstruktur:


├── project.py        # Hauptdatei: Eingabe, Validierung, CV-Erstellung

├── cvgenerator.py    # PDF-Generierung für jede CV-Sektion

├── test_project.py   # Tests für die Validierungsfunktionen

├── assets/           # Bilder für Templates
│   ├── applicantf.png
│   ├── applicantm.png
│   ├── applicantn.png
│   └── cv_picture.png

└── cv.pdf            # Ergebnisdatei (erstellt nach Ausführung)


project.py

Enthält die main()-Funktion, die die Abläufe Schritt für Schritt ausführt.

Stellt Funktionen bereit, um:

- Benutzereingaben abzufragen

- Eingaben zu validieren

- Platzhalterdaten zu erzeugen, falls keine Eingabe erfolgt

Daten werden in Dictionaries gespeichert und anschließend an die Funktionen in cvgenerator.py übergeben.

Aufgeteilt in vier CV-Sektionen:

- Persönliche Informationen

- Ausbildung

- Qualifikationen (z.B. Sprachen)

- Berufserfahrung

  

cvgenerator.py

Verantwortlich für die PDF-Erstellung mithilfe der FPDF-Bibliothek.

Enthält Funktionen für jede CV-Sektion, die die validierten Daten ins PDF einfügen.

PDF-Vorlage:

- Seitenlayout, Linien, Titel und Rahmen für ein sauberes Layout

- Platzhalterbilder, falls Benutzer kein eigenes Bild auswählt

Funktionen:

- generate_personal_information(), generate_education(), etc.

- cursor_position() setzt Ränder und Positionen im PDF

  

test_project.py

Enthält pytest-Tests für die Validierungsfunktionen.

Überprüft:

- Rückgabe von Template-Dictionaries bei fehlenden Eingaben

- Rückgabe der Benutzer-Daten, falls vorhanden

Assets

Template-Bilder:

applicantf.png – weiblich

applicantm.png – männlich

applicantn.png – neutral

cv_picture.png – erstellt aus gewähltem Template während der Laufzeit


Nutzung

Projekt ausführen:

python project.py


Benutzereingaben eingeben:

Name, Geburtstag, Geburtsort

Ausbildung, Qualifikationen, Arbeitserfahrung

Template-Bild auswählen

CV wird als cv.pdf erstellt



Bekannte Einschränkungen / Zukunftspläne

Der Benutzer kann aktuell unbegrenzt Daten eingeben → Layout kann zerstört werden

Die CV-Generierung überprüft die Seitenbegrenzung noch nicht zuverlässig

Geplante Erweiterungen:

Limitierung der Eingaben basierend auf verfügbarem Platz

Möglichkeit für Benutzer, eigene Bilder hochzuladen

Webinterface für bequemere Eingabe

Technologien

Python 3

FPDF

Pytest

Fazit

Dieses Projekt ist ein praktisches Beispiel für:

Benutzereingaben sammeln und validieren

Strukturierte Daten in PDFs darstellen

Sauberes, modulares Design mit getrennten Funktionen für Input, Validierung und PDF-Erstellung
