print("Welcome to Sample Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Choose an Option for Calculator Operation : "))

if option == 1:
    Number1 = int(input("Enter First Number : "))
    Number2 = int(input("Enter Second Number : "))
    Number3 = Number1 + Number2
    print("Addition is : " + str (Number3))

elif option == 2:
    Number1 = int(input("Enter First Number : "))
    Number2 = int(input("Enter Second Number : "))
    Number3 = Number1 - Number2
    print("Subtraction is : " + str (Number3))

elif option == 3:
    Number1 = int(input("Enter First Number : "))
    Number2 = int(input("Enter Second Number : "))
    Number3 = Number1 * Number2
    print("Multiplication is : " + str (Number3))

elif option == 4:
    Number1 = int(input("Enter First Number : "))
    Number2 = int(input("Enter Second Number : "))
    Number3 = Number1 / Number2
    print("Division is : " + str (Number3))
else:
    print("Invalid Number")