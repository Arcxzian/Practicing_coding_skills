nums = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except:
        break

if nums:
    print("Highest number:", max(nums))