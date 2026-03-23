
numbers = []

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter a number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value")
            
unique_numbers = [n for n in numbers if numbers.count(n) == 1]

print("\nNumbers With no duplicates: ")
if unique_numbers:
    print(unique_numbers)
else:
    print("No unique numbers found; all numbers were duplicates!")
        
