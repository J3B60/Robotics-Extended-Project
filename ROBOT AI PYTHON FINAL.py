import serial as SER
from gpiozero import DistanceSensor
import cv2
import os
import time
import numpy as np
import random
import pygame
print "Import Successful"
A = 0
C = 0
D = 0
E = 0
F = 0
G = 0
J = 0
K = 0
P = 0
M = 0
OPENCV1 = 0
DEBUG = 0
DEBUGSW = 0
BOOTPY = 0
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
AMREV = "0"
AMFOR = "/"
AML = "."
AMR = "-"
AMTURN180 = ","
EMSTOP = "+"
ARDUINOBOOT = "a"
KEY = 100
print "Variable Set Successful"
def FM(Q):
    global K
    global C
    global D
    global E
    global F
    global photo
    if (Q == 1):
        if (D == 0 and E == 0 and F == 0 and C < 3):
            C += 1
            photo = pygame.image.load('HappyGIF.gif')
            FMPACK()
        if (D != 0):
            D -= 1
        if (E != 0):
            E -= 1
        if (F != 0):
            F -= 1
        Q = 0
    if (Q == 2):
        if (C == 0 and E == 0 and F == 0 and D < 3):
            D += 1
            photo = pygame.image.load('SadGIF.gif')
            FMPACK()
        if (C != 0):
            C -= 1
        if (E != 0):
            E -= 1
        if (F != 0):
            F -= 1
        Q = 0
    if (Q == 3):
        if (D == 0 and D == 0 and F == 0 and E < 3):
            E += 1
            photo = pygame.image.load('AngryGIF.gif')
            FMPACK()
        if (C != 0):
            C -= 1
        if (D != 0):
            D -= 1
        if (F != 0):
            F -= 1
        Q = 0
    if (Q == 4):
        if (C == 0 and D == 0 and E == 0 and F < 3):
            F += 1
            photo = pygame.image.load('ShockGIF.gif')
            FMPACK()
        if (C != 0):
            C -= 1
        if (D != 0):
            D -= 1
        if (E != 0):
            E -= 1
        Q = 0
    if (Q > 5):
        while True:
            if (K == 0):
                photo = pygame.image.load('DeadGIF.gif')
                FMPACK()
                K = 1
    if (C > 3 or D > 3 or E > 3 or F > 3):
        while True:
            if (K == 0):
                photo = pygame.image.load('Dead2GIF.gif')
                FMPACK()
                K = 1
    if (C == 0 and D == 0 and E == 0 and F == 0):
        photo = pygame.image.load('NeutralGIF.gif')
        FMPACK()
    if (C == 3):
        photo = pygame.image.load('VeryHappyGIF.gif')
        FMPACK()
    if (D == 3):
        photo = pygame.image.load('VerySadGIF.gif')
        FMPACK()
    if (E == 3):
        photo = pygame.image.load('VeryAngryGIF.gif')
        FMPACK()
    if (F == 3):
        photo = pygame.image.load('FearGIF.gif')
        FMPACK()
def JVAR():
    global J
    global Arduino
    global time
    global M
    #while (J == 1):        
        #print "M is:", M
        #print "Waiting for Arduino"
        #Arduino = SER.Serial('/dev/ttyUSB0', 9600, timeout=0)
    Arduino.write(M)
        #if (Arduino.readline()== "AR\r\n"):
            #Arduino.write("NA")
            #print "Arduino Done"
            #J = 0   
def CVFACE():
    global P
    global J
    global SIGNAL
    global Arduino
    global CVDETCT
    global OPENCV1
    global AMSTOP
    global AMTURN180
    global M
    global cap
    global face_cascade
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        CVDETCT = 'True'
        SIGNAL = 'AMSTOP'
        FM(1)
        P = 0
        J = 1
        M = AMSTOP
        JVAR()
        SIGNAL = 'AMTURN180'
        J = 1
        M = AMTURN180
        JVAR()
    else:
        if (P == 30000):
            FM(2)
            P = 0
            CVDETECT = 'False'
    cv2.waitKey(1)
    time.sleep(0.01)
    P += 1
def CONM():
    global CON
    global Arduino
    global SIGNAL
    global AMCON
    global AMAI
    global M
    CON += 1
    if (CON == 1):
        SIGNAL = 'AMCON'
        M = AMCON
        JVAR()
    if (CON == 2):
        SIGNAL = 'AMAI'
        M = AMAI
        JVAR()
        CON = 0
def CONTROL():
    global CON
    global KEY
    global Arduino
    global SIGNAL
    global AMUP
    global AMDOWN
    global AMREV
    global AMFOR
    global AML
    global AMR
    global M
    if (CON == 1):
        if (KEY == 3):
            SIGNAL = 'AMUP'
            KEY = 100
            M = AMUP
            JVAR()
        if (KEY == 4):
            SIGNAL = 'AMDOWN'
            KEY = 100
            M = AMDOWN
            JVAR()
        if (KEY == 5):
            SIGNAL = 'AMREV'
            KEY = 100
            M = AMREV
            JVAR()
        if (KEY == 6):
            SIGNAL = 'AMFOR'
            KEY = 100
            M = AMFOR
            JVAR()
        if (KEY == 7):
            SIGNAL = 'AML'
            KEY = 100
            M = AML
            JVAR()
        if (KEY == 8):
            SIGNAL = 'AMR'
            KEY = 100
            M = AMR
            JVAR()
def CVWINDOW():
    global CAM
    global img
    global cap
    global ret
    if (CAM == 1):
        ret, img = cap.read()
        cv2.imshow('CAM' ,img)
        cv2.waitKey(1)
def BOOT():
    global A
    global P
    global K
    global ARDUINOBOOT
    global photo
    global Arduino
    global BOOTPY
    global SIGNAL    
    while (A == 0):
        Arduino = SER.Serial('/dev/ttyUSB0', 9600)
        Arduino.write(ARDUINOBOOT)
        SIGNAL = 'ARBOOT'
        if (Arduino.readline() == "RE\r\n"):
            A = 1
            BOOTPY = 0
            print "BOOT Successful !!"
            Arduino.write("q")
        else:
            if(P == 60):
                while True:
                    if (K == 0):
                        photo = pygame.image.load('FatalErrorGIF.gif')
                        BOOTPY = 0
                        FMPACK()
                        K = 1
                        print "BOOT unsuccessful -End-"
            A = 0
            P += 1
            time.sleep(1)
            BOOTPY = 1
            print "BOOT unsuccessful -Retry-"
            print "Time Remaining: %d" % (60-P)
            FMPACK()
    time.sleep(5)
def PREMAIN():
    global US2
    global US1
    global Arduino
    global SIGNAL
    global A
    global J
    global AMSTOP
    global AMAI
    global M
    if (A == 1):
        print "US1:", US1.distance
        print "US2:", US2.distance
        if (US2.distance > 0.07 or US1.distance < 0.16):
            print "PREMAIN -DANGER-"
            SIGNAL = 'AMSTOP'
            A = 2
            M = AMSTOP
            FM(4)
            J = 1
            print "-Wait for Arduino-"
            JVAR()
    while (A == 2):
        print "US1:", US1.distance
        print "US2:", US2.distance
        if (US2.distance <= 0.07 and US1.distance >= 0.16):
            M = AMAI
            print "PREMAIN -DANGER OVER-"
            SIGNAL = 'AMAI'
            A = 3
            FMPACK()
            JVAR()
    if (A == 1):
        A = 3
        print "PREMAIN -SAFE-"
        SIGNAL = 'AMAI'
        FM(0)
        M = AMAI
        JVAR()
def KEYPRESS():
    global KEY
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
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
    global CAM
    CAM += 1
    if (CAM == 2):
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        CAM = 0
def USMODULE():
    global CON
    global Arduino
    global SIGNAL
    global J
    global G
    global US1
    global US2
    global AMAIREV
    global AMR90
    global AML90
    global AMSTOP
    global M
    if (CON == 0):
        if (US2.distance > 0.07):
            SIGNAL = 'AMAIREV'
            FM(4)
            J = 1
            M = AMAIREV
            JVAR()
            if (G < 4):
                SIGNAL = 'AMR90'
                G += 1
                J = 1
                M = AMR90
                JVAR()
                if (US1.distance > 0.16):
                    G = random.choice([0,7])
                if (G == 3):
                    G = 7
            if (G > 4):
                SIGNAL = 'AML90'
                G -= 1
                J = 1
                M = AML90
                JVAR()
                if (US1.distance > 0.16):
                    G = random.choice([0,7])
                if (G == 4):
                    G = 0
        if (US1.distance < 0.16):
            SIGNAL = 'AMSTOP'
            FM(3)
            J = 1
            M = AMSTOP
            JVAR()
            if (G < 4):
                SIGNAL = 'AMR90'
                G += 1
                J = 1
                M = AMR90
                JVAR()
                if (US1.distance > 0.16):
                    G = random.choice([0,7])
                if (G == 3):
                    G = 7
            if (G > 4):
                SIGNAL = 'AML90'
                G -= 1
                J = 1
                M = AML90
                JVAR()
                if (US1.distance > 0.16):
                    G = random.choice([0,7])
                if (G == 4):
                    G = 0
def EMSTOP():
    global KEY
    global Arduino
    global SIGNAL
    global M
    if (KEY == 10):
        SIGNAL = 'EMSTOP'
        KEY = 100
        M = EMSTOP
        JVAR()
def CLOSE():
    global KEY
    global Arduino
    global SIGNAL
    global CAM
    global EMSTOP
    global M
    if (KEY == 11):
        M = EMSTOP
        JVAR()
        Arduino.close()
        SIGNAL = 'EMSTOP'
        if (CAM == 1):
            cv2.DestroyAllWindows()
        pygame.quit()
        sys.exit()
def KEYINPUTS():
    global KEY
    global DEBUGSW
    global TIME
    if (KEY == 0):
        CAMMODE()
        KEY = 100
    if (KEY == 1):
        TIME += 1
        KEY = 100
        if (TIME == 2):
            TIME = 0
    if (KEY == 2):
        CONM()
        KEY = 100
    if (KEY == 9):
        DEBUGSW += 1
        KEY = 100
        if (DEBUGSW == 2):
            DEBUG = 0
            DEBUGSW = 0
def MAINLOOP():
    global A
    while (A == 3):
        print "MAIN FMPACK"
        FMPACK()
        print "MAIN USMODULE"
        USMODULE()
        print "MAIN KEYPRESS"
        KEYPRESS()
        print "MAIN KEYINPUTS"
        KEYINPUTS()
        print "MAIN EMSTOP"
        EMSTOP()
        print "MAIN CVFACE"
        CVFACE()
        print "MAIN CONTROL"
        CONTROL()
        print "MAIN CVWINDOW"
        CVWINDOW()
        print "MAIN CLOSE"
        CLOSE()
def FMPACK():
    global photo
    global BOOTPY
    global CON
    global TIME
    global DEBUG
    global CVDETECT
    global Arduino
    global SIGNAL
    global US1
    global US2
    global A
    screen.fill((255, 255, 255))
    screen.blit(photo, (0, 0))
    if CON == 1:
        CONPY = myfont.render("Controller ON", 1, (0, 0, 0))
    else:
        CONPY = myfont.render("", 1, (0, 0, 0))
    screen.blit(CONPY, (10, 10))
    if TIME == 1:
        TIMEPY = myfont.render(time.ctime(), 1, (0, 0, 0))
    else:
        TIMEPY = myfont.render("", 1, (0, 0, 0))
    screen.blit(TIMEPY, (800, 10))
    if BOOTPY == 1:
        PPY = myfont.render(("%d" % (P)), 1, (255, 0, 0))
    else:
        PPY = myfont.render("", 1, (255, 0, 0))
    screen.blit(PPY, (10, 10))
    if DEBUG == 1:
        US1PY = myfont.render(('US1:', US1.distance), 1, (255, 0, 0))
        US2PY = myfont.render(('US2:', US2.distance), 1, (255, 0, 0))
        APY = myfont.render(('A: %d' % (A)), 1, (255, 0, 0))
        SIGNALPY = myfont.render(('PI: %s' % (SIGNAL)), 1, (255, 0, 0))
        ARREADPY = myfont.render(('AR: %s' % (Arduino.readline())), 1, (255, 0, 0))
        CVPY = myfont.render(('CV: %s' % (CVDETECT)), 1, (255, 0, 0))
    else:
        US1PY = myfont.render('', 1, (255, 0, 0))
        US2PY = myfont.render('', 1, (255, 0, 0))
        APY = myfont.render('', 1, (255, 0, 0))
        SIGNALPY = myfont.render('', 1, (255, 0, 0))
        ARREADPY = myfont.render('', 1, (255, 0, 0))
        CVPY = myfont.render('', 1, (255, 0, 0))
    screen.blit(US1PY, (10, 50))
    screen.blit(US2PY, (10, 90))
    screen.blit(APY, (10, 130))
    screen.blit(SIGNALPY, (10, 170))
    screen.blit(ARREADPY, (10, 210))
    screen.blit(CVPY, (10, 250))
    pygame.display.update()
    print "Display Update Successful"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
pygame.init()
screen = pygame.display.set_mode((1280, 650))
myfont = pygame.font.SysFont("helvatica", 50)
US1 = DistanceSensor(echo = 17, trigger = 4)
US2 = DistanceSensor(echo = 18, trigger = 3)
print "US Module set Successful"
Arduino = SER.Serial('/dev/ttyUSB0', 9600, timeout=0)
print "READYPI Write Successful"
SIGNAL = 'READYPI'
pygame.display.flip()
print "Pygame display Successful"
photo = pygame.image.load('LoadTestGIF.gif')
FMPACK()
print "BOOT Start"
BOOT()
print "PREMAIN Start"
PREMAIN()
print "MAINLOOP Start"
MAINLOOP()
