def manual_lower(text):
    result = ""
    for char in text:
        # Check if the character is an uppercase letter (A-Z)
        if 'A' <= char <= 'Z':
            # Add 32 to the ASCII value to get the lowercase version
            lowercase_char = chr(ord(char) + 32)
            result += lowercase_char
        else:
            # If it's already lowercase, a number, or a symbol, keep it as is
            result += char
    return result

# Testing the program
my_string = "HELLO World!"
print(f"Original: {my_string}")
print(f"Manual Lower: {manual_lower(my_string)}")