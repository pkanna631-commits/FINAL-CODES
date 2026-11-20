import random


def check_prime():
    number = int(input("Enter a number: "))
    if number < 2:
        print("Not a prime number.")
        return

    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    print("Prime number." if is_prime else "Not a prime number.")


def factorial():
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    result = 1
    for value in range(1, number + 1):
        result *= value
    print(f"Factorial of {number} is {result}")


def generate_otp():
    digits = int(input("Enter OTP length: "))
    otp = "".join(str(random.randint(0, 9)) for _ in range(digits))
    print(f"Generated OTP: {otp}")


def fibonacci_iterative():
    count = int(input("Enter number of terms: "))
    if count <= 0:
        print("Please enter a positive number.")
        return

    first, second = 0, 1
    for _ in range(count):
        print(first, end=" ")
        first, second = second, first + second
    print()


def fibonacci_recursive():
    def fibonacci(number):
        if number <= 1:
            return number
        return fibonacci(number - 1) + fibonacci(number - 2)

    count = int(input("Enter number of terms: "))
    if count <= 0:
        print("Please enter a positive number.")
        return

    for number in range(count):
        print(fibonacci(number), end=" ")
    print()


def main():
    programs = {
        "1": ("Checking whether a number is prime", check_prime),
        "2": ("Factorial of a number", factorial),
        "3": ("OTP Generator", generate_otp),
        "4": ("Fibonacci Series", fibonacci_iterative),
        "5": ("Fibonacci Series using Recursion", fibonacci_recursive),
    }

    while True:
        print("\nUNIT 2")
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
