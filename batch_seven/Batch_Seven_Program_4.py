def manual_islower(text):
    found_alpha = False
    
    for char in text:
        if 'A' <= char <= 'Z':
            return False
        
        if 'a' <= char <= 'z':
            found_alpha = True
            
    return found_alpha

print(f"'hello': {manual_islower('hello')}")
print(f"'Hello: {manual_islower('Hello')}")
print(f"'123': {manual_islower('123')}")
print(f"'maangas' {manual_islower('maangas')}")
        
        