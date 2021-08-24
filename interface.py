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
font_result = font.Font(family="Comic Sans MS", name="appresultfont", size=10, weight="normal", slant="italic")

def ditinfo():
    info = Label(app, text="Welcome, " + name.get(), font=font_result, bg="#00a57d")
    info.grid(row=4, column=1)
    #dropdown
    keuze = StringVar(app)
    keuze.set("What can we help you with today?")
    dropdown = OptionMenu(app, keuze, "I'm looking for works by " + favourite.get(), "I want to submit information on " + favourite.get(), "I just want to explore and learn")
    dropdown.grid(row=5, column=1)
    #checkbutton
    check = Checkbutton(app, text="I've read the terms and conditions", padx=20)
    check.grid(row=6, column=1)


#input
ask_name = Label(app, text="My name : ", padx=10, pady=10, bg="#00a57d")
ask_name.grid(row=0, column=0)
name = Entry(app)
name.grid(row=0, column=1)
ask_favourite = Label(app, text="My favourite designer: ", bg="#00a57d")
ask_favourite.grid(row=1, column=0)
favourite = Entry(app)
favourite.grid(row=1, column=1)

#button
font_button = font.Font(family="Arial", name="appbuttonfont", size=10, weight="bold")
DIT = Button(app, text="tell us about yourself", fg="#b75097", bg="#fdc20c", borderwidth="1", font=font_button, command=ditinfo)
DIT.grid(row=3, column=2)

app.mainloop()