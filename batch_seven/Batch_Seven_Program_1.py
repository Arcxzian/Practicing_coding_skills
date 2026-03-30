def manual_rstrip(text):
    # Handle empty strings or strings with only spaces
    if not text or text.isspace():
        return ""

    # Start at the last index
    i = len(text) - 1
    
    # Move 'i' backwards while the character at text[i] is a space
    while i >= 0 and text[i] == " ":
        i -= 1
        
    # Slice from the start up to i + 1 (since slicing is exclusive)
    return text[:i + 1]

# Testing it out
original = "maangas     "
stripped = manual_rstrip(original)

print(f"Original: '{original}'")
print(f"Stripped: '{stripped}'")
print(f"Length saved: {len(original) - len(stripped)} characters")