num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
if num2 == 0:
    print("Division by zero is undefined")
else:
    remainder = num1 % num2
    
    print(f"The remainder when {num1} is divided by {num2} is {remainder}")