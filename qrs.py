import pyqrcode
import os
from tkinter import *
from PIL import Image,ImageTk
def getVals():
    global s
    s=stringurl.get()
    ur=pyqrcode.create(s)
    ur.png("myqr.png", scale = 6)
    qr_path=os.getcwd()+"\myqr.png"
    image.config(file=f"{qr_path}")
    
window=Tk()
window.geometry("644x434")
window.title("QR Generator")
text=Label(text="Enter URL to generate QR Code",font="comicsansms 19 bold")
stringurl=StringVar()
url=Entry(textvariable=stringurl)
submit=Button(text="Submit",command=getVals)
qr_path=os.getcwd()+"\myqr.png"
image=PhotoImage(file="")
photo=Label(image=image)
text.grid()
url.grid()
submit.grid(row=2,column=0)
photo.grid()
window.mainloop()

