numbers = []

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter a number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invald please input a numerical number")
            
same_numbers = [n for n in numbers if numbers.count(n) == 2]

print("\nNumbers With Duplicates")
if same_numbers:
    print(same_numbers)
else:
    print("All numbers were duplicate, No unique numbers found!")