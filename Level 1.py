print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Root")
print("6.Square")
while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4','5','6'):
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", (num1+num2))

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", (num1-num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", (num1*num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", (num1/num2))
            
        elif choice in ('5'):
            num = float(input("Enter number: "))
            print("Square root=" , ( num**0.5))
            
        elif choice in ('6'):
            num = float(input("Enter number: "))
            print("Square =" , ( num*num))
        break
    else :
            print("invalid input")
