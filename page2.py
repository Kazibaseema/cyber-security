
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb

ws = Tk()
ws.geometry('700x500+150+180')
ws.resizable(False,False)
ws.title('Steganography')
#ws['bg']='#95b9c7'
f = ("Times bold", 10)


# Load the image
image=Image.open('Picsart_23-01-01_16-49-37-311.jpg')

# Resize the image in the given (width, height)  #h=350
img=image.resize((690, 500))


# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(ws, image=my_img)
label.pack()








 
def nextPage():
    ws.destroy()
    import page3


def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG File","*png"),
                                                  ("JPG File","*.jpg"),("All file","*txt")))
                                        
                                        
                                                 
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename), message)

def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)



def save():
    secret.save("SECRET_DATA.png")


#___________________icon__________________


image_icon=PhotoImage(file="icon.png")
ws.iconphoto(False,image_icon)

#_________________logo__________________

#logo=PhotoImage(file="")
#Label(ws,image=logo,bg="red").place(x=10,y=0)

Label(ws,text="STEGANOGRAPHY",bg="black",fg="white",font="arial 25 bold").place(x=15,y=20)

#__________creating first frame_____________

f=Frame(ws,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)   

lbl=Label(f,bg="black")
lbl.place(x=40,y=20)


#_______________creating second frame______________

frame2=Frame(ws,bd=3,bg="white",width=340,height=280,relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 17",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#_____________creating third frame______________

frame3=Frame(ws,bd=3,bg="#000080",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",bd='5',command=showimage).place(x=20,y=20)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",bd='5',command=save).place(x=180,y=20)
Label(frame3,text="Picture , Image , Photo File",bg="#000080",fg="white").place(x=12,y=5)   


#______________creating fouth frame_________________



frame4=Frame(ws,bd=3,bg="#000080",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="HideData",width=10,height=2,font="arial 14 bold",bd='5',relief=RAISED,command=Hide).place(x=20,y=20)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",bd='5',relief=RAISED,command=Show).place(x=180,y=20)
Label(frame4,text="Picture , Image , Photo File",bg="#000080",fg="white").place(x=12,y=5)





Button(
    ws, 
    text="CLICK HERE TO ENCRYPT AND DECRYPT MSG",font="arial 8 bold",command=nextPage).place(x=442,y=473)

ws.mainloop()
