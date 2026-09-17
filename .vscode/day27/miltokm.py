from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


# Button function
def calculate():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    km_result.config(text=round(kilometers, 2))


# Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()