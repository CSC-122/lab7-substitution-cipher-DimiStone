# CSC 122
# Substitution Cipher
# By <Your Name>

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
def convertMessage(message):
    encryptedMessage = ""

    for i in range(len(message)):
        asciiNum = ord(message[i])
        character = chr(asciiNum + 3)
        encryptedMessage += character

    return encryptedMessage

def decodeMessage(decodeThis):
    decodedMessage = ""

    for i in range(len(decodeThis)):
        asciiNum = ord(decodeThis[i])
        character = chr(asciiNum - 3)
        decodedMessage += character

    return decodedMessage

def main():
    message = input("Enter the message to be encrypted: ")
    encryptedMessage = convertMessage(message)

    print(f"Encrypted message = {encryptedMessage}\n")

    decodeThis = input("Enter the cipher to be decrypted: ")
    decodedMessage = decodeMessage(decodeThis)

    print(f"Decrypted message = {decodedMessage}\n")

if __name__ == '__main__':
    main()
