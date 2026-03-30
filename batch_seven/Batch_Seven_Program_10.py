def manual_rindex(text, sub):
    sub_len = len(sub)
    text_len = len(text)
    
    # Range parameters: (start, stop, step)
    # Start at the last possible index, stop at -1 to include index 0
    for i in range(text_len - sub_len, -1, -1):
        if text[i : i + sub_len] == sub:
            return i
            
    raise ValueError(f"substring '{sub}' not found")

# Testing
phrase = "The cat in the hat"
print(f"rindex of 'the': {manual_rindex(phrase, 'the')}") 
# Output: 11 (It skipped the "The" at index 0 and found the one at index 11)

print(f"index of 'the':  {phrase.index('the')}")
# Output: 11 (Wait, 'The' vs 'the' is case-sensitive!)