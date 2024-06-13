from scripts.utils import load_income_data, save_data

def add_income(date, source, amount, description):
    income = load_income_data()
    new_income = {"Date": date, "Source": source, "Amount": amount, "Description": description}
    income = income.append(new_income, ignore_index=True)
    save_data(income, 'data/income.csv')