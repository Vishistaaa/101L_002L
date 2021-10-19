# Name : Vishista Vuppulapati
# Week 6 Program : Caesar Cipher 
# Student ID : 16324243
# UMKC email ID : vvd94@umsystem.edu

# A python program to play Caesar Cipher Game.

#####################################################################################
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if char == ' ':
            result += " "
            continue
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result.upper()

def decrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        if char == ' ':
            result += " "
            continue
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result.upper()

#Driver code

print("MAIN MENU:")
print("1) Encode a string")
print("2) Decode a string")
print("Q) Quit")
print("Enter your selection ==>", end=" ")
choice = input()

while(choice != 'Q'):
    if choice == '1':
        print("\nEnter (brief) text to encrypt:",end=" ")
        text = input()
        shift = int(input("Enter the number of shifts letter by: "))
        encrypt_text = encrypt(text,shift)
        print("Encrypted: "+encrypt_text)
        
    if choice == '2':
        print("\nEnter (brief) text to decrypt:",end=" ")
        text = input()
        shift = int(input("Enter the number of shifts letter by: "))
        decrypt_text = decrypt(text,shift)
        print("Decrypted: "+decrypt_text)
        
    print("\nMAIN MENU:")
    print("1) Encode a string")
    print("2) Decode a string")
    print("Q) Quit")
    print("Enter your selection ==>", end=" ")
    choice = input() 
    
    #################################################################################