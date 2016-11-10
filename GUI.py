# Import
from tkinter import *
import random
import pygame
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setwarnings(False)

buttonRechts = 23
buttonLinks = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonLinks, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Knop S1
GPIO.setup(buttonRechts, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Knop S2

# Variablen voor functies
iterationsGroen = 1
speedGroen = 1
iterationsRood = 3
speedRood = 1
pincode = 0000

# Algemene functies
def BlinkGroen(numTimes, speed):
    for i in range(0,numTimes): ## Zet loop numTimes aan
        GPIO.output(21, True) ## zet GPIO pin 7 aan
        time.sleep(speed) ## Wacht
        GPIO.output(21, False) ## zet GPIO pin 7 aan
        time.sleep(speed) ## Wacht

def BlinkRood(numTimes, speed):
    for i in range(0,numTimes): ## Zet loop numTimes aan
        GPIO.output(4, True) ## zet GPIO pin 4 aan
        time.sleep(speed) ## Wacht
        GPIO.output(4, False) ## zet GPIO pin 4 uit
        time.sleep(speed) ## Wacht

def alarmaan():
    BlinkRood(int(iterationsRood),float(speedRood))
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play()

def knop():
    while True:
        input_1 = GPIO.input(buttonLinks)
        if input_1 == False:
            break

def scherm1():
    # Algemene settings
    root = Tk()
    root.title('Alarm')
    root.geometry('800x480')
    root.resizable(width=False, height=False)
    root.configure(background='#ddffcc')
    Label(root,text='Vul uw Pincode in:', bg='#ddffcc').pack()

    # Userinputveld
    userinput = StringVar()
    myEntry = Entry(root, textvariable=userinput).pack()

    # Functies
    def pincodefunct():
        try:
            userinputpincode = userinput.get()
            if pincode == eval(userinputpincode):
                Label(root,text='Correct!, een moment geduld AUB',bg='#ddffcc').pack()
                BlinkGroen(int(iterationsGroen),float(speedGroen))
                root.destroy()
                scherm2()
            else:
                Label(root,text='Helaas fout, probeer opnieuw!', bg='#ddffcc').pack()
        except:
            None

    def countdown(count):
        try:
            # change text in label
            aftellen['text'] = count
            if count > 0:
                # call countdown again after 1000ms (1s)
                root.after(1000, countdown, count-1)
            if count <= 0:
                alarmaan()
                Label(root,text='Tijd voorbij!', bg='#ddffcc').pack()

        except:
            None

    # Buttons
    okbutton = Button(root, text='OK', command=pincodefunct,fg='#000000', bg='#cce6ff')
    aftellen = Label(root, bg='#ddffcc')
    aftellen.pack()

    # Buttons positioneren
    okbutton.config(height=2, width=10)
    okbutton.pack()

    # Functie aanroepen en variable vaststellen

    countdown(10)

    # Einde en sluiten
    root.mainloop()

def scherm2():
    # Algemene settings
    root2 = Tk()
    root2.title('Alarm')
    root2.geometry('800x480')
    root2.resizable(width=False, height=False)
    root2.configure(background='#ddffcc')

    # Functies
    def nieuwepincode():
        nwpincode = random.randrange(1000,9999)
        global pincode
        pincode = nwpincode
        Label(root2,text='Je nieuwe pincode is: {}'.format(nwpincode),bg='#ddffcc').pack()

    def terug():
        root2.destroy()
        scherm3()

    buttonRechts = 23
    buttonLinks = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonLinks, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Knop S1
    GPIO.setup(buttonRechts, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Knop S2


    def alarmaan():
        knop()
        root2.destroy()
        scherm1()

    def alarmuit():
        pygame.mixer.init()
        pygame.mixer.music.stop()
        BlinkGroen(int(iterationsGroen),float(speedGroen))


    # Buttons
    nieuwepincodebutton = Button(root2, text='Nieuwe pincode!', command=nieuwepincode, fg='#000000', bg='#cce6ff')
    terugbutton = Button(root2, text='Ik wil terug!', command=terug, fg='white', bg='#ff3333')
    alarmuit = Button(root2, text='Alarm Uit', fg='white', command=alarmuit, bg='#ff3333')
    alarmaan = Button(root2, text='Alarm Aanzetten',fg='white', command=alarmaan, bg='#ff3333')

    # Buttons positioneren
    nieuwepincodebutton.config(height=2, width=20)
    nieuwepincodebutton.pack()
    terugbutton.config(height=2, width=10)
    terugbutton.place(x=200,y=0)
    alarmaan.config(height=2, width=10)
    alarmaan.place(x=400, y=100)
    alarmuit.config(height=2, width=10)
    alarmuit.place(x=300, y=100)

     # Einde en sluiten
    root2.mainloop()

def scherm3():
    # Algemene settings
    root3 = Tk()
    root3.title('Alarm')
    root3.geometry('800x480')
    root3.resizable(width=False, height=False)
    root3.configure(background='#ddffcc')
    Label(root3,text='Vul uw Pincode in:', bg='#ddffcc').pack()

    # Userinputveld
    userinput = StringVar()
    myEntry = Entry(root3, textvariable=userinput).pack()

    # Functies
    def pincodefunct():
        try:
            userinputpincode = userinput.get()
            if pincode == eval(userinputpincode):
                Label(root3,text='Correct!, een moment geduld AUB',bg='#ddffcc').pack()
                BlinkGroen(int(iterationsGroen),float(speedGroen))
                root3.destroy()
                scherm2()
            else:
                Label(root3,text='Helaas fout, probeer opnieuw!', bg='#ddffcc').pack()
        except:
            None

    # Buttons
    okbutton = Button(root3, text='OK', command=pincodefunct,fg='#000000', bg='#cce6ff')
    aftellen = Label(root3, bg='#ddffcc')
    aftellen.pack()

    # Buttons positioneren
    okbutton.config(height=2, width=10)
    okbutton.pack()

    # Einde en sluiten
    root3.mainloop()

scherm3()
