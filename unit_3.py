def contact_book():
    contacts = {}

    while True:
        print("\n1. Add Contact  2. Search  3. Display  4. Delete  0. Back")
        choice = input("Choose an option: ")
        if choice == "0":
            break
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            contacts[name] = phone
            print("Contact added.")
        elif choice == "2":
            name = input("Enter name to search: ")
            print(f"Phone: {contacts[name]}" if name in contacts else "Contact not found.")
        elif choice == "3":
            if contacts:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts.")
        elif choice == "4":
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted.")
            else:
                print("Contact not found.")
        else:
            print("Invalid choice.")


def student_grading():
    marks = []
    count = int(input("Enter number of subjects: "))
    for subject in range(1, count + 1):
        marks.append(float(input(f"Marks for subject {subject}: ")))

    average = sum(marks) / count
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def frequency_counter():
    text = input("Enter text: ")
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1

    for character, count in frequencies.items():
        print(f"{character!r}: {count}")


def attendance_tracker():
    students = {}
    count = int(input("Enter number of students: "))

    for _ in range(count):
        name = input("Student name: ").strip()
        status = input("Present or absent (P/A): ").strip().upper()
        students[name] = "Present" if status == "P" else "Absent"

    print("\nAttendance Report")
    present_count = sum(status == "Present" for status in students.values())
    for name, status in students.items():
        print(f"{name}: {status}")
    print(f"Present: {present_count}")
    print(f"Absent: {count - present_count}")


def main():
    programs = {
        "1": ("Simple Contact Book using Lists and Dictionaries", contact_book),
        "2": ("Student Grading System", student_grading),
        "3": ("Frequency Counter using Dictionaries", frequency_counter),
        "4": ("Attendance Tracker", attendance_tracker),
    }

    while True:
        print("\nUNIT 3")
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
