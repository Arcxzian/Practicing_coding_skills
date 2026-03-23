def print_between():
    try:
        start = int(input("Enter your first number: "))
        end = int(input("Enter your second number: "))
        
        low = min(start, end)
        high = max(start, end)
        
        print(f"\nNumbers between {low} and {high}: ")
        
        for i in range(low + 1, high):
            print(i, end=" ")
        if low + 1 >= high:
            print("no integer between the numbers")
            
    except ValueError:
        print("Invalid input, Make sure you input an integer")
        
if __name__ == "__main__":
    print_between()