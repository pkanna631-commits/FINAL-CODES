import csv
from pathlib import Path


def log_file_reader():
    filename = input("Enter log filename (or press Enter for sample.log): ").strip()
    filename = filename or "sample.log"
    path = Path(filename)

    if not path.exists():
        print("Log file not found.")
        return
    with path.open("r", encoding="utf-8") as log_file:
        for line_number, line in enumerate(log_file, start=1):
            print(f"{line_number}: {line.rstrip()}")


def student_data_manager():
    filename = "students.txt"

    while True:
        print("\n1. Add  2. View  3. Search  0. Back")
        choice = input("Choose an option: ")
        if choice == "0":
            break
        if choice == "1":
            name = input("Name: ")
            marks = input("Marks: ")
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"{name},{marks}\n")
            print("Student record saved.")
        elif choice == "2":
            if not Path(filename).exists():
                print("No records found.")
                continue
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read())
        elif choice == "3":
            name = input("Enter name to search: ").lower()
            found = False
            if Path(filename).exists():
                with open(filename, "r", encoding="utf-8") as file:
                    for line in file:
                        record_name, marks = line.strip().split(",", 1)
                        if record_name.lower() == name:
                            print(f"Name: {record_name}, Marks: {marks}")
                            found = True
                            break
            print("Record not found." if not found else "")
        else:
            print("Invalid choice.")


def payroll_management():
    filename = input("Enter CSV filename (or press Enter for payroll.csv): ").strip()
    filename = filename or "payroll.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee", "Basic Salary", "Allowance", "Deduction", "Net Salary"])

        count = int(input("Enter number of employees: "))
        for _ in range(count):
            name = input("Employee name: ")
            basic = float(input("Basic salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))
            net_salary = basic + allowance - deduction
            writer.writerow([name, basic, allowance, deduction, net_salary])

    print(f"Payroll saved to {filename}")
    with open(filename, "r", newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            print(row)


def log_analyzer():
    filename = input("Enter log filename (or press Enter for sample.log): ").strip()
    filename = filename or "sample.log"
    path = Path(filename)

    if not path.exists():
        print("Log file not found.")
        return

    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with path.open("r", encoding="utf-8") as log_file:
        for line in log_file:
            for level in counts:
                if level in line.upper():
                    counts[level] += 1

    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")


def main():
    programs = {
        "1": ("Log File Reader", log_file_reader),
        "2": ("Student Data Manager Using Files", student_data_manager),
        "3": ("CSV Based Payroll Management System", payroll_management),
        "4": ("Log Analyzer", log_analyzer),
    }

    while True:
        print("\nUNIT 4")
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
