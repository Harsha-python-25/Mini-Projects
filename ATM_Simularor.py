print("""Welcome to ATM Simulator
Select from the options below 
Balance
Withdraw
Transfer
Deposit
Quit""")
user_selection = ""
current_balance = 1000
while True:
    user_selection = input("> ").lower()
    if user_selection == "balance":
        print("Your current balance is:", current_balance)
    elif user_selection == "deposit":
        dep=int(input("Please enter the amount you want to deposit: "))
        current_balance += dep
        print("Your current balance is:", current_balance)
    elif user_selection == "transfer":
        while True:
            account_num = input("Please enter the 13-digit account number you want to transfer to: ")
            if len(account_num) == 13 and account_num.isdigit():
                transfer = int(input("Please enter the amount you want to transfer: "))
                if transfer <= current_balance:
                    current_balance -= transfer
                    print(f"""
        You have transferred ${transfer} to {account_num}
        Your current balance is: ${current_balance}
        """)
                    break  # exit the inner loop after successful transfer
                else:
                    print("Insufficient balance. Your current balance is:", current_balance)
                    break  # still exit transfer flow
            else:
                print("❌ Invalid account number. Please enter exactly 13 digits.")
    elif user_selection == "withdraw":
        withdraw=int(input("Please enter the amount you want to withdraw: "))
        if withdraw <= current_balance:
            current_balance -= withdraw
            print("Your current balance is:", current_balance)
        else:
            print("Sorry Low on funds")
    elif user_selection == "quit":
        break
else:
    print("invalid input")