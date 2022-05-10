# substitution_cipher_atbash
 
from microbit import *
 
# Atbash cipher.
def scrambled_alphabet(text):
    alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789:,{}'"
    crypta = "ZIAWVUTSRJPBNMLKQYHGFEDCOX 345169872,':}{"
    result = ""
 
    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]
 
    return result
 
# The script starts executing statements from here.
 
sleep(1000)
 
print("Set your keyboard to CAPS LOCK.")
print()
 
while True:
    plaintext = input("Enter a CAPS LOCK string: ")
    
    result = scrambled_alphabet(plaintext)
 
    print("result =", result)