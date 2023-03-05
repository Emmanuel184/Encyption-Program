import sys
from subprocess import Popen, PIPE

logger = Popen(['python3', 'logger.py', sys.argv[1]], stdout=PIPE, stdin=PIPE, encoding='utf-8')

encrytion = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf-8')



while True:

    command = input()

    logger.stdin.write(f"{command}\n")
    logger.stdin.flush()
    encrytion.stdin.write(f"WRITE\n")
    encrytion.stdin.write(f"{command}\n")
    encrytion.stdin.write(f"READ\n")
    encrytion.stdin.flush()
    result = encrytion.stdout.readline().rstrip()
    print(result)
    logger.stdin.write(f"{result}")
    logger.stdin.flush()    




    



    




