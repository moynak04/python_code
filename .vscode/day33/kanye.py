from tkinter import *
import requests

# ---------------------------- GET QUOTE ------------------------------- #

def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()

    data = response.json()
    quote = data["quote"]

    canvas.itemconfig(quote_text, text=quote)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Background
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Quote
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes Here",
    width=250,
    font=("Arial", 20, "bold"),
    fill="black"
)

canvas.grid(row=0, column=0)

# Kanye button
kanye_img = PhotoImage(file="kanye.png")

button = Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote
)

button.grid(row=1, column=0)

window.mainloop()