num1 = float(input("Please enter your divident: ")) # variable
num2 = float(input("Please enter your divisor: "))
if num2 == 0: #condition if he try to enter a zero on divisor this will print
    print("Invalid you cannot divide a zero")
else: 
    quotient = int(num1 // num2) #condition so that it print a number without any decimal
print(f"The quotient between {num1} and {num2} is {quotient}")