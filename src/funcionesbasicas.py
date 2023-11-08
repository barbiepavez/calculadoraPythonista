import math
def add(a, b):
    return a + b

def menu():
    print("Select operation:")
    print("1. Suma")

    choice = int(input("Enter choice: "))
    return choice

def perform_operation(choice):
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", add(a, b))
def main():
    while True:
        choice = menu()
        perform_operation(choice)

if __name__ == "__main__":
    main() 

