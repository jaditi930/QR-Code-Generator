from tkinter import filedialog
import pyqrcode
import os
from tkinter import *
from PIL import Image
qr_path=os.getcwd()+"\myqr.png"
global c
c=1

def getVals():
    global s
    s=stringurl.get()
    ur=pyqrcode.create(s)
    ur.png("myqr.png", scale = 6)
    qr_path=os.getcwd()+"\myqr.png"
    image.config(file=f"{qr_path}")
    submit.place_forget()
    photo.place(relx=0.32,rely=0.5)
    download=Button(text="Save QR Code",command=dwld,font="comicsansms 15 bold",fg="black",bg="light green")
    download.place(relx=0.35,rely=0.85)

def dwld():
    global c
    folder=filedialog.askdirectory()
    cur_path=os.getcwd()
    os.chdir(folder)
    qr=Image.open(f"{qr_path}") 
    qr.save(f"qrimage-{c}.jpg")
    c+=1
    os.chdir(cur_path)


window=Tk()
window.geometry("844x634")
window.title("QR Generator")
title=Label(text="QR Code Generator",font="comicsansms 35 bold",fg="red",bg="yellow")
title.place(relx=0.15,rely=0.1)
text=Label(text="Enter URL to generate QR Code",font="comicsansms 20 bold")
stringurl=StringVar()
url=Entry(textvariable=stringurl)
submit=Button(text="Submit",font="comicsansms 15 bold",command=getVals,fg="black",bg="light green")
image=PhotoImage(file="")
photo=Label(image=image,width=200,height=200)
text.place(relx=0.15,rely=0.3)
url.place(relx=0.3,rely=0.45,width=250)
submit.place(relx=0.4,rely=0.55)
window.mainloop()

