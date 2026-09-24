import hashlib 

text = input ("Enter the text : ") 

hash_value = hashlib.sha256(text.encode()).hexdigest() 

print("\nOriginal Text : ", text)
print("SHA-256 Hash : ", hash_value)