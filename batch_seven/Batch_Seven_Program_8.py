def manual_count(text, sub):
    if not sub:
        return len(text) + 1
    
    count = 0
    i = 0
    # Loop until we don't have enough characters left for a match
    while i <= len(text) - len(sub):
        # Check if the slice starting at i matches the substring
        if text[i : i + len(sub)] == sub:
            count += 1
            # Move index forward by the length of the substring (non-overlapping)
            i += len(sub)
        else:
            # Move forward by 1 to check the next position
            i += 1
    return count

# Testing
phrase = "banana"
print(f"Count of 'ana': {manual_count(phrase, 'ana')}") 
# Output: 1 (Standard count() does not overlap, so 'ana' is found once)

print(f"Count of 'a':   {manual_count(phrase, 'a')}")   
# Output: 3