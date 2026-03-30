def manual_cut(s, p):
    # If the first 'n' characters of s match p, cut them off
    if s[:len(p)] == p:
        return s[len(p):]
    return s

# Test
print(manual_cut("Prog02_Data", "Prog02_")) # Output: Data