import matplotlib.pyplot as plt
from scripts.utils import load_data

def plot_income_over_time():
    income = load_data('data/income.csv')
    if income.empty:
        print("No income data to plot.")
        return

    income['Date'] = pd.to_datetime(income['Date'])
    income.set_index('Date', inplace=True)
    income['Amount'].plot(kind='line')
    plt.title("Income Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.show()

