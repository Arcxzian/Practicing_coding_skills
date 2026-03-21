num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: ")) # variables
if num1 + num2: # condition for summing up the 2 number
    print(f"the sum of {num1} and {num2} is {num1 + num2}")
else: # else it will invalid if you put a letter 
    print("invalid please input a real number")