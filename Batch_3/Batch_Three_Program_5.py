numbers = []

print("Enter a number. Input any non numeric value to stop the program")

while True:
    user_input = input("Enter a number: ")
    
    try:
        current_numbers = float(user_input)
        numbers.append (current_numbers)
        
    except ValueError:
        print(f"\n '{user_input}' is not a valid number. sorting results...")
        break
    
    if numbers: 
        numbers.sort()
                
    print("Numbers from highest to lowest")
    print(numbers)  
else:
    print("Invalid no number were entered.")