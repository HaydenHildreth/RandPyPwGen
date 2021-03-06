import os
import string
import secrets
import tkinter.messagebox
import pyperclip
import tkinter as tk

window = tk.Tk()
window.title('RandPyPwGen v.0.1')
window.geometry("800x600")
name = os.getlogin()
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = ""
pw_len = 0
entry_len = tk.StringVar()


def click():
    global password
    global pw_len
    try:
        pw_len = int(entry_len.get())
        if pw_len > 100 or pw_len <= 0:
            raise RuntimeError

        password = ''.join(secrets.choice(alphabet) for i in range(pw_len))
        print_pw.configure(text=f"Your password is {password}")
    except ValueError:
        tkinter.messagebox.showerror(title="Invalid input", message="Enter an integer...")
    except RuntimeError:
        tkinter.messagebox.showerror(title="Invalid input", message="Number must be positive and under 101 characters")


def copy():
    global password
    pyperclip.copy(password)


greeting = tk.Label(window, text=f"Greetings {name}.")
greeting.grid(row=0, column=0, sticky=tk.W)
t = tk.Label(window, text="Please input desired password length:")
t.grid(row=1, column=1, sticky=tk.E + tk.W)
input_text = tk.Entry(window, textvariable=entry_len)
input_text.grid(row=1, column=2, sticky=tk.E + tk.W)
print_pw = tk.Label(window, text=f"Your password is: {password}")
print_pw.grid(row=1, column=1, sticky=tk.E + tk.W)
sendBtn = tk.Button(window, text="Generate!", command=click)
copyBtn = tk.Button(window, text="Copy!", command=copy)
sendBtn.grid(row=2, column=1, sticky=tk.E + tk.W)
copyBtn.grid(row=2, column=2, sticky=tk.E + tk.W)
window.mainloop()
