from collections import Counter

numbers = []
while True:
    try:
        numbers.append(float(input("Enter a number: ")))
    except ValueError:
        break

if numbers:
    # Counter(numbers).most_common(1) returns [(number, count)]
    most_common, count = Counter(numbers).most_common(1)[0]
    print(f"Most frequent: {most_common} (appeared {count} times)" if count > 1 else "No duplicates.")