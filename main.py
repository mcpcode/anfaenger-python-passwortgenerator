import random
# --- Variablen
# 1. Buchstaben/Characters, 2. Zahlen, 3. Sonderzeichen
numberOfDigits = 0
passwordLetters = ['A','B','C','D','E','F','G','a','b','c','d','e','f','g']
specialCharacters = ['§', '&', '#', '$']

myPassword = []
finalPassword = ""
# --- Ende Variablen


numberOfDigits = input("Wie viele Zahlen soll das Passwort haben? ")

for i in range(0, int(numberOfDigits)):
    myPassword.append(str(random.randint(0,9)))
myPassword.append(specialCharacters[random.randint(0,len(specialCharacters)-1)])
myPassword.append(passwordLetters[random.randint(0,len(passwordLetters)-1)])
finalPassword = "".join(myPassword)

print("Mein Passwort: ")
print(finalPassword)
