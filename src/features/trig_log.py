import  math

# Función que calcula el seno de un numero
def sine(a):
    return math.sin(a)
# Función que calcula el coseno de un numero    
def cosine(a):
    return math.cos(a)

def tangent(a):
    return math.tan(a)

def logarithm(a, b):
    return math.log(a, b)
    
# Función que muestra un menú de operaciones y devuelve la elección del usuario
def menu():
def menu():
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")
    print("12. Logaritmo")

    choice = int(input("Enter choice: ")) # Solicita al usuario que ingrese la elección y la convierte a un entero
    return choice

# Función que realiza la operación seleccionada por el usuario
def perform_operation(choice):

    if choice == 9:

        a = float(input("Enter angle in radians: ")) # Solicita al usuario que ingrese un angulo en radianes
        print("Result: ", sine(a)) # calcula el seno del numero

    elif choice == 10:
        a = float(input("Enter angle in radians: ")) # Solicita al usuario que ingrese un angulo en radianes
        print("Result: ", cosine(a)) # calcula el coseno del numero

    elif choice == 11:
        a = float(input("Enter angle in radians: "))
        print("Result: ", tangent(a))

    elif choice == 12:
        a = float(input("Enter number: "))
        b = float(input("Enter base: "))
        print("Result: ", logarithm(a, b))

# Función principal del programa

def main():
    while True:
        choice = menu()  # Muestra el menú y obtiene la elección del usuario
        perform_operation(choice)# Realiza la operación seleccionada por el usuario


if __name__ == "__main__":
    main()  # Inicia la ejecución del programa llamando a la función principal 'main'

