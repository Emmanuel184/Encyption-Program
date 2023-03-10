import sys

PASSKEY = ""
WRITEBACK = ""

mode = sys.stdin.readline().rstrip()

def encryptChar(character: chr, passKeyChar: chr) -> chr:
    
    overflow = (ord(character) + (ord(passKeyChar))) - (97 * 2)
    return chr((overflow % 26) + 97) if  overflow > 25 else chr(overflow + 97)

def decryptChar(character: chr, passKeyChar: chr) -> chr:

    passKeyToZ = ord('z') - ord(passKeyChar)
    aToCharcater = ord(character) - ord('a')
    overflow = (passKeyToZ + aToCharcater) % 26 + 1

    return chr((overflow) % 26 + 97) if overflow > 25 else chr(overflow + 97)

def setPASSKEY(newPASSKEY: str):
    global PASSKEY
    PASSKEY = newPASSKEY[:]

    return "", True

def ENCRYPT(stringToEncrypt: str):

    if PASSKEY == "":
        return "Passkey not set", False 
    
    encryptedString = []

    indexOfPasskey = 0

    for char in stringToEncrypt:

        encryptedString.append(encryptChar(char, PASSKEY[indexOfPasskey]))

        if indexOfPasskey == len(PASSKEY) - 1:
            indexOfPasskey = 0
            continue

        indexOfPasskey += 1
    
    return "".join(encryptedString), True

def DECRYPT(stringToDecrypt: str):
    
    if PASSKEY == "":
        return "Passkey not set", False


    decryptedString = []

    indexOfPasskey = 0

    for char in stringToDecrypt:

        decryptedString.append(decryptChar(char, PASSKEY[indexOfPasskey]))

        if indexOfPasskey == len(PASSKEY) - 1:
            indexOfPasskey = 0
            continue

        indexOfPasskey += 1
    
    return "".join(decryptedString), True

try:
    while mode != "quit":

        if mode == "write":
            WRITE = sys.stdin.readline().rstrip()
            WRITE = WRITE.split(" ")
            command = WRITE[0]
            arguement = "".join(WRITE[1:])

            options = {
                "passkey": setPASSKEY,
                "encrypt": ENCRYPT,
                "decrypt": DECRYPT,
            }
            
            WRITEBACK = options[command](arguement)
        elif mode == "read":

            if WRITEBACK[1]:
                print(f"RESULT {WRITEBACK[0]}\n")
            else:
                print(f"ERROR {WRITEBACK[0]}\n")

            sys.stdout.flush()
        
        mode = sys.stdin.readline().rstrip()
except KeyboardInterrupt:
    exit()

