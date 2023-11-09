import  math

def sine(a):
    return math.sin(a)
    
def cosine(a):
    return math.cos(a)

def tangent(a):
    return math.tan(a)
# Función que calcula logaritmo de un numero de base b 
def logarithm(a, b):
    return math.log(a, b)
  
def menu():
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")
    print("12. Logaritmo")

    choice = int(input("Enter choice: "))
    return choice

def perform_operation(choice):

    if choice == 9:
        a = float(input("Enter angle in radians: "))
        print("Result: ", sine(a))

    elif choice == 10:
        a = float(input("Enter angle in radians: "))
        print("Result: ", cosine(a))

    elif choice == 11:
        a = float(input("Enter angle in radians: "))
        print("Result: ", tangent(a))

    elif choice == 12:
        a = float(input("Enter number: ")) # Solicita al usuario que ingrese un nuemero
        b = float(input("Enter base: ")) # Solicita al usuario que ingrese un numero para la bese 
        print("Result: ", logarithm(a, b)) # calcula el logaritmo 


def main():
    while True:
        choice = menu()
        perform_operation(choice)

if __name__ == "__main__":
    main() 

