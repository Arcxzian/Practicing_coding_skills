num1 = float(input("Enter the first number: ")) # varible
num2 = float(input("Enter the second number: ")) 

if num1 > num2: # checking if number 1 is bigger than number 2
    print(f"the large number is {num1}")
elif num2 > num1: # same condition with line 4
    print(f"the large number is {num2}")
else:
    print("both numbers are equal")