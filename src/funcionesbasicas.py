import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def quotient(a, b):
    return a // b
    
def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b

    
def menu():
    print("Select operation:")
    print("1. Suma")
    print("2. resta")
    print("3. Multiplicación")
    print("4. division")
    print("5. Cuociente")
    print("6. resto ")
    print("7. Potencia")

    choice = int(input("Enter choice: "))
    return choice

def perform_operation(choice):
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", add(a, b))

def perform_operation(choice):
    if choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", subtract(a, b))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", multiply(a, b))

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", divide(a, b))

    elif choice == 5:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", quotient(a, b))

    elif choice == 6:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", remainder(a, b))

    elif choice == 7:
        a = float(input("Enter base: ")) # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter exponent: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", power(a, b))  # Realiza la potencia de los dos números y muestra el resultado


def main():
    while True:
        choice = menu()
        perform_operation(choice)

if __name__ == "__main__":
    main() 
