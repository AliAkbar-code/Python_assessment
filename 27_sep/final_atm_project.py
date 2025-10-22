import datetime


accounts = {
    "1": {"name": "Ali", "pin": "1234", "balance": 10000000, "history": [], "last_used": None},
    "2": {"name": "Ahmed", "pin": "5678", "balance": 10000000, "history": [], "last_used": None},
    "3": {"name": "Sara", "pin": "9999", "balance": 10000000, "history": [], "last_used": None},
}

# --------------------------- LOGIN ---------------------------
login_success = False
user_id = None
user = None

while not login_success:
    login_id = input("Enter Account ID to Login: ").strip()
    login_pin = input("Enter PIN: ").strip()

    if login_id in accounts and accounts[login_id]["pin"] == login_pin:
        login_success = True
        user_id = login_id
        user = accounts[user_id]
        print(f"\n Welcome {user['name']}! Login successful.\n")
    else:
        print(" Invalid ID or PIN. Try again.\n")

# --------------------------- ATM MENU ---------------------------
while True:
    print("\n\n===== ATM MENU =====")
    print("1. Create Transfer")
    print("2. Change PIN")
    print("3. Cash Withdraw")
    print("4. Check Transaction History")
    print("5. Check Balance")
    print("6. Last ATM Usage")
    print("7. Exit")

    choice = input("Choose an option: ").strip()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user["last_used"] = now  # update last usage time

    # 1. Transfer
    if choice == "1":
        receiver_id = input("Enter Receiver Account ID: ").strip()
        amount = float(input("Enter Amount to Transfer: "))

        if receiver_id in accounts:
            if user["balance"] >= amount:
                user["balance"] -= amount
                accounts[receiver_id]["balance"] += amount
                user["history"].append(f"Transferred {amount} to {accounts[receiver_id]['name']} on {now}")
                print(f" Successfully transferred {amount} to {accounts[receiver_id]['name']}")
            else:
                print(" Insufficient balance.")
        else:
            print(" Receiver account not found.")

    # 2. Change PIN
    elif choice == "2":
        old_pin = input("Enter current PIN: ")
        if old_pin == user["pin"]:
            new_pin = input("Enter new PIN: ")
            user["pin"] = new_pin
            print(" PIN changed successfully.")
        else:
            print(" Wrong PIN entered.")

    # 3. Withdraw
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if user["balance"] >= amount:
            user["balance"] -= amount
            user["history"].append(f"Withdrew {amount} on {now}")
            print(user["history"]) 
            print(f" Successfully withdrew {amount}")
        else:
            print(" Insufficient balance.")

    # 4. Transaction history
    elif choice == "4":
        print("\n Transaction History:")
        if user["history"]:
            for h in user["history"]:
                print(h)
        else:
            print("No transactions yet.")

    # 5. Check balance
    elif choice == "5":
        print(f" Current Balance: {user['balance']}")

    # 6. Last ATM usage
    elif choice == "6":
        if user["last_used"]:
            print(f" Last used ATM on: {user['last_used']}")
        else:
            print("No usage recorded.")

    # 7. Exit
    elif choice == "7":
        print(" Thank you for using ATM. Goodbye!")
        break

    else:
        print(" Invalid option. Please try again.")
