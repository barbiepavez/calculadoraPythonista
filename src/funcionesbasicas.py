import math
def add(a, b):
    return a + b
    
def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def menu():
    print("Select operation:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")

choice = int(input("enter choice:"))
return choice

def perform_operation(choice):
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", add(a, b))

    if choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", substract(a, b))
    
     elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", multiply(a, b))

        
def main():
    while True:
        choice = menu()
        perform_operation(choice)

if __name__ == "__main__":
    main() 