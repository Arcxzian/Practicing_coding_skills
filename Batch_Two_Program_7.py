# Prog07: Count even numbers from 10 inputs
print("--- Even Number Counter (10 Numbers) ---")

# Step 1: Initialize a counter to keep track of even numbers
even_count = 0

# Step 2: Use a loop to ask for 10 inputs
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    
    # Step 3: Check if the number is even
    # A number is even if it is divisible by 2 with 0 remainder
    if num % 2 == 0:
        even_count += 1

# Step 4: Display the final count
print("-" * 30)
print(f"Total even numbers entered: {even_count}")