from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title("Password Generator")
# root.geometry('500x300')

my_password = ""  # initialize as empty

def new_rand(event=None):  # Allow key binding with event
    global my_password
    pw_entry.delete(0, END)
    try:
        pw_length = int(my_entry.get())
        my_password = ""
        for x in range(pw_length):
            my_password += chr(randint(33, 126))
        pw_entry.insert(0, my_password)
    except ValueError:
        pw_entry.insert(0, "Enter a number!")

def clipper():
    root.clipboard_clear()
    root.clipboard_append(my_password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Layout
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)
my_entry.bind('<Return>', new_rand)  # Bind Enter key to password generation

pw_entry = Entry(root, text='', font=('Helvetica', 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
