from scripts.add_expenses import add_expense
from scripts.add_income import add_income
from scripts.view_summary import view_summary
from scripts.plot_expenses import plot_expenses_by_category
from scripts.plot_income import plot_income_over_time

def main():
    while True:
        print("Personal Finance Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Summary")
        print("4. Plot Expenses by Category")
        print("5. Plot Income Over Time")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            source = input("Enter source: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_income(date, source, amount, description)
        elif choice == '3':
            view_summary()
        elif choice == '4':
            plot_expenses_by_category()
        elif choice == '5':
            plot_income_over_time()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
