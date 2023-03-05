from curses.ascii import isdigit
import sys
from subprocess import Popen, PIPE


logger = Popen(['python3', 'logger.py', sys.argv[1]], stdout=PIPE, stdin=PIPE, encoding='utf-8')

encrytion = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf-8')

lastResult = ""

options = {
    "PASSKEY": "Sets a new password for encryption algorithm",
    "ENCRYPT": "Encrypts string",
    "DECRYPT": "Decrypts string",
    "QUIT": "Quits program"    
}

HISTORY = []


def printHistory():

    print(f"HISTORY")

    index = 0

    while index < len(HISTORY):

        print(f"{index} {' '.join(HISTORY[index])}")
        index += 1
    
    return index
    
    



def historyReturn() -> int:

    global HISTORY

    goIntoHistory = input("Want to go into history? (y/n) ")

    if goIntoHistory != "y":
        return - 1

    logger.stdin.write("HISTORY ACCESSED\n")
    logger.stdin.flush()

    lastIndex = printHistory()
    
    print(f"{lastIndex} to go back")

    try:
        useHistory = int(input())
    except ValueError:
        print("Please enter integer only or -1 to exit")

    if useHistory < 0 or useHistory >= len(HISTORY):
        return -1
    else:
        return useHistory

def printCommands():

    global options

    print(f"---------------------\nCOMMANDS")

    for option in options.keys():

        print(f"{option} -> {options[option]}")
    
    print(f"---------------------")


try:
    while True:

        printCommands()

        command = input("COMMAND: ").split(" ")

        if command[0] not in options:
            print("NOT VALID COMMAND")
            continue

        useHistory = -1

        if HISTORY:
            useHistory = historyReturn()

        command.append(f"{input('Arguement: ') if useHistory == -1 else HISTORY[useHistory]}")
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

        if command[0] != "PASSKEY":
            HISTORY.append(command[1])
        

except KeyboardInterrupt:
        logger.stdin.write(f"quit")
        encrytion.stdin.write("QUIT PADDING")
        exit()


    



    




