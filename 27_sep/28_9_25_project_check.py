# 🏧 ATM Machine Project with User Input & Exception Handling

# ----------- CREATE ACCOUNT -----------
print("===== Create Your ATM Account =====")
acc_id = input("Enter Account ID: ").strip()
name = input("Enter Your Name: ").strip().capitalize()

# PIN must be 4 digits
while True:
    pin = input("Set 4-digit PIN: ").strip()
    if pin.isdigit() and len(pin) == 5:
        break
    else:
        print("❌ Invalid PIN! Must be exactly 5 digits.")

# Initial balance (with exception handling)
while True:
    try:
        amount = int(input("Enter Initial Balance: "))
        break
    except ValueError:
        print("❌ Please enter a valid number for balance!")

# Store user account inside a list
accounts = [
    [acc_id, name, pin, amount]
]

print("\n✅ Account Created Successfully!")
print(f"Your Account ID: {acc_id}, Name: {name}, Balance: Rs.{amount}\n")

# ----------- LOGIN SYSTEM -----------
login_success = False
user = None

while not login_success:
    login_id = input("Enter Account ID to Login: ").strip()
    login_pin = input("Enter PIN: ").strip()

    for acc in accounts:
        if acc[0] == login_id and acc[2] == login_pin:
            login_success = True
            user = acc
            break

    if not login_success:
        print("❌ Invalid ID or PIN. Try again.\n")

print(f"\n✅ Login successful! Welcome {user[1]}.")

# ----------- MAIN MENU -----------
while True:
    print("\n===== ATM Menu =====")
    print("1. 💰 Check Balance")
    print("2. 💸 Cash Withdraw")
    print("3. 🔄 Transfer")
    print("4. 🔑 Change PIN")
    print("5. ❌ Exit")

    choice = input("Enter your choice: ").strip()

    # Check Balance
    if choice == "1":
        print(f"Your current balance is: Rs. {user[3]}")

    # Withdraw
    elif choice == "2":
        try:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount <= 0:
                print("❌ Enter a valid positive amount!")
            elif withdraw_amount <= user[3]:
                user[3] -= withdraw_amount
                print(f"✅ Withdraw successful. Remaining Balance: Rs. {user[3]}")
            else:
                print("❌ Insufficient Balance!")
        except ValueError:
            print("❌ Invalid input! Enter numbers only.")

    # Transfer
    elif choice == "3":
        receiver_id = input("Enter receiver Account ID: ").strip()
        try:
            transfer_amount = int(input("Enter amount to transfer: "))
            if transfer_amount <= 0:
                print("❌ Enter a valid positive amount!")
                continue

            found = False
            for acc in accounts:
                if acc[0] == receiver_id and acc != user:
                    found = True
                    if transfer_amount <= user[3]:
                        user[3] -= transfer_amount
                        acc[3] += transfer_amount
                        print(f"✅ Transfer Successful! Rs.{transfer_amount} sent to {acc[1]}.")
                    else:
                        print("❌ Insufficient Balance!")
            if not found:
                print("❌ Receiver Account not found!")
        except ValueError:
            print("❌ Invalid input! Enter numbers only.")

    # Change PIN
    elif choice == "4":
        new_pin = input("Enter new 4-digit PIN: ").strip()
        if new_pin.isdigit() and len(new_pin) == 4:
            user[2] = new_pin
            print("✅ PIN Changed Successfully!")
        else:
            print("❌ Invalid PIN format! Must be 4 digits.")

    # Exit
    elif choice == "5":
        print("👋 Thank you for using ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
