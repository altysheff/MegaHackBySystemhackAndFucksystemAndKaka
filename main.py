###### LIB #######
import pyautogui
import cv2
import time
import os
###### LIB END #######

###### FUNCTIONS ######
def makephoto(): #make photo from web-cam
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()
    ret, frame = cap.read()
    cv2.imwrite('cam.png', frame)   
    cap.release()

def makess():
    screen = pyautogui.screenshot('screenshot.png')

def capturevideo():
    cap = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('captured.avi',codec, 25.0, (640,480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        out.write(frame)
    out.release()
    cap.release()
    cv2.destroyAllWindows()

def lockmouse():
    while True:
        pyautogui.moveTo(0, 0)

def killtaskmngr():
    os.system("taskkill /F /IM Taskmgr.exe")


###### END OF FUNCTIONS ######
functxt = "SELECT FUNCTION: \n1. MAKE PHOTO FROM WEBCAM \n2. MAKE SCREENSHOT \n3. RECORD VIDEO FROM WEBCAM \n4. LOCK MOUSE \n5. KILL TASK MANAGER\n"

os.system("echo off")
os.system("cls")
os.system("color a")

while True:
    func = int(input(functxt))
    if func == 1:
        makephoto()
    elif func == 2:
        makess()
    elif func == 3:
        capturevideo()
    elif func == 4:
        lockmouse()    
    elif func == 5:
        killtaskmngr()
    time.sleep(1)
    os.system("cls")