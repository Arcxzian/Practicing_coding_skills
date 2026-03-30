def manual_index(text, sub):
    sub_len = len(sub)
    text_len = len(text)
    
    # Loop through the string
    # We stop at text_len - sub_len + 1 to avoid slicing past the end
    for i in range(text_len - sub_len + 1):
        # Extract the window
        window = text[i : i + sub_len]
        
        # Check if it matches
        if window == sub:
            return i
            
    # If the loop finishes, the substring wasn't found
    raise ValueError(f"substring '{sub}' not found")

# Testing
try:
    phrase = "Python is fun"
    print(f"Index of 'is': {manual_index(phrase, 'is')}")  # Output: 7
    print(f"Index of 'fun': {manual_index(phrase, 'fun')}") # Output: 10
    print(manual_index(phrase, "Java")) # This will trigger the error
except ValueError as e:
    print(f"Error: {e}")