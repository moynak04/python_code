from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Dialog Box Example")
window.minsize(width=500, height=300)


def show_message():
    messagebox.showinfo(title="Information", message="Hello Moynak!")


button = Button(text="Click Me", command=show_message)
button.pack()

window.mainloop()