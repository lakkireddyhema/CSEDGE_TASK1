print("select operation")
print("1:Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4:Division")
def calculator():
    choice = input("enter your choice (1/2/3/4):")
    if choice in ["1", "2", "3", "4"]:
        n1 = float(input("enter first number:"))
        n2 = float(input("enter second number:"))
        if choice == '1':
            result = n1 + n2
            print(f"{n1} + {n2}={result}")
        elif choice == "2":
            result = n1 - n2
            print(f"{n1} - {n2}={result}")
        elif choice == "3":
            result = n1 * n2
            print(f"{n1} * {n2}={result}")
        elif choice == "4":
            result = n1 / n2
            print(f"{n1} / {n2}={result}")
        else:
            print("invalid input")
while True:
     u = input("Do you want to continue (y/n):")
     if u=="y" or u=="Y":
          calculator()
     elif u=="n" or u=="N":
         print("exit")
         break





