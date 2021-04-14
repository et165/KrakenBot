import pyautogui
import random
from random import uniform
from time import sleep, time

pyautogui.FAILSAFE = True

n = 4

for i in range(n):
    
 print("Starting..")
 print("You are killing Kraken: ", n, " times.")
 sleep(3)

#Top Right
 XtopRight = random.randint(1414, 1439)
 YtopRight = random.randint(453, 473)

 #Bot Right
 XbotRight= random.randint(1429, 1455)
 YbotRight = random.randint(579, 595)

 #Top Left
 XtopLeft = random.randint(1093, 1112)
 YtopLeft = random.randint(461, 477)

 #Bot Left
 XbotLeft = random.randint(1075, 1105)
 YbotLeft = random.randint(585, 605)

 #Center
 X = random.randint(1224, 1256)
 Y = random.randint(531, 557)

 KrakenWait = random.randint(55, 63)
 randomSec = random.uniform(1.9, 2.7)

 pyautogui.moveTo(XtopRight,YtopRight)
 print("X = ", XtopRight, "Y = ", YtopRight)
 pyautogui.click()
 print("click top right")
 sleep(randomSec)

 pyautogui.moveTo(XbotRight,YbotRight)
 print("X = ", XbotRight, "Y = ", YbotRight)
 pyautogui.click()
 print("click bot right")
 sleep(randomSec)

 pyautogui.moveTo(XtopLeft,YtopLeft)
 print("X = ", XtopLeft, "Y = ", YtopLeft)
 pyautogui.click()
 print("click top left")
 sleep(randomSec)

 pyautogui.moveTo(XbotLeft,YbotLeft)
 print("X = ", XbotLeft, "Y = ", YbotLeft)
 pyautogui.click()
 print("click bot left")
 sleep(randomSec)

 pyautogui.moveTo(X,Y)
 pyautogui.click()
 print("CENTER!") 
 sleep(KrakenWait) 
        
