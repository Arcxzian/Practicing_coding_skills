text = input("Enter your text: ")
width = int(input("Enter the width: "))
if len(text) < width:
    text += " " * (width - len(text))
print(text)