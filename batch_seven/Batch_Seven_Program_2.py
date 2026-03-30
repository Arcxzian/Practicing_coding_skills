def manual_remove_suffix(text, suffix):
    if not suffix:
        return " "
    if text.endswith(suffix):
        end_index = len(text) - len(suffix)
        return text[:end_index]
    
    return text
word = "PythonProgramming"
result = manual_remove_suffix(word, "programming")

print(f"original: {word}")
print(f"result: {result}")