# Streamlit Anwendung - Gehaltsverwaltung

Dieses Repository enthält eine einfache Streamlit-Anwendung, die es Benutzern ermöglicht, Gehaltsinformationen einzugeben, anzuzeigen und zu verwalten. Die Anwendung unterstützt das Hinzufügen von Daten über eine Benutzeroberfläche und das Laden von Daten aus Excel- oder CSV-Dateien.

## Funktionen

- Eingabe von Namen, Alter, Job, Bruttogehalt und Steuersatz für einzelne Personen.
- Anzeige und Verwaltung von eingetragenen Gehaltsdaten.
- Berechnung und Anzeige aggregierter Statistiken wie Summe der Bruttogehälter, Median der Brutto- und Nettogehälter, sowie Durchschnittsalter.


## Python Imports

Die folgenden Python-Module werden in diesem Projekt verwendet und für die folgenden Zwecke importiert:

- **streamlit**: Zur Erstellung der Webanwendung und interaktiven Benutzeroberfläche.
- **pandas**: Zur Datenverarbeitung, einschließlich des Lesens, Schreibens und der Manipulation von Datenframes.
- **os**: Zur Interaktion mit dem Betriebssystem, z.B. zum Überprüfen und Erstellen von Verzeichnissen.
- **pickle**: Zur Serialisierung und Deserialisierung von Python-Objekten, z.B. zum Speichern und Laden von Datenstrukturen.

## Todo

- Laden von Daten aus Excel- oder CSV-Dateien zur Masseneingabe von Gehaltsinformationen. (implementiert, aber funktioniert noch nicht)


## Installation


   ```bash
   git clone https://github.com/xenoplayed/python-streamlit-example
   cd python-streamlit-example
   pip install -r requirements.txt
```

Führen Sie die folgenden Befehle aus, um die Streamlit-Anwendung zu starten:

```bash
streamlit run app.py
```


