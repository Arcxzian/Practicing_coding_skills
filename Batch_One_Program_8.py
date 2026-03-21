count_odd = 0

for i in range(10): # limit to 10 
    num = int(input(f"enter 10 numbers {i+1}: "))
    
    num = num + 11 
     
    if num % 2 != 0: #condition to know if the number is odd
        count_odd += 1
     
print("the total of the odd number is: ", {count_odd}) # printing 
