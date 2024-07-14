import pandas as pd

def load_excel_data(file):
    try:
        df = pd.read_excel(file)
        # Stelle sicher, dass die erwarteten Spalten vorhanden sind
        required_columns = ["Name", "Alter", "Job", "Bruttogehalt", "Steuersatz"]
        if set(required_columns).issubset(df.columns):
            # Konvertiere DataFrame in eine Liste von Diktaten
            data = df.to_dict(orient='records')
            for person in data:
                person["Nettogehalt"] = person["Bruttogehalt"] * (1 - person["Steuersatz"] / 100)
            return data
        else:
            raise ValueError(f"Excel file does not have the required columns: {', '.join(required_columns)}")
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")

def load_csv_data(file):
    try:
        df = pd.read_csv(file)
        # Stelle sicher, dass die erwarteten Spalten vorhanden sind
        required_columns = ["Name", "Alter", "Job", "Bruttogehalt", "Steuersatz"]
        if set(required_columns).issubset(df.columns):
            # Konvertiere DataFrame in eine Liste von Diktaten
            data = df.to_dict(orient='records')
            for person in data:
                person["Nettogehalt"] = person["Bruttogehalt"] * (1 - person["Steuersatz"] / 100)
            return data
        else:
            raise ValueError(f"CSV file does not have the required columns: {', '.join(required_columns)}")
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")
