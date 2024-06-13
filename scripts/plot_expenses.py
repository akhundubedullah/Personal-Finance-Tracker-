import matplotlib.pyplot as plt
from scripts.utils import load_data

def plot_expenses_by_category():
    expenses = load_data('data/expenses.csv')
    if expenses.empty:
        print("No expenses to plot.")
        return

    expense_summary = expenses.groupby("Category")['Amount'].sum()
    expense_summary.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.ylabel('')  # Hide y-label
    plt.show()

