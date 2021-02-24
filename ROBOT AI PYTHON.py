import serial as SER
from gpiozero import DistanceSensor
import Tkinter as TK
import cv2 as CV
import os
import time
import numpy as np
import random
import pygame
A = 0
Z = 0
C = 0
D = 0
E = 0
F = 0
G = 0
J = 0
P = 0
K = 0
MWSW = 0
CAM = 0
TIME = 0
CON = 0
READYPI = "1"
AMSTOP = "2"
AMAI = "3"
AMAIREV = "4"
AMR90 = "5"
AML90 = "6"
AMCON = "7"
AMUP = "8"
AMDOWN = "9"
AMREV = "10"
AMFOR = "11"
AML = "12"
AMR = "13"
AMTURN180 = "14"
EMSTOP = "15"
KEY = 100
Z = 0
def MWSWITCH():
    global MWSW
    MWSW ++ 1
    if (MWSW == 1):
        MW.destroy()
        MWSW = 0
def FMPACK():
    TK.Label(MW, image=photo).pack()
    MW.after(1, MWSWITCH)
    MW.mainloop()
face_cascade = CV.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = CV.VideoCapture(0)
MW = TK.Tk()
w = 1280
h = 670
pygame.init()
screen = pygame.display.set_mode((50, 50))
w, h = MW.winfo_screenwidth(), MW.winfo_screenheight()
MW.geometry("1280x670")
MW.overrideredirect(0)
US1 = DistanceSensor(echo = 17, trigger = 4)
US2 = DistanceSensor(echo = 18, trigger = 3)
Arduino = SER.Serial('/dev/ttyUSB0', 9600)
Arduino.write(READYPI)
photo = TK.PhotoImage(file="LoadTestGIF.gif", format="gif -index %d" % (0))
FMPACK()
def FM():
    if (Z == 1):
        if (D == 0 and E == 0 and F == 0 and C < 3):
            C ++ 1
            photo = TK.PhotoImage(file="HappyGIF.gif", format="gif -index %d" % (0))
            FMPACK()
        if (D != 0):
            D -- 1
        if (E != 0):
            E -- 1
        if (F != 0):
            F -- 1
        Z = 0
    if (Z == 2):
        if (C == 0 and E == 0 and F == 0 and D < 3):
            D ++ 1
            photo = TK.PhotoImage(file="SadGIF.gif", format="gif -index %d" % (0))
            FMPACK()
        if (C != 0):
            C -- 1
        if (E != 0):
            E -- 1
        if (F != 0):
            F -- 1
        Z = 0
    if (Z == 3):
        if (D == 0 and D == 0 and F == 0 and E < 3):
            E ++ 1
            photo = TK.PhotoImage(file="AngryGIF.gif", format="gif -index %d" % (0))
            FMPACK()
        if (C != 0):
            C -- 1
        if (D != 0):
            D -- 1
        if (F != 0):
            F -- 1
        Z = 0
    if (Z == 4):
        if (C == 0 and D == 0 and E == 0 and F < 3):
            F ++ 1
            photo = TK.PhotoImage(file="ShockGIF.gif", format="gif -index %d" % (0))
            FMPACK()
        if (C != 0):
            C -- 1
        if (D != 0):
            D -- 1
        if (E != 0):
            E -- 1
        Z = 0
    if (Z > 4):
        while True:
            if (K == 0):
                photo = TK.PhotoImage(file="DeadGIF.gif", format="gif -index %d" % (0))
                FMPACK()
                K = 1
    if (C > 3 or D > 3 or E > 3 or F > 3):
        while True:
            if (K == 0):
                photo = TK.PhotoImage(file="Dead2GIF.gif", format="gif -index %d" % (0))
                FMPACK()
                K = 1
    if (C == 0 and D == 0 and E == 0 and F == 0):
        photo = TK.PhotoImage(file="NeutralGIF.gif", format="gif -index %d" % (0))
        FMPACK()
    if (C == 3):
        photo = TK.PhotoImage(file="VeryHappyGIF.gif", format="gif -index %d" % (0))
        FMPACK()
    if (D == 3):
        photo = TK.PhotoImage(file="VerySadGIF.gif", format="gif -index %d" % (0))
        FMPACK()
    if (E == 3):
        photo = TK.PhotoImage(file="VeryAngryGIF.gif", format="gif -index %d" % (0))
        FMPACK()
    if (F == 3):
        photo = TK.PhotoImage(file="FearGIF.gif", format="gif -index %d" % (0))
        FMPACK()
def JVAR():
    while (J == 1):
        if (Arduino.readline() == "b'ARREADY\n"):
            J = 0
def CVFACE():
    ret, img = cap.read()
    gray = CV.cvtColor(img, CV.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if (x,y,w,h) in faces:
        CV.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        Arduino.write(AMSTOP)
        FM(1)
        P = 0
        J = 1
        JVAR()
        Arduino.write(AMTURN180)
        J = 1
        JVAR()
    else:
        if (P == 30000):
            Z = 2
            FM()
            P = 0
        time.sleep(0.01)
        P ++ 1
def CONM():
    CON ++ 1
    if (CON == 1):
        Arduino.write(AMCON)
    if (CON == 2):
        Arduino.write(AMAI)
        CON = 0
def CONTROL():
    if (CON == 1):
        if (KEY == 3):
            Arduino.write(AMUP)
            KEY = 100
        if (KEY == 4):
            Arduino.write(AMDOWN)
            KEY = 100
        if (KEY == 5):
            Arduino.write(AMREV)
            KEY = 100
        if (KEY == 6):
            Arduino.write(AMFOR)
            KEY = 100
        if (KEY == 7):
            Arduino.write(AML)
            KEY = 100
        if (KEY == 8):
            Arduino.write(AMR)
            KEY = 100
def CVWINDOW():
    if (CAM == 1):
        ret, frame = cap.read()
        CV.imshow('CAM', frame)
def BOOT():
    global A
    while (A == 0):
        photo = TK.PhotoImage(file="LoadTestGIF.gif", format="gif -index %d" % (0))
        FMPACK()
        if (Arduino.readline() == "b'READYAR\n"):
            A = 1
        else:
            if(P == 60):
                while True:
                    if (K == 0):
                        photo = TK.PhotoImage(file="FatalErrorGIF.gif", format="gif -index %d" % (0))
                        FMPACK()
                        K =1
            A = 0
            P ++ 1
            time.sleep(1)
    time.sleep(5)
def PREMAIN():
    if (A == 1):
        if (US2.distance > 0.07 or US1.distance < 0.16):
            Arduino.write(AMSTOP)
            A = 2
            Z = 4
            FM()
            J = 1
            JVAR()
        while (A == 2):
            if (US2.distance <= 0.07 or US1.distance >= 0.16):
                Arduino.write(AMAI)
                A = 3
                FMPACK()
        if (A == 1):
            A = 3
            Arduino.write(AMAI)
def KEYPRESS():
    if (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_0):
            KEY = 0
        if (event.key == pygame.K_1):
            KEY = 1
        if (event.key == pygame.K_e):
            KEY = 2
        if (event.key == pygame.K_o):
            KEY = 3
        if (event.key == pygame.K_l):
            KEY = 4
        if (event.key == pygame.K_s):
            KEY = 5
        if (event.key == pygame.K_w):
            KEY = 6
        if (event.key == pygame.K_a):
            KEY = 7
        if (event.key == pygame.K_d):
            KEY = 8
        if (event.key == pygame.K_9):
            KEY = 9
        if (event.key == pygame.K_q):
            KEY = 10
        if (event.key == pygame.K_4):
            KEY = 11
def CAMMODE():
    CAM ++ 1
    if (CAM == 2):
        CV.waitKey(1)
        CV.destroyAllWindows()
        CAM = 0
def USMODULE():
    if (CON == 0):
        Arduino.write(AMAIREV)
        Z = 4
        FM()
        J = 1
        JVAR()
        if (G < 4):
            Arduino.write(AMR90)
            G ++ 1
            J = 1
            JVAR()
            if (US1.distance > 0.16):
                G = random.choice[0,7]
            if (G == 3):
                G = 7
        if (G > 4):
            Arduino.write(AML90)
            G -- 1
            J = 1
            JVAR()
            if (US1.distance > 0.16):
                G = random.choice[0,7]
            if (G == 4):
                G = 0
    if (US1.distance < 0.16):
        Arduino.write(AMSTOP)
        Z = 3
        FM()
        J = 1
        JVAR()
        if (G < 4):
            Arduino.write(AMR90)
            G ++ 1
            J = 1
            JVAR()
            if (US1.distance > 0.16):
                G = random.choice[0,7]
            if (G == 3):
                G = 7
        if (G > 4):
            Arduino.write(AML90)
            G -- 1
            J = 1
            JVAR()
            if (US1.distance > 0.16):
                G = random.choice[0,7]
            if (G == 4):
                G = 0
def EMSTOP():
    if (KEY == 10):
        Arduino.write(EMSTOP)
        KEY = 100
def CLOSE():
    if (KEY == 11):
        Arduino.write(EMSTOP)
        if (CAM == 1):
            CV.DestroyAllWindows()
        MW.quit()
        pygame.quit()
        sys.exit()
def KEYINPUTS():
    if (KEY == 0):
        CAMMODE()
        KEY = 100
    if (KEY == 2):
        CONM()
        KEY = 100
def MAINLOOP():
    while (A == 3):
        FM()
        FMPACK()
        USMODULE()
        KEYPRESS()
        KEYINPUTS()
        EMSTOP()
        CVFACE()
        CONTROL()
        CVWINDOW()
        CLOSE() 
BOOT()
PREMAIN()
MAINLOOP()
