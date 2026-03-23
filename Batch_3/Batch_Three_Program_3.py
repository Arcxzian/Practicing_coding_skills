# A set to keep track of every unique number entered
seen_numbers = set()

print("Enter numbers one by one. Input any non-numeric value to stop.")

while True:
    user_input = input("Enter a number: ")
    
    try:
        # Try to convert input to a number
        current_number = float(user_input)
        
        # Check if we've seen this number before
        if current_number in seen_numbers:
            print("-> Duplicate")
        else:
            print("-> Unique")
            # Add the new number to our 'memory'
            seen_numbers.add(current_number)
            
    except ValueError:
        # If the input isn't a number, the loop breaks
        print(f"\n'{user_input}' is not a valid number. Program finished.")
        break