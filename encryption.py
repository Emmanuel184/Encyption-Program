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
    PASSKEY = newPASSKEY

    return newPASSKEY, True

def ENCRYPT(stringToEncrypt: str) -> tuple[str, bool]:

    if not PASSKEY:
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
    
    if not PASSKEY:
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

def NOCOMMAND():

    return "Not a valid command try again", False

def QUIT(string: str):
    #WRITE TO LOGGER AND EXIT
    exit()

while mode != "QUIT":

    if mode == "WRITE":
        WRITE = sys.stdin.readline().rstrip()
        WRITE = WRITE.split(" ")
        command = WRITE[0]
        arguement = WRITE[1]

        options = {
            "PASSKEY": setPASSKEY,
            "ENCRYPT": ENCRYPT,
            "DECRYPT": DECRYPT,
            "QUIT": QUIT
        }

        WRITEBACK = options[command](arguement)
    else:
        print(f"{f'RESULT {WRITEBACK[0]}' if WRITEBACK[1] else f'ERROR {WRITEBACK[0]}'}")
        sys.stdout.flush()
    
    mode = sys.stdin.readline().rstrip()

    # commandAndArguement = input().split(" ")

    # command = commandAndArguement[0]

    # arguement = commandAndArguement[1] if len(commandAndArguement) > 1 else "PADDING"

    # options = {
    #     "PASSKEY": setPASSKEY,
    #     "ENCRYPT": ENCRYPT,
    #     "DECRYPT": DECRYPT,
    #     "QUIT": QUIT
    # }

    # result = options[command](arguement) if command in options and len(commandAndArguement) <= 2 else NOCOMMAND()

    # print(f"{f'RESULT {result[0]}' if result[1] else f'ERROR {result[0]}'}")
