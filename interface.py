from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

#general settings
app = Tk()
app.title("Train the Trainer 1")
app.configure(bg="#00a57d")
app.geometry("640x427")
app.iconbitmap(r"C:\Users\scheppsu\Pictures\CoGent_logo.ico")

#background image
#foto_gent = ImageTk.PhotoImage(Image.open(r"C:\Users\scheppsu\Pictures\640px-Graslei_Ghent.jpg"))
#foto_label = Label(app, image=foto_gent)
#foto_label.place(x=0, y=0)

#input result
font_result = font.Font(family="Comic Sans MS", name="appresultfont", size=15, weight="normal", slant="italic")

def ditinfo():
    info = Label(app, text="Hello "  + input.get(), font=font_result)
    info.grid(row=5, column=1)

#button
font_button = font.Font(family="Arial", name="appbuttonfont", size=20, weight="bold")
DIT = Button(app, text="What is your name?", fg="#b75097", bg="#fdc20c", borderwidth="10", font=font_button, command=ditinfo)
DIT.grid(row=1, column=1)

#input
input = Entry(app)
input.grid(row=1, column=2)

#checkbutton
check = Checkbutton(app, text="checkbutton")
check.grid(row=8, column=1)

#dropdown
keuze = StringVar(app)
keuze.set("Choose your answer")
dropdown = OptionMenu(app, keuze, "ja", "nee", "misschien")
dropdown.grid(row=10, column=1)

app.mainloop()