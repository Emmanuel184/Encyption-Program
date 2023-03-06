import sys
from subprocess import Popen, PIPE



logger = Popen(['python3', 'logger.py', sys.argv[1]], stdout=PIPE, stdin=PIPE, encoding='utf-8')

encrytion = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf-8')

logger.stdin.flush()
logger.stdout.flush()

lastResult = ""

options = {
    "passkey": "Sets a new password for encryption algorithm",
    "encrypt": "Encrypts string",
    "decrypt": "Decrypts string",
    "history": "Shows history",
    "quit": "Quits program"
    
}

HISTORY = []

def printHistory():

    print(f"HISTORY")

    index = 0

    while index < len(HISTORY):

        print(f"{index} {HISTORY[index]}")
        index += 1
    
    return index
    
def quit():
    global encrytion
    global logger
    encrytion.stdin.write("quit\n")
    encrytion.stdin.flush()
    logger.stdin.flush()
    logger.stdin.write("quit\n")
    logger.stdin.flush()
    logger.wait()
    
    
def historyReturn() -> int:

    global HISTORY

    goIntoHistory = input("Want to go into history? (y/n) ")

    if goIntoHistory != "y":
        return -1

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

        command = input("COMMAND: ").lower().split(" ")

        if command[0] == "quit":
            quit()
            break
        if command[0] not in options:
            print("NOT VALID COMMAND")
            continue
        
        if command[0] == "history":
            printHistory()
            continue


        useHistory = -1

        if HISTORY and command[0] != "passkey":
            useHistory = historyReturn()

        command.append(f"{input('Arguement: ').lower() if useHistory == -1 else HISTORY[useHistory].lower()}")
        logger.stdin.write(f"{' '.join(command)}\n")
        logger.stdin.flush()

            
        encrytion.stdin.write(f"write\n")
        encrytion.stdin.write(f"{' '.join(command)}\n")
        encrytion.stdin.write(f"read\n")
        encrytion.stdin.flush()
        result = encrytion.stdout.readline().rstrip('\n')
        encrytion.stdout.readline()
        print(result)
        lastResult = result.upper()
        testRESULTSPLIT = result.split(' ')[0]
 

        if command[0] != "passkey":
            logger.stdin.write(f"{command[0]} {'SUCCESS' if result.split(' ')[0] == 'RESULT' else 'ERROR'} {' '.join(result.split(' ')[1:])}\n".lower())
            logger.stdin.flush()
            if useHistory == -1:
                HISTORY.append(command[1])

            if result.split(" ")[0] != "ERROR":

                test = result.split(" ")[0]
                testTwo = "".join(result.split(" ")[1:])
                
                HISTORY.append("".join(result.split(" ")[1:]))
        else:

            logger.stdin.write(f"{command[0]} {'SUCCESS' if result.split(' ')[0] == 'RESULT' else 'ERROR'}\n".lower())
            logger.stdin.flush()

        
except KeyboardInterrupt:
        quit()


    



    




