import math

# Función que realiza una suma de dos números
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def quotient(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a // b
    
def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b

def root(a, b):
    if b < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return a ** (1/b)

    
    
# Función que muestra un menú de operaciones y devuelve la elección del usuario
def menu():
    print("Select operation:")
    print("1. Suma")
    print("2. resta")
    print("3. Multiplicación")
    print("4. division")
    print("5. Cuociente")
    print("6. resto ")
    print("7. Potencia")
    print("8. raiz")


    choice = int(input("Enter choice: "))  # Solicita al usuario que ingrese la elección y la convierte a un entero
    return choice

# Función que realiza la operación seleccionada por el usuario
def perform_operation(choice):
    if choice == 1:

        a = float(input("Enter first number: "))  # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: "))  # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", add(a, b))  # Realiza la suma de los dos números y muestra el resultado
        

def perform_operation(choice):
    if choice == 2:
        a = float(input("Enter first number: ")) # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", subtract(a, b)) # Realiza la resta de los dos números y muestra el resultado

    elif choice == 3:
        a = float(input("Enter first number: ")) # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", multiply(a, b)) # Realiza la multipliccion de los dos números y muestra el resultado

    elif choice == 4:
        a = float(input("Enter first number: "))  # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", divide(a, b)) # Realiza la division  de los dos números y muestra el resultado


    elif choice == 5:
        a = float(input("Enter first number: "))  # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", quotient(a, b)) # Realiza el cuociente de los dos números y muestra el resultado


    elif choice == 6:
        a = float(input("Enter first number: "))# Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: "))# Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", remainder(a, b)) # Calcula el resto  y muestra el resultado


    elif choice == 7:
        a = float(input("Enter base: ")) # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter exponent: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", power(a, b))  # Realiza la potencia de los dos números y muestra el resultado


    elif choice == 8:
        a = float(input("Enter number: ")) # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter root: ")) # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", root(a, b)) # Calcula la raiz del numero 


# Función principal del programa

def main():
    while True:
        choice = menu()  # Muestra el menú y obtiene la elección del usuario
        perform_operation(choice)  # Realiza la operación seleccionada por el usuario

if __name__ == "__main__":
    main()  # Inicia la ejecución del programa llamando a la función principal 'main'


