def manual_startswith(text, prefix):
    if not prefix:
        return True
    # If the prefix is longer than the text, it can't match
    if len(prefix) > len(text):
        return False
    # Slice the text from index 0 to the length of the prefix
    beginning_text = text[0:len(prefix)]
    # Compare the slice to the prefix
    return beginning_text == prefix

print(f"Match: {manual_startswith('Python Programming', 'Pyth')}") # True
print(f"No Match: {manual_startswith('Hello', 'Heaven')}")         # False
print(f"Case Sensitivity: {manual_startswith('Apple', 'app')}")    # False
