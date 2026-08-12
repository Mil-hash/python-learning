expenses = []

def add_expense():
    name = input ("What was the expense for? ")
    amount = float(input("How much? "))
    expenses.append([name, amount])
    print("Added!")
def view_expenses():
    print("All expenses:")
    for expense in expenses:
        print("- " + expense[0] + ": " + str(expense[1]))

def show_total():
    total = 0
    for expense in expenses:
        total = total + expense[1]
    print("Total spent: " + str(total))

while True:
    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")