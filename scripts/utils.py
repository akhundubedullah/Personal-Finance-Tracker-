import pandas as pd

def load_expenses_data():
    try:
        expenses_data = pd.read_csv('data/expenses.csv')
    except FileNotFoundError:
        expenses_data = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    return expenses_data

def load_income_data():
    try:
        income_data = pd.read_csv('data/income.csv')
    except FileNotFoundError:
        income_data = pd.DataFrame(columns=["Date", "Source", "Amount", "Description"])
    return income_data

def save_data(data, file_path):
    data.to_csv(file_path, index=False)


