from tkinter import *
from PIL import Image,ImageTk
import datetime
import time
import pygame
from pygame import mixer
import threading
from tkinter import messagebox
root=Tk()
root.title("ALARAM CLOCK")
root.configure(bg='white')
root.geometry("650x400")
head=Label(root,text="ALARAMCLOCK",fg="red",font=('comic sans',20))
head.grid(row=0,columnspan=3,pady=10)
alaramtime=StringVar()
msgi=StringVar()
mixer.init()
def th():
	t1 = threading.Thread(target=ala, args=())
	t1.start()

def ala():
    a=altime.get()
    Alaramt=a
    currenttime=time.strftime("%H:%M")
    while Alaramt!=currenttime:
        currenttime=time.strftime("%H:%M")
    if Alaramt==currenttime:
         mixer.music.load('tone.mp3')
         mixer.music.play()
         msg = messagebox.showinfo('INFO', f'{msgi.get()}')
         if msg=='ok':
            mixer.music.stop()
clockimage=ImageTk.PhotoImage(Image.open("alaram2.png"))
image=Label(root,image=clockimage)
image.grid(rowspan=4,column=0)
inputt=Label(root,text="Input Time",fg="red",font=('comic sans',18))
inputt.grid(row=1,column=1)
altime=Entry(root,textvariable=alaramtime,font=('comic sans',18))
altime.grid(row=1,column=2)
msg=Label(root,text="MESSAGE📧",fg="red",font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)
msginput=Entry(root,textvariable=msgi,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)
submit=Button(root,text="SUBMIT",fg="red",command=th,font=('comic sans',18))
submit.grid(row=4,column=1,columnspan=2)
root.mainloop()
