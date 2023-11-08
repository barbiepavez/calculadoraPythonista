import  math

def sine(a):
    return math.sin(a)
  
def menu():
    print("9. Seno")

choice = int(input("Enter choice: "))
    return choice

def perform_operation(choice):
   elif choice == 9:
        a = float(input("Enter angle in radians: "))
        print("Result: ", sine(a))
def main():
    while True:
        choice = menu()
        perform_operation(choice)

if name == "main":
   main()
