from tkinter import filedialog
import pyqrcode
import os
from tkinter import *
from PIL import Image,ImageTk
qr_path=os.getcwd()+"\myqr.png"

def getVals():
    global s
    s=stringurl.get()
    ur=pyqrcode.create(s)
    ur.png("myqr.png", scale = 6)
    qr_path=os.getcwd()+"\myqr.png"
    image.config(file=f"{qr_path}")

def dwld():
    folder=filedialog.askdirectory()
    cur_path=os.getcwd()
    os.chdir(folder)
    qr=Image.open(f"{qr_path}") 
    qr=qr.save("qrimage.jpg")
    os.chdir(cur_path)
window=Tk()
window.geometry("644x434")
window.title("QR Generator")
text=Label(text="Enter URL to generate QR Code",font="comicsansms 10 bold")
stringurl=StringVar()
url=Entry(textvariable=stringurl)
submit=Button(text="Submit",command=getVals)
image=PhotoImage(file="")
photo=Label(image=image)
text.grid(row=3,column=2)
url.grid(row=5,column=2)
submit.grid(row=10,column=2)
photo.grid()
download=Button(text="Save QR Code",command=dwld)
download.grid()
window.mainloop()

