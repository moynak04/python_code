from tkinter import *

window = Tk()
window.title("Grid Layout")
window.minsize(width=500, height=300)

# Labels
label1 = Label(text="First Name")
label1.grid(row=0, column=0)

label2 = Label(text="Last Name")
label2.grid(row=1, column=0)

# Entry boxes
entry1 = Entry(width=20)
entry1.grid(row=0, column=1)

entry2 = Entry(width=20)
entry2.grid(row=1, column=1)

# Button
button = Button(text="Submit")
button.grid(row=2, column=1)

window.mainloop()