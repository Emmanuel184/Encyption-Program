import sys
from subprocess import Popen, PIPE

logger = Popen(['python3', 'logger.py', sys.argv[1]], stdout=PIPE, stdin=PIPE, encoding='utf-8')

encrytion = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf-8')

lastResult = ""

options = {
    "PASSKEY": -1,
    "ENCRYPT": -1,
    "DECRYPT": -1,
    "QUIT": -1    
}

HISTORY = []

def historyReturn() -> int:

    global HISTORY

    print(f"HISTORY")

    index = 0

    while index < len(HISTORY):

        print(f"{index} {' '.join(HISTORY[index])}")
        index += 1
    
    print(f"{index} to go back")

    useHistory = int(input())

    if useHistory < 0 or useHistory >= len(HISTORY):
        return -1
    else:
        return useHistory

while True:

    userChoice = historyReturn()

    command = input().split(" ") if userChoice == -1 else HISTORY[userChoice]

    if command[0] not in options:
        continue

    logger.stdin.write(f"{' '.join(command)}\n")
    logger.stdin.flush()

    if command[0].lower() == "quit":
        encrytion.stdin.write("QUIT")
        exit()
        
    encrytion.stdin.write(f"WRITE\n")
    encrytion.stdin.write(f"{' '.join(command)}\n")
    encrytion.stdin.write(f"READ\n")
    encrytion.stdin.flush()
    result = encrytion.stdout.readline()
    encrytion.stdout.readline()
    print(result, end="")
    lastResult = result
    logger.stdin.write(f"{result}")
    logger.stdin.flush()    

    HISTORY.append(command)




    



    




