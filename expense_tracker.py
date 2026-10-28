import json

EXPENSES_FILE = "expenses.json"

expenses = []


def load_data():
    global expenses
    try:
        with open(EXPENSES_FILE, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []


def save_data():
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense():
    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number (e.g. 250 or 99.50).")
        return

    category = input("Enter the expense category (food/travel/shopping/other): ")
    description = input("Enter the expense description: ")
    date = input("Enter the expense date (YYYY-MM-DD): ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_data()
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}, Date: {exp['date']}")


def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    choice = input("Enter the expense number to delete (0 to cancel): ")

    if not choice.isdigit():
        print("Enter a valid number")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(expenses):
        print("Invalid expense number.")
        return

    removed = expenses.pop(index)
    save_data()
    print(f"Expense '{removed['description']}' deleted successfully!")


def view_summary():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    total = sum(expense['amount'] for expense in expenses)

    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\n--- Expense Summary ---")
    print(f"Total Expenses: {total}")
    print("Expenses by Category:")
    for category, amount in category_totals.items():
        print(f"{category}: {amount}")


load_data()

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View Expense Summary")
    print("4. Delete Expense")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please try again.")