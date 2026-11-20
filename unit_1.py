import math


def student_information():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = [float(input(f"Enter marks for subject {i + 1}: ")) for i in range(3)]
    total = sum(marks)
    average = total / len(marks)
    print(f"\nStudent Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Total Marks: {total:.2f}")
    print(f"Average: {average:.2f}")


def scientific_calculator():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print(f"Addition: {number1 + number2}")
    print(f"Subtraction: {number1 - number2}")
    print(f"Multiplication: {number1 * number2}")
    print(f"Division: {number1 / number2 if number2 != 0 else 'Cannot divide by zero'}")
    print(f"Power: {number1 ** number2}")
    print(f"Modulo: {number1 % number2 if number2 != 0 else 'Undefined'}")


def mathematical_calculator():
    number = float(input("Enter a number: "))
    print(f"Square root: {math.sqrt(number)}")
    print(f"Absolute value: {abs(number)}")
    print(f"Rounded value: {round(number)}")
    print(f"Floor: {math.floor(number)}")
    print(f"Ceiling: {math.ceil(number)}")
    print(f"Factorial: {math.factorial(int(number)) if number >= 0 and number.is_integer() else 'Not applicable'}")
    print(f"Sine: {math.sin(math.radians(number))}")
    print(f"Cosine: {math.cos(math.radians(number))}")
    print(f"Logarithm (base 10): {math.log10(number)}")


def electricity_bill():
    customer_name = input("Enter customer name: ")
    units = int(input("Enter units consumed: "))

    if units <= 100:
        amount = units * 5
    elif units <= 200:
        amount = 100 * 5 + (units - 100) * 7
    else:
        amount = 100 * 5 + 100 * 7 + (units - 200) * 10

    print(f"\nCustomer Name: {customer_name}")
    print(f"Units Consumed: {units}")
    print(f"Bill Amount: Rs. {amount:.2f}")


def main():
    programs = {
        "1": ("Student Information and Academic Summary", student_information),
        "2": ("Scientific Calculator for Two Numbers", scientific_calculator),
        "3": ("Mathematical Calculator using Built-in Functions and Math Module", mathematical_calculator),
        "4": ("Electricity Bill Generator", electricity_bill),
    }

    while True:
        print("\nUNIT 1")
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
