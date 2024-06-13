from scripts.utils import load_expenses_data,save_data

def add_expense(date,category,amount,description):
    expenses = load_expenses_data()
    new_expense = {"Date": date, "Category": category, "Amount": amount, "Description": description}
    expenses = expenses.append(new_expense, ignore_index=True)
    save_data(expenses, 'data/expenses.csv')