import string 

password = input("Enter your password: ") 

score = 0 

if len(password) >= 8:
    score += 1 
    if any(char.isupper() for char in password):
        score += 1 
    if any(char.islower() for char in password):
        score += 1 
    if any(char.isdigit() for char in password):
        score += 1 
    if any(char in string.punctuation for char in password):
        score += 1 

print(f"Password strength: {score}/5")

if score == 5:
    print("Password is strong")
elif score == 4:
    print("Password is medium")
elif score == 3:
    print("Password is weak")
else:
    print("Password is very weak")
    