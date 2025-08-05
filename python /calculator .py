
#Ask for user input
num1 = int(input("Enter the first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 =int(input("Enter the second number: "))
#Perform operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

print (result)
print(f"{num1} {operation} {num2} = {result}")


