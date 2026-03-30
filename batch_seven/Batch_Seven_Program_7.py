def manual_zfill(text, width):
    padding_needed = width - len(text)
    
    # If it's already long enough, just return it
    if padding_needed <= 0:
        return text
    
    # Check for leading signs (+ or -)
    if text.startswith(("+", "-")):
        # Place zeros AFTER the sign: Sign + Zeros + Rest of string
        return text[0] + ("0" * padding_needed) + text[1:]
    
    # Otherwise, just add zeros to the front
    return ("0" * padding_needed) + text

# Testing
print(manual_zfill("42", 5))       # "00042"
print(manual_zfill("-42", 5))      # "-0042" (The sign stays at the front!)
print(manual_zfill("+7", 3))       # "+07"