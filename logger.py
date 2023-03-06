import sys
from datetime import datetime

sys.stdin.flush()
sys.stdout.flush()

testARGV = sys.argv[1]
print(testARGV)

def quit():
    try:
        with open(sys.argv[1], "a") as quit:
            endDate = datetime.today().strftime("%Y-%m-%d %H:%M")
            quit.write(f"{endDate} [STOP] Logging Stopped from KeyboardInterrupt\n")
            exit()
    except:
        pass

try:
    with open(sys.argv[1], "a") as test:
        
        startDate = datetime.today().strftime("%Y-%m-%d %H:%M")

        test.write(f"{startDate} [START] Logging Started\n")
       

        while True:

            log = sys.stdin.readline().rstrip('\n').split(" ")

            action = log[0]
            
            message = log[1:] if len(log) > 1 else ""

            date = datetime.today().strftime("%Y-%m-%d %H:%M")

            finalWrite = [date]

            if action == "quit":

                test.write(f"{finalWrite[0]} [STOP] Logging Stopped\n")
                break
            
            finalWrite.append(f"[{action}]")
            finalWrite.append(" ".join(message))

            test.write(f"{' '.join(finalWrite).upper()}\n")

except BaseException or KeyboardInterrupt as e:
    quit()
