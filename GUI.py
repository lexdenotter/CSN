# Import
from tkinter import *
import random

pincode = 0000

def scherm1():
    # Algemene settings
    root = Tk()
    root.title('Alarm')
    root.iconbitmap('alarm.ico')
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
                Label(root,text='Correct!', bg='#ddffcc').pack()
                root.iconbitmap('alarm.ico')
                root.destroy()
                scherm2()

            else:
                Label(root,text='Helaas fout, probeer opnieuw!', bg='#ddffcc').pack()
        except:
            None

    # Buttons
    okbutton = Button(root, text='OK', command=pincodefunct,fg='#000000', bg='#cce6ff')

    # Buttons positioneren
    okbutton.config(height=2, width=10)
    okbutton.pack()

    # Einde en sluiten
    root.mainloop()

def scherm2():
    # Algemene settings
    root2 = Tk()
    root2.title('Alarm')
    root2.iconbitmap('alarm.ico')
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
        scherm1()

    # Buttons
    nieuwepincodebutton = Button(root2, text='Nieuwe pincode!', command=nieuwepincode, fg='#000000', bg='#cce6ff')
    terugbutton = Button(root2, text='Ik wil terug!', command=terug, fg='white', bg='#ff3333')

    # Buttons positioneren
    nieuwepincodebutton.config(height=2, width=20)
    nieuwepincodebutton.pack()
    terugbutton.config(height=2, width=10)
    terugbutton.place(x=200,y=0)

     # Einde en sluiten
    root2.mainloop()

scherm1()
