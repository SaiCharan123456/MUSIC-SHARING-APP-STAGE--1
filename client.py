import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def musicWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x330")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select Song", bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window, height=10,width = 39, activestyle = "dotbox",bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10,y=18)
    
    scrollbarl = Scrollbar(listbox)
    scrollbarl.place(relheight=1, relx=1) 
    scrollbarl.config(command=listbox.yview)

    PlayButton = Button(window, text="Play", width=10, bd=1,bg="SkyBlue",font=("Calibri",10))
    PlayButton.place(x=30,y=200)

    Stop = Button(window, text="Stop",bd=1,width=10,bg="SkyBlue", font=("Calibri",10))
    Stop.place(x=200,y=200)

    Upload = Button(window, text="Upload",width=10, bd=1,bg='SkyBlue', font=("Calibri", 10))
    Upload.place(x=30,y=250)

    Download = Button(window, text="Download",width=10,bd=1,bg='SkyBlue', font=("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel = Label(window, text="", fg="blue", font=("Calibri",8))
    infoLabel.place (x=4, y=280)
    
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()