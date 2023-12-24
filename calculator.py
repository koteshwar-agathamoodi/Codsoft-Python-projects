def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("-------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice : ")
    ans = None
    if operation == "1":
        ans = num1 + num2
        print(f"The result of addition is: {ans}")
    elif operation == "2":
        ans = num1 - num2
        print(f"The result of subtraction is: {ans}")
    elif operation == "3":
        ans = num1 * num2
        print(f"The result of multiplication is: {ans}")
    elif operation == "4":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            ans = num1 / num2
            print(f"The result of division is: {ans}")
    else:
        print("Invalid choice, Please try again.")

calculator()
