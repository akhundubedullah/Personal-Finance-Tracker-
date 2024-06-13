from scripts.utils import load_data

def view_summary():
    expenses = load_data('data/expenses.csv')
    income = load_data('data/income.csv')

    total_expenses = expenses['Amount'].sum()
    total_income = income['Amount'].sum()
    balance = total_income - total_expenses

    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Balance: ${balance:.2f}")

