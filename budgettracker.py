import sqlite3

# Create tables if they don't exist
def create_tables():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY,
        amount REAL,
        source TEXT,
        date TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
    ''')

    conn.commit()
    conn.close()

# Function to add income to the database
def add_income(amount, source, date):
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (amount, source, date) VALUES (?, ?, ?)", (amount, source, date))
    conn.commit()
    conn.close()

# Function to add expenses to the database
def add_expense(amount, category, description, date):
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?)", (amount, category, description, date))
    conn.commit()
    conn.close()

# Function to calculate the budget
def calculate_budget():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0] or 0

    conn.close()
    
    return total_income, total_expenses, total_income - total_expenses

# Function to analyze expenses by category
def analyze_expenses():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()

    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    category_expenses = cursor.fetchall()

    conn.close()
    return category_expenses

# Main menu function
def main_menu():
    print("\nBudget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. Analyze Expenses")
    print("5. Exit")

# Function to add income via user input
def add_income_menu():
    try:
        amount = float(input("Enter income amount: "))
        source = input("Enter income source: ")
        date = input("Enter date (YYYY-MM-DD): ")
        add_income(amount, source, date)
        print("Income added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")

# Function to add expense via user input
def add_expense_menu():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")
        date = input("Enter date (YYYY-MM-DD): ")
        add_expense(amount, category, description, date)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")

# Function to view the budget
def view_budget_menu():
    total_income, total_expenses, remaining_budget = calculate_budget()
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Budget: {remaining_budget}")

# Function to analyze expenses by category
def analyze_expenses_menu():
    category_expenses = analyze_expenses()
    print("Expenses by Category:")
    for category, amount in category_expenses:
        print(f"{category}: {amount}")

# Function to run the budget tracker application
def run_budget_tracker():
    create_tables()
    while True:
        main_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_income_menu()
        elif choice == '2':
            add_expense_menu()
        elif choice == '3':
            view_budget_menu()
        elif choice == '4':
            analyze_expenses_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    run_budget_tracker()
