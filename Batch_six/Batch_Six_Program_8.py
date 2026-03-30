text = "Hello Niggas!"
result = ""
for char in text:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)