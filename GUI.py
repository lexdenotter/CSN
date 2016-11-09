# Import
from tkinter import *
import random

# Algemene settings
root = Tk()
root.title('Alarm')
root.iconbitmap('alarm.ico')
root.geometry('800x480')
root.configure(background='#66ccff')

# Userinput
userinput = StringVar()
myEntry = Entry(root, textvariable=userinput).pack()

file = open('pincodefile.txt', 'r+')
pincode = file.readline()

# Functies
#pincode inlezen uit bestand en opslaan in de var pincode
with open('pincodefile.txt', 'r+') as bestand:
    pin = bestand.read()
    if bestand == '':
        bestand.write('0000')

def nieuwepincode():
    nwpincode = random.randrange(1000,9999)
    global pincode
    pincode = nwpincode
    Label(root,text='Je nieuwe pincode is: {}'.format(nwpincode)).pack()
    #code om pincode aan te passen
    file.flush()
    file.writelines(str(nwpincode))
    file.close()

def pincodefunct():
    try:
        userinputpincode = userinput.get()
        if pincode == str(userinputpincode):
            Label(root,text='Correct!').pack()
        else:
            Label(root,text='Helaas fout, probeer opnieuw!').pack()
    except:
        print('fout')

# Buttons


okbutton = Button(root, text='OK', command=pincodefunct,fg='red', bg='blue').pack()
pincodebutton = Button(root, text='Nieuwe pincode!', command=nieuwepincode, fg='red', bg='blue').pack()


root.mainloop()
