import streamlit as st

def input_form():
    name = st.text_input("Name")
    age = st.number_input("Alter", min_value=0, max_value=120, step=1)
    job = st.text_input("Job")
    gross_salary = st.number_input("Bruttogehalt", min_value=0.0, step=100.0)
    tax_rate = st.number_input("Steuersatz (%)", min_value=0.0, max_value=100.0, step=1.0)

    if st.button("Daten hinzufügen"):
        if name and job and gross_salary > 0:
            net_salary = gross_salary * (1 - tax_rate / 100)
            return {"Name": name, "Alter": age, "Job": job, "Bruttogehalt": gross_salary, "Steuersatz": tax_rate, "Nettogehalt": net_salary}
        else:
            st.error("Bitte füllen Sie alle Felder aus und stellen Sie sicher, dass das Bruttogehalt größer als 0 ist")
    return None
