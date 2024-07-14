import streamlit as st
import pandas as pd
from data_manager import load_data, save_data
from ui import input_form
from excel_loader import load_excel_data, load_csv_data

# Daten laden
data = load_data()

# Möglichkeit, Daten aus einer Excel- oder CSV-Datei zu laden
st.sidebar.title("Optionen")
upload_file = st.sidebar.file_uploader("Datei hochladen", type=["xlsx", "csv"])

if upload_file is not None:
    try:
        if upload_file.type == 'application/vnd.ms-excel':
            file_data = load_excel_data(upload_file)
        elif upload_file.type == 'text/csv':
            file_data = load_csv_data(upload_file)
        else:
            raise ValueError("Ungültiger Dateityp. Bitte laden Sie eine Excel- oder CSV-Datei hoch.")

        if st.sidebar.button("Daten laden"):
            data.extend(file_data)
            save_data(data)
            st.success("Daten erfolgreich geladen")
    except ValueError as e:
        st.error(e)

# Eingabefelder für den Benutzer und Daten hinzufügen
new_data = input_form()

# Daten hinzufügen und speichern
if new_data:
    data.append(new_data)
    save_data(data)
    st.success("Daten erfolgreich hinzugefügt")

# Anzeige der gespeicherten Daten
if data:
    df = pd.DataFrame(data)
    # Formatierung der Ausgabe
    df['Bruttogehalt'] = df['Bruttogehalt'].apply(lambda x: f"€{x:,.2f}")
    df['Steuersatz'] = df['Steuersatz'].apply(lambda x: f"{x:.2f}%")
    df['Nettogehalt'] = df['Nettogehalt'].apply(lambda x: f"€{x:,.2f}")

    # Tabelle für individuelle Daten anzeigen
    st.write("Eingegebene Daten:")
    st.dataframe(df)

    # Aggregierte Statistiken
    if st.button("Statistiken anzeigen"):
        st.header("Gehälter Statistiken")
        salary_statistics = {
            'Summe Bruttogehälter': df['Bruttogehalt'].str.replace('€', '').str.replace(',', '').astype(float).sum(),
            'Median Bruttogehalt': df['Bruttogehalt'].str.replace('€', '').str.replace(',', '').astype(float).median(),
            'Median Nettogehalt': df['Nettogehalt'].str.replace('€', '').str.replace(',', '').astype(float).median()
        }
        salary_statistics_df = pd.DataFrame(salary_statistics, index=[0])
        st.dataframe(salary_statistics_df.style.format(formatter={'Summe Bruttogehälter': '{:.2f} EUR', 
                                                                 'Median Bruttogehalt': '{:.2f} EUR', 
                                                                 'Median Nettogehalt': '{:.2f} EUR'}))

        st.header("Personal Statistiken")
        personal_statistics = {
            'Durchschnittsalter': df['Alter'].mean()
        }
        personal_statistics_df = pd.DataFrame(personal_statistics, index=[0])
        st.dataframe(personal_statistics_df)

else:
    st.write("Noch keine Daten eingegeben.")
