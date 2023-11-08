import  math

def sine(a):
    return math.sin(a)
    
def cosine(a):
    return math.cos(a)

def tangent(a):
    return math.tan(a)
  
def menu():
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")

choice = int(input("Enter choice: "))
    return choice

def perform_operation(choice):
   elif choice == 9:
        a = float(input("Enter angle in radians: "))
        print("Result: ", sine(a))

   elif choice == 10:
        a = float(input("Enter angle in radians: "))
        print("Result: ", cosine(a))

   elif choice == 11:
        a = float(input("Enter angle in radians: "))
        print("Result: ", tangent(a))

def main():
    while True:
        choice = menu()
        perform_operation(choice)

if name == "main":
   main()
