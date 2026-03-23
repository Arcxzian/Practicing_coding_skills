nums = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except:
        break

if nums:
    print("Average:", sum(nums) / len(nums))
else:
    print("No numbers were entered.")