from tkinter import *
from tkinter import messagebox
import base64
import os
from PIL import ImageTk, Image


def decrypt():
    password=code.get()
    
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("decryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#00bd56")
        

        message=text1.get(1.0 , END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(encode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen1,text="DECRYPTION CODE",font="arial 15 bold",fg="white",bg="#00bd56").place(x=10,y=3)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)

    elif password == "":
        messagebox.showerror("Error","Input Password")

    elif password !="1234":
        messagebox.showerror("Error","Invalid password. password must match with admin password")
    
    


def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0 , END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPTION CODE",font="arial 15 bold",fg="white",bg="#ed3833").place(x=10,y=3)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=3)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)

    elif password == "":
        messagebox.showerror("Error","Input Password")

    elif password !="1234":
        messagebox.showerror("Error","Invalid password!!! Password must match with admin password")










def main_screen():
    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("700x500+150+180")
    screen.title("CRYPTOGRAPHY")
    screen.resizable(False,False)
    screen.configure(bg="#95B9C7")
    

    


    
     # Create an object of tkinter ImageTk
    #img = ImageTk.PhotoImage(Image.open("Picsart_22-12-31_20-38-03-996.jpg"))

    # Create a Label Widget to display the text or Image
    #label = Label(screen, image = img)
   # label.pack() 

#________________________________________________________



        # Load the image
    image=Image.open('Picsart_22-12-31_20-53-56-468.jpg')

    # Resize the image in the given (width, height)  #h=350
    img=image.resize((690, 493))


    # Conver the image in TkImage
    my_img=ImageTk.PhotoImage(img)

    # Display the image with label
    label=Label(screen, image=my_img)
    label.pack()





    #_________-icon__________

    image_icon=PhotoImage(file="icon.png")
    screen.iconphoto(False,image_icon)







    def reset():
        code.set("")
        text1.delete(1.0 , END)
        


    Label(text="ENTER YOUR MESSAGE",bg="black",fg="white",font=("ucida 20 bold")).place(x=200,y=10)
    text1=Text(font="ucida 20 bold italic",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=20,y=55,width=660,height=190)    #width=355,height=100

    Label(text="Enter A Secret Key To Encrypt And Decrypt Your Message",bg="black",fg="white",font=("times 16 bold")).place(x=100,y=255)
    code=StringVar()
    Entry(textvariable=code,width=20,bd=0,font=("arial",25),show="*").place(x=182,y=300)

    #cryptography
    Label(text="( ADMIN PASSWORD )",bg="black",fg="white",font=("times 11 bold")).place(x=12,y=308)



    Button(text="ENCRYPT",height="2",width="23",bg="#ed3833",fg="white",bd="5",command=encrypt).place(x=180,y=375) #180 400
    Button(text="DECRYPT",height="2",width="23",bg="#00bd56",fg="white",bd='5',command=decrypt).place(x=370,y=375) #370 400
    Button(text="RESET",height="2",width="50",bg="#1089ff",fg="white",bd='5',command=reset).place(x=180,y=440)     #180 450
    

    # Button for closing
    exit_button = Button(screen, text="Exit",bg="red",fg="white",font="arial 15 bold",bd='5',command=screen.destroy).place(x=624,y=440)
    #exit_button.pack()
















    screen.mainloop()

main_screen()
