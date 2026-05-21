balance = 0   # Global Variable

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("₹", amount, "deposited successfully.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")
    else:
        print("Insufficient balance!")

def check_balance():
    global balance
    print("Current Balance = ₹", balance)

# Main Program
balance = float(input("Enter initial balance: "))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit()

    elif choice == 2:
        withdraw()

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")