python3 driver.py [log file name] 
|
v
worked on cs2 machine

!!!! A version of this program would exit and logger.py would keep going, and create a huge [log file name], I tested this version and was not able to replicate this, so it should not happen, but I would still check if log.txt is a valid size even though this error was not present in this version !!!

Also I used lists to manipulate the strings, the programs I thought it was a nice touch for better performance, but I realized I was going to need to do a lot of string alteration the way I implemented my programs, so there is some admittetly confusing code, I tried to comment most of them but I can explain the code if needed.

logger.py 
logger.py program logs all valid commands in [log file name] along with wether the command was sucessful and thet time it was executed

encryption.py
encryption.py program is in charge of encrypting the strings passed to it and setting the passkey for the encryption algorithm, returns wether the ecryption was successful or not along with a message. 

driver.py
driver.py is the main program which creates two subprocesses for the other two programs logger.py and encryption.py, this program keeps track of the history commands for the current session, this program has a user interface which walks you through how the program works.



