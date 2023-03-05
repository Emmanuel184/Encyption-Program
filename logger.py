import sys
from datetime import datetime

testARGV = sys.argv[1]
print(testARGV)

try:
    with open(sys.argv[1], "a") as test:
        
        startDate = datetime.today().strftime("%Y-%m-%d %H:%M")

        test.write(f"{startDate} [START] Logging Started\n")
       

        while True:

            log = sys.stdin.readline().lower().rstrip('\n').split(" ")

            action = log[0]
            
            message = log[1:] if len(log) > 1 else ""

            date = datetime.today().strftime("%Y-%m-%d %H:%M")

            finalWrite = [date]

            if action.lower() == "quit":

                test.write(f"{finalWrite[0]} [STOP] Logging Stopped\n")
                break
            
            finalWrite.append(f"[{action}]")
            finalWrite.append(" ".join(message))

            test.write(f"{' '.join(finalWrite).upper()}\n")

except BaseException or KeyboardInterrupt as e:
    exit()






