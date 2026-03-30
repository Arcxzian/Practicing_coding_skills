def manual_upper(text):
    result = ""
    
    for char in text:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32 )
            result += upper_char
        else:
            result += char 
            
    return result

text_sting = "Python programming maangas"
print(f"original:[text_sting]")
print(f"result:{manual_upper(text_sting)}")      
        