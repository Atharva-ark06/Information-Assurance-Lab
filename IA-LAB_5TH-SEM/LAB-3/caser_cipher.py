def encrypt(text,shift): 
    result ="" 
    
    for char in text : 
        if char.isalpha(): 
            
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            
            
        else:
            result += char
    
    return result

def decrypt(text,shift): 
    return encrypt(text, -shift) 

text = input("Enter Plain Text: ") 

shift = int(input("Enter Shift value: ") ) 

cipher=encrypt(text,shift) 
print("Encrypted Text: " , cipher) 

plain =decrypt(cipher,shift)
print("Decrypted Text: " , plain)
