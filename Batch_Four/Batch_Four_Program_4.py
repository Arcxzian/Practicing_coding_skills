nums = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except:
        break

if nums:
    nums.sort(reverse=True)
    print("Highest to Lowest:", nums)