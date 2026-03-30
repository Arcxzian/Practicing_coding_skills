text = "i lOVE pYTHON"
words = text.split()
capitalized_words = [word[0].upper() + word[1:].lower() for word in words]
result = " ".join(capitalized_words) 
print(result)