alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUYWXYZabcdefghijklmopqrstuvwxyzАБВГДЕЄЖЗИІЇйКЛМНОПРСТУФЧЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцшщбюяАБВГДЕЄЖЗИІЇйКЛМНОПРСТУФЧЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцшщбюя01234567890123456789"

cipher = input("Enter your text: ")
key = int(input("Enter key (1-25): "))
ciphered = ""
for letter in cipher:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        ciphered = ciphered + alphabet[newPosition]
    else:
        ciphered = ciphered + letter
print("Your ciphered word: ", ciphered)