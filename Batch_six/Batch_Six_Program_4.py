def manual_upper(text):
    has_letter = False
    for char in text :
        if 'a' <= char <= 'z':
            return False
        
        if 'A' <= char <= 'Z':
            has_letter = True 
        return has_letter
print(manual_upper("hello!"))
print(manual_upper("I MISS YOU!"))
print(manual_upper("sinta"))
print(manual_upper("BLUE"))