balance = 0

def deposit():
    global balance
    amount = float(input("Amount to deposit: "))
    balance = balance + amount
    print("Deposited!")

def withdraw():
    global balance
    amount = float(input("Amount to withdraw: "))
    if amount > balance:
        print("Not enough money!")
    else:
        balance = balance - amount
        print("withdrawn!")

def show_balance():
    print("your balance is: " + str(balance))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("choose an option: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        ("Invalid choice!")