#Convert name to PascalCase
fullname = input("Enter your full name (any casing): ")

# 1. .title() converts "jUAn DEla CrUZ" to "Juan Dela Cruz"
proper_casing = fullname.title()

# 2. .replace(" ", "") removes all spaces
pascal_case = proper_casing.replace(" ", "")

print("Output:", pascal_case)