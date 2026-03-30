text = "Hello"
width = 20
left_padding = (width - len(text)) // 2
centered = (" " * left_padding) + text
centered = centered.ljust(width)
print(f"'{centered}'")