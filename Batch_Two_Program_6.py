numbers = []

for i in range(1,11):
    val = float(input(f"Enter nunber {i}: "))
    numbers.append(val)

result = numbers[0]

for num in numbers [1:]:
    result -= num
    
print("-" * 30)
print(f"the final result is : {result}")
