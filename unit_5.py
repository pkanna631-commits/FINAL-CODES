import csv
import random
from pathlib import Path


class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited: {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount:.2f}")

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}")


def bank_account_system():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(name, account_number, balance)

    while True:
        print("\n1. Deposit  2. Withdraw  3. Display  0. Back")
        choice = input("Choose an option: ")
        if choice == "0":
            break
        if choice == "1":
            account.deposit(float(input("Deposit amount: ")))
        elif choice == "2":
            account.withdraw(float(input("Withdrawal amount: ")))
        elif choice == "3":
            account.display()
        else:
            print("Invalid choice.")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = {"author": author, "available": True}

    def issue_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif not self.books[title]["available"]:
            print("Book is already issued.")
        else:
            self.books[title]["available"] = False
            print("Book issued successfully.")

    def return_book(self, title):
        if title in self.books:
            self.books[title]["available"] = True
            print("Book returned successfully.")
        else:
            print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for title, details in self.books.items():
            status = "Available" if details["available"] else "Issued"
            print(f"{title} - {details['author']} ({status})")


def library_management():
    library = Library()

    while True:
        print("\n1. Add Book  2. Issue  3. Return  4. Display  0. Back")
        choice = input("Choose an option: ")
        if choice == "0":
            break
        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            library.add_book(title, author)
        elif choice == "2":
            library.issue_book(input("Book title: "))
        elif choice == "3":
            library.return_book(input("Book title: "))
        elif choice == "4":
            library.display_books()
        else:
            print("Invalid choice.")


def dice_simulator():
    count = int(input("Enter number of dice rolls: "))
    for _ in range(count):
        print(random.randint(1, 6), end=" ")
    print()


def retail_sales_dashboard():
    filename = "sales.csv"

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib is not installed.")
        return

    if not Path(filename).exists():
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product", "Sales"])
            writer.writerow(["Mobile", 120])
            writer.writerow(["Laptop", 95])
            writer.writerow(["Tablet", 70])
            writer.writerow(["Headphones", 150])
            writer.writerow(["Keyboard", 60])

    products = []
    sales = []
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row["Product"])
            sales.append(float(row["Sales"]))

    plt.figure(figsize=(8, 5))
    plt.bar(products, sales, color="skyblue")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.title("Retail Sales Dashboard")
    plt.tight_layout()
    plt.show()


def main():
    programs = {
        "1": ("Bank Account System using OOP", bank_account_system),
        "2": ("Library Management System", library_management),
        "3": ("Dice Simulator using Random Module", dice_simulator),
        "4": ("Retail Sales Dashboard using CSV and Matplotlib", retail_sales_dashboard),
    }

    while True:
        print("\nUNIT 5")
        for key, (name, _) in programs.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Choose a program: ")
        if choice == "0":
            break
        if choice in programs:
            programs[choice][1]()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
