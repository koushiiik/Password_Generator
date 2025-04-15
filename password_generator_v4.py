from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title("★ Password Generator")
root.geometry('500x550')
root.configure(bg="#f0f5f9")

my_password = ""

def new_rand(event=None):
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
    messagebox.showinfo("✅ Copied", "Password copied to clipboard!")

def save_to_file():
    note = note_entry.get()
    if not my_password:
        messagebox.showwarning("⚠️ Warning", "Generate a password first!")
        return
    if not note:
        messagebox.showwarning("⚠️ Warning", "Please enter a note (e.g., Gmail, Instagram)")
        return
    with open("saved_passwords.txt", "a") as file:
        file.write(f"The password for {note} is: {my_password}\n")
    messagebox.showinfo("✅ Saved", f"Password saved with note: {note}")
    note_entry.delete(0, END)

# Title
title_label = Label(root, text="★ Password Generator", font=("Helvetica", 20, "bold"), bg="#f0f5f9", fg="#0b3d91")
title_label.pack(pady=10)

# Character length
lf = LabelFrame(root, text="How Many Characters?", font=("Helvetica", 12, "bold"), bg="#e3f2fd", fg="#0b3d91", padx=10, pady=10, bd=3, relief=GROOVE)
lf.pack(pady=15)

my_entry = Entry(lf, font=("Helvetica", 20), width=10, justify="center", bd=2, relief=RIDGE)
my_entry.pack(pady=10)
my_entry.bind('<Return>', new_rand)

# Password display
pw_entry = Entry(root, font=('Helvetica', 20, 'bold'), bd=2, bg="#ffffff", fg="#333", justify="center", relief=SUNKEN)
pw_entry.pack(pady=20, ipady=5, ipadx=5)

# Note entry
note_label = Label(root, text="Add a note (e.g., Instagram):", font=("Helvetica", 12), bg="#f0f5f9", fg="#0b3d91")
note_label.pack(pady=(10, 2))

note_entry = Entry(root, font=("Helvetica", 14), bd=2, relief=RIDGE, justify="center")
note_entry.pack(pady=(0, 15))

# Buttons
my_frame = Frame(root, bg="#f0f5f9")
my_frame.pack(pady=10)

my_button = Button(my_frame, text="🎲 Generate Password", command=new_rand, font=("Helvetica", 12, "bold"), bg="#43a047", fg="white", padx=20, pady=5, bd=0)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="📋 Copy", command=clipper, font=("Helvetica", 12, "bold"), bg="#1e88e5", fg="white", padx=20, pady=5, bd=0)
clip_button.grid(row=0, column=1, padx=10)

save_button = Button(root, text="💾 Save to File", command=save_to_file, font=("Helvetica", 12, "bold"), bg="#fb8c00", fg="white", padx=20, pady=5, bd=0)
save_button.pack(pady=10)

# Footer
footer = Label(root, text="Made with ❤️ by You", font=("Helvetica", 10), bg="#f0f5f9", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
