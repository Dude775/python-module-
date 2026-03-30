# Lab ATM - Bank System

accounts = [
    {"account_id": 101, "name": "Daniel", "pin": "5678", "balance": 1000},
    {"account_id": 100, "name": "Liron", "pin": "1234", "balance": 500}
]

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

# חיפוש חשבון לפי ID - עובר על הרשימה ומחזיר את ה-dict או None
def find_account(account_id):
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    return None

# אימות PIN - משווה את מה שהמשתמש הזין למה ששמור בחשבון
def verify_pin(account, pin):
    return account["pin"] == pin

# התחברות אדמין - בודק username + password מול קבועים
def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    print("Access denied")
    return False

# יצירת חשבון - רק אדמין יכול, מייצר dict חדש ומוסיף לרשימה
def create_account():
    if not admin_login():
        return
    name = input("Enter name: ")
    pin = input("Set PIN: ")
    account = {
        "account_id": len(accounts) + 100,
        "name": name,
        "pin": pin,
        "balance": 0
    }
    accounts.append(account)
    print(f"Account created: {account['account_id']}")

# הפקדה - מוצא חשבון, מאמת PIN, מוסיף לbalance
def deposit():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")
    amount = float(input("Amount: "))
    account = find_account(account_id)
    if not account:
        print("Account not found")
        return
    if not verify_pin(account, pin):
        print("Wrong PIN")
        return
    if amount <= 0:
        print("Invalid amount")
        return
    account["balance"] += amount
    print(f"Deposited {amount}. New balance: {account['balance']}")

# משיכה - כמו הפקדה אבל עם בדיקת יתרה מספיקה
def withdraw():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")
    amount = float(input("Amount: "))
    account = find_account(account_id)
    if not account:
        print("Account not found")
        return
    if not verify_pin(account, pin):
        print("Wrong PIN")
        return
    if account["balance"] < amount:
        print("Insufficient funds")
        return
    account["balance"] -= amount
    print(f"Withdrew {amount}. New balance: {account['balance']}")

# הצגת חשבון בודד - מוצא ומאמת לפני הצגה
def show_account():
    account_id = int(input("Account ID: "))
    pin = input("PIN: ")
    account = find_account(account_id)
    if not account:
        print("Account not found")
        return
    if not verify_pin(account, pin):
        print("Wrong PIN")
        return
    print(account)

# הצגת כל החשבונות - רק אדמין
def show_all_accounts():
    if not admin_login():
        return
    for acc in accounts:
        print(acc)

# תפריט ראשי - while True שרץ עד שבוחרים Exit
while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Show 5.Admin View 6.Exit")
    choice = input("Choose: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        show_account()
    elif choice == "5":
        show_all_accounts()
    elif choice == "6":
        break
