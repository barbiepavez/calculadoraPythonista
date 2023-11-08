import  math

def sine(a):
    return math.sin(a)
    
def cosine(a):
    return math.cos(a)
  
def menu():
    print("9. Seno")
    print("10. Coseno")

    choice = int(input("Enter choice: "))
    return choice

def perform_operation(choice):
   if choice == 9:
        a = float(input("Enter angle in radians: "))
        print("Result: ", sine(a))

   elif choice == 10:
        a = float(input("Enter angle in radians: "))
        print("Result: ", cosine(a))

def main():
    while True:
        choice = menu()
        perform_operation(choice)

if name == "main":
   main()
