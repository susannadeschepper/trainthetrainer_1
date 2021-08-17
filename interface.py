from tkinter import *

app = Tk()
app.title("Tkinter fun")
app.configure(bg="green")
app.geometry("400x300")

def ditinfo():
    info = Label(app, text="Hello "  + input.get(), font=("Helvetica", 15, "italic"))
    info.grid(row=5, column=1)

DIT = Button(app, text="What is your name?", fg="green", bg="yellow", borderwidth="10", font=("Arial", 18, "bold"), command=ditinfo)
DIT.grid(row=1, column=1)

input = Entry(app)
input.grid(row=1, column=2)

check = Checkbutton(app, text="checkbutton")
check.grid(row=8, column=1)

keuze = StringVar(app)
keuze.set("Choose your answer")
dropdown = OptionMenu(app, keuze, "ja", "nee", "misschien")
dropdown.grid(row=10, column=1)


app.mainloop()