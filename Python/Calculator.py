# mini calculator

user_input = input("Choose the mathematical operation:\nAddition\nSubtraction\nMultiplication\nDivision\n")

a = int(input("First number: "))
b = int(input("Second number: "))

if user_input == "Addition" or user_input == "add":
    result = a + b
    print(result)

elif user_input == "Subtraction" or user_input == "sub":
    result = a - b
    print(result)

elif user_input == "Multiplication" or user_input == "multi":
    result = a * b
    print(result)

elif user_input == "Division" or user_input == "div":
    if b != 0:
        result = a / b
        print(result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid Option: Please Choose again")
