# Calculadora Pythonista

## Descripción

Este proyecto consiste en el desarrollo de una calculadora con operaciones básicas, funciones trigonométricas y logaritmos utilizando un flujo de trabajo de Git con las ramas Main, Hotfix, Release, Develop y Features.

## Requisitos

* Git instalado en tu computadora.
* Una cuenta de [Github](https://github.com/)

## Pasos 

* Clona el repositorio en tu computadora.
* Abre el archivo en tu entorno de desarrollo.
* Utiliza los métodos disponibles para realizar cálculos.

## Uso de la Calculadora

1. Ejecución

   - Asegúrate de tener Python instalado en tu computadora.
   - Se mostrará un menú de operaciones y deberás seleccionar la opción deseada ingresando el número correspondiente.
   - 
## Código operaciones básicas


import math

# Función que realiza una suma de dos números
def add(a, b):
    return a + b

# Función que realiza una resta de dos números
def subtract(a, b):
    return a - b
# Función que realiza la multiplicación  de dos números
def multiply(a, b):
    return a * b
# Función que realiza la division  de dos números
def divide(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b
# Función que realiza el cuocinte de dos números
def quotient(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a // b
# Función que calcula el resto
def remainder(a, b):
    return a % b
# Función que calcula la potencia  de dos números
def power(a, b):
    return a ** b
# Función que calcula la raiz
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


2. Datos de entrada y salida:

   - Suma: Ingresa dos números y la calculadora mostrará el resultado de la suma.
   - Resta: Ingresa dos números y la calculadora mostrará el resultado de la resta.
   - Multiplicación: Ingresa dos números y la calculadora mostrará el resultado de la multiplicación.
   - División: Ingresa dos números y la calculadora mostrará el resultado de la división. Si el divisor es cero, se mostrará un mensaje de error.
   - Cociente: Ingresa dos números y la calculadora mostrará el cociente de la división entera.
   - Resto: Ingresa dos números y la calculadora mostrará el resto de la división entera.
   - Potencia: Ingresa dos números y la calculadora mostrará el resultado de elevar el primer número a la potencia del segundo número.
   - Raíz: Ingresa un número y la calculadora mostrará la raíz cuadrada de ese número.

## Código operaciones avanzadas




3. Funciones trigonométricas y logaritmos

   - Seno: Ingresa un ángulo en radianes y la calculadora mostrará el seno de ese ángulo.
   - Coseno: Ingresa un ángulo en radianes y la calculadora mostrará el coseno de ese ángulo.
   - Tangente: Ingresa un ángulo en radianes y la calculadora mostrará la tangente de ese ángulo.
   - Logaritmo: Ingresa un número y la base del logaritmo, y la calculadora mostrará el logaritmo de ese número en esa base.


## Contribucción

Si deseas contribuir a este proyecto, sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con el nombre descriptivo de tu contribución.
3. Realiza tus cambios y pruebas.
4. Envía un pull request explicando tus cambios.

## Contacto 

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi perfil de GitHub.

