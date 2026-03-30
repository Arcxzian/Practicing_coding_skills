text = input("Enter a text: ")
suffix = input("Enter your suffix: ")
if text[-len(suffix):] == suffix:
    print("True")
else:
    print("False")