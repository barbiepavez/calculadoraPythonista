import math

# Función que realiza una suma de dos números
def add(a, b):
    return a + b

# Función que muestra un menú de operaciones y devuelve la elección del usuario
def menu():
    print("Select operation:")
    print("1. Suma")

    choice = int(input("Enter choice: "))  # Solicita al usuario que ingrese la elección y la convierte a un entero
    return choice

# Función que realiza la operación seleccionada por el usuario
def perform_operation(choice):
    if choice == 1:
        a = float(input("Enter first number: "))  # Solicita al usuario que ingrese el primer número y lo convierte a un número de punto flotante
        b = float(input("Enter second number: "))  # Solicita al usuario que ingrese el segundo número y lo convierte a un número de punto flotante
        print("Result: ", add(a, b))  # Realiza la suma de los dos números y muestra el resultado

# Función principal del programa
def main():
    while True:
        choice = menu()  # Muestra el menú y obtiene la elección del usuario
        perform_operation(choice)  # Realiza la operación seleccionada por el usuario

if __name__ == "__main__":
    main()  # Inicia la ejecución del programa llamando a la función principal 'main'


