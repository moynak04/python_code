from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# "is equal to" label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Result
km_result = Label(text="0")
km_result.grid(column=1, row=1)

# Kilometers label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)

window.mainloop()