from tkinter import *
from random import randint

root=Tk()
root.title("Password Generator")
#root.geometry('500*300')

my_password =chr(randint(33,126))
def new_rand():
    #Clear our Entry box
    pw_entry.delete(0,END)

    #Get Pw length and covert to integer
    pw_length=int(my_entry.get())

    #create a variable  to hold our password
    my_password=""

    #loop through password length
    for x in range(pw_length):
        my_password +=chr(randint(33,126))
    #output password on screen
    pw_entry.insert(0,my_password)

#copy to clipboard
def clipper():
    #clear the clipboard
    root.clipboard_clear()
    #copy to clipboard
    root.clipboard_append(my_password)

#Label Frame
lf=LabelFrame(root,text="How Many Characters?")
lf.pack(pady=20)

#Create Entry Box to Designate Number of Characters
my_entry=Entry(lf,font=("helvetica",24))
my_entry.pack(pady=20,padx=20)

#create entry box for our return password
pw_entry=Entry(root, text='',font=('Helvetica',24),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)

#create a frame for our button
my_frame=Frame(root)
my_frame.pack(pady=20)

#create our button
my_button=Button(my_frame,text="Generate Password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text="Copy To Clipbaord",command=clipper)
clip_button.grid(row=0,column=1,padx=10)

root.mainloop()