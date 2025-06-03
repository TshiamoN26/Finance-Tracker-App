# Branch: add-name-fields-expense-income
# Purpose: Added expense_name and income_name fields to expenses and
# income tables

import sqlite3

EXPENSES_TABLE = "expenses"
INCOME_TABLE = "income"
BUDGETS_TABLE = "budgets"
GOALS_TABLE = "goals"

# Connect to SQLite database
conn = sqlite3.connect("finance_tracker.db")
cursor = conn.cursor()

# Create necessary tables
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    expense_name TEXT,
    category TEXT,
    amount REAL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY,
    income_name TEXT,
    category TEXT,
    amount REAL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
    category TEXT PRIMARY KEY,
    budget_limit REAL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY,
    description TEXT,
    target REAL,
    progress REAL DEFAULT 0
)''')

conn.commit()

# Function Definitions


def add_expense():
    """
    Adds a new expense to the database.
    Prompts the user for the expense name, category, and amount.
    """
    try:
        expense_name = input("Enter expense name: ")
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))
        cursor.execute(
            "INSERT INTO expenses (expense_name, category, amount) "
            "VALUES (?, ?, ?)",
            (expense_name, category, amount)
        )
        conn.commit()
        print("Expense added.")
    except Exception as e:
        print(f"Error: {e}")


def view_expenses():
    """
    Displays all expenses in the database, showing the name, category,
    and amount.
    """
    cursor.execute("SELECT expense_name, category, amount FROM expenses")
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Category: {row[1]}, Amount: {row[2]}")


def view_expenses_by_category():
    """
    Displays all expenses for a specific category.
    Prompts the user for the category and shows the name and amount
    of each expense.
    """
    category = input("Enter category: ")
    cursor.execute(
        "SELECT expense_name, amount FROM expenses WHERE category = ?",
        (category,)
    )
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Amount: {row[1]}")


def add_income():
    """
    Adds a new income entry to the database.
    Prompts the user for the income name, category, and amount.
    """
    try:
        income_name = input("Enter income name: ")
        category = input("Enter income category: ")
        amount = float(input("Enter amount: "))
        cursor.execute(
            "INSERT INTO income (income_name, category, amount) "
            "VALUES (?, ?, ?)",
            (income_name, category, amount)
        )
        conn.commit()
        print("Income added.")
    except Exception as e:
        print(f"Error: {e}")


def view_income():
    """
    Displays all income entries in the database, showing the name, category,
    and amount.
    """
    cursor.execute("SELECT income_name, category, amount FROM income")
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Category: {row[1]}, Amount: {row[2]}")


def view_income_by_category():
    """
    Displays all income entries for a specific category.
    Prompts the user for the category and shows the name and amount
    of each income entry.
    """
    category = input("Enter category: ")
    cursor.execute(
        "SELECT income_name, amount FROM income WHERE category = ?",
        (category,)
    )
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Amount: {row[1]}")


def set_budget():
    """
    Sets a budget limit for a specific category.
    Prompts the user for the category and budget limit.
    """
    try:
        category = input("Enter category: ")
        budget_limit = float(input("Enter budget limit: "))
        cursor.execute(
            "REPLACE INTO budgets (category, budget_limit) VALUES (?, ?)",
            (category, budget_limit)
        )
        conn.commit()
        print("Budget set.")
    except Exception as e:
        print(f"Error: {e}")


def view_budget():
    """
    Displays the budget limit for a specific category.
    Prompts the user for the category.
    """
    category = input("Enter category: ")
    cursor.execute(
        "SELECT budget_limit FROM budgets WHERE category = ?", (category,)
    )
    row = cursor.fetchone()
    if row:
        print(f"Budget for {category}: {row[0]}")
    else:
        print("No budget set for this category.")


def set_financial_goal():
    """
    Sets a financial goal.
    Prompts the user for the goal description and target amount.
    """
    try:
        description = input("Enter goal description: ")
        target = float(input("Enter goal amount: "))
        cursor.execute("INSERT INTO goals (description, target) VALUES (?, ?)",
                       (description, target))
        conn.commit()
        print("Goal set.")
    except Exception as e:
        print(f"Error: {e}")


def view_goal_progress():
    """
    Displays all financial goals along with their target and progress.
    """
    cursor.execute("SELECT description, target, progress FROM goals")
    for row in cursor.fetchall():
        print(f"Goal: {row[0]}, Target: {row[1]}, Progress: {row[2]}")


def update_goal_progress():
    """
    Updates the progress of a specific financial goal.
    Prompts the user for the goal ID and the new progress amount.
    """
    try:
        goal_id = int(input("Enter goal ID to update progress: "))
        progress = float(input("Enter new progress amount: "))
        cursor.execute("UPDATE goals SET progress = ? WHERE id = ?",
                       (progress, goal_id))
        conn.commit()
        print("Goal progress updated.")
    except Exception as e:
        print(f"Error: {e}")


def main_menu():
    """
    Displays the main menu and handles user input to execute the
    corresponding functions.
    """
    try:
        while True:
            print("""
1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View income by category
7. Set budget for a category
8. View budget for a category
9. Set financial goals
10. View progress towards financial goals
11. Update goal progress
12. Quit
""")
            choice = input("Choose an option: ")
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                view_expenses_by_category()
            elif choice == '4':
                add_income()
            elif choice == '5':
                view_income()
            elif choice == '6':
                view_income_by_category()
            elif choice == '7':
                set_budget()
            elif choice == '8':
                view_budget()
            elif choice == '9':
                set_financial_goal()
            elif choice == '10':
                view_goal_progress()
            elif choice == '11':
                update_goal_progress()
            elif choice == '12':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        conn.close()


if __name__ == "__main__":
    main_menu()
