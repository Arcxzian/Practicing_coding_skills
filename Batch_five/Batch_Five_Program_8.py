fullname = input("Enter Your Fullname: ")
count = 0
for char in fullname:
    if char.isalpha():
        count += 1
        
        print(count)