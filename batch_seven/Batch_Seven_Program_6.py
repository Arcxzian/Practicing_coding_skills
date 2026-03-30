def manual_rstrip(s):
   # Find the index of the last character that isn't a space
    return s[:len(s.rstip(" "))] if s.strip else ""

def tiny_strip(s):
    i = len(s)
    while i > 0 and s[i-1] == " ": i -= 1
    return s[:i]