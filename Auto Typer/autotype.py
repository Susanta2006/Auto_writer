########### MODULES #################
import pyfiglet as pf               #
import warnings                     #
import sys                          #
from datetime import datetime       #
import pyautogui as pg              #
pg.FAILSAFE = False                 #
import time                         #
#####################################

########### BANNER #########################
pf = pf.figlet_format("Auto-Typer")        #
print(pf,"\n version 1.0")                 #
print()                                    #
warnings.filterwarnings('ignore')          #
############################################

###################### MAIN CODE ######################################################
print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
print("***********************************************************************")
print()
try:
    n=int(input("[+]Enter how many times you want send: "))
    print()
    msg=str(input("[+]Enter the message: "))
    print()
    s=int(input("[+]Enter the time (in seconds) after which the message is to be sent: "))
    print()
    print("[*]Okay, sending the message after",s,"seconds, prepare suitable site within this time !!")
    print()
    time.sleep(s)
    print("[*]Typing started......")
    print()
    for i in range(n):
        #pg.typewrite(msg,interval=0.01)      #interval shows the speed of typing
        pg.typewrite(msg)
        pg.press("enter")
except Exception or KeyboardInterrupt or SyntaxError:
    print()
    print("[-]Something went wrong !!")
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    sys.exit()
####################################### END OF THE CODE ##################################
