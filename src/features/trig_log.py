import  math

def sine(a):
    return math.sin(a)
    
def cosine(a):
    return math.cos(a)
# Función que calcula la tangente de un numero
def tangent(a):
    return math.tan(a)

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
        a = float(input("Enter angle in radians: "))# Solicita al usuario que ingrese un angulo en radianes
        print("Result: ", tangent(a)) # calcula el seno del numero

    elif choice == 12:
        a = float(input("Enter number: "))
        b = float(input("Enter base: "))
        print("Result: ", logarithm(a, b))


def main():
    while True:
        choice = menu()
        perform_operation(choice)

if __name__ == "__main__":
    main() 

