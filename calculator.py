#python simple calculator

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2st number: "))
operator = input("Enter operator (+ - * /): ")

if operator == "+" :
    result = num1 + num2
    print(round(result,3))

elif operator == "-":
    result = num1 - num2
    print(round(result,3))

elif operator == "/":
    result = num1 / num2
    print(round(result,3))

elif operator == "*":
    result = num1 * num2
    print(round(result,3))

else:
    print(f"{operator} is invalid operator!")