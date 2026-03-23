numbers = []
seen = set()
result = []

print("Please enter 10 numbers: ")

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter a number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("invalid please enter a numerical number.")
        
for n in numbers:
    if n not in seen:
        result.append(n)
        seen.add(n)
        
print("\nNumbers (duplicates removed, first entries kept):")
print(result) 