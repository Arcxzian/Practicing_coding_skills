# print("Program One")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if num1 > num2:
#     print(f"The bigger number is {num1}")
# elif num1 < num2:
#     print(f"The bigger number is {num2}")
# else:
#     print("Retry both numbers are equal")
    
# print("Program Two")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if num1 == num2:
#     print(f"Both numbers are equal")
# else:
#     print(f"Retry, both numbers must be equal")

# print("Program Three")
# num1 = float(input("Enter First Number: "))
# num2 = float(input("Enter Second number:"))
# if num1 + num2:
#     print(f"The sum of {num1} and {num2} is {num1 + num2}")
# else:
#     print("Retry, both numbers must be greater than zero")

# print("Program Four")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# product = num1 * num2
# print(f"The product of {num1} and {num2} is {product}")

# print("Program Five")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# quotient = num1 / num2
# print(f"The quotient of {num1} and {num2} is {quotient}")

# print("Program Six")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = num1 ** num2
# print(f"The result of {num1} raised to the power of {num2} is {result}")

print("Program Seven")
total_sum = 0
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    
    total_sum = total_sum + num
    
    
print(f"The total sum of all 10 numbers is {total_sum}")