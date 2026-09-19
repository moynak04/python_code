from tkinter import *

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)


# ---------------------------- FUNCTIONS ------------------------------- #

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result.config(text=f"{km:.2f}")


# ---------------------------- UI ELEMENTS ------------------------------- #

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label - Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label - Is equal to
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Label - Result
km_result = Label(text="0")
km_result.grid(column=1, row=1)

# Label - Kilometers
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(
    text="Calculate",
    command=miles_to_km
)
calculate_button.grid(column=1, row=2)


# ---------------------------- MAIN LOOP ------------------------------- #

window.mainloop()