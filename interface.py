from tkinter import *
from tkinter import font

#general settings
app = Tk()
app.title("Train the Trainer 1")
app.configure(bg="#00a57d")
app.geometry("640x427")
#app.iconbitmap(r"C:\Users\scheppsu\Pictures\CoGent_logo.ico")

font_gen = font.Font(family="Lucida Sans", name="appgenfont", size=10, weight="normal")
font_result = font.Font(family="Lucida Sans", name="appresultfont", size=10, weight="normal", slant="italic")
font_button = font.Font(family="Arial Narrow", name="appbuttonfont", size=12, weight="bold")
font_dropdown = font.Font(family="Arial Narrow", name="appdropdownfont", size=10, weight="normal")
font_check = font.Font(family="Arial Narrow", name="appcheckfont", size=8, weight="normal")

#checkbutton T&C
is_checked = IntVar()


def deleteinput():
    name.delete(0,END)
    favourite.delete(0,END)


def userinput():
    if is_checked.get():
        #welcome text
        info = Label(app, text="Welcome, " + name.get(), font=font_result, bg="#00a57d")
        info.grid(row=5, column=0)
        options()
    else:
        pass


def options():
    # dropdown
    choice = StringVar(app)
    choice.set("How can we help you?")
    dropdown = OptionMenu(app, choice, *OptionList)
    dropdown.config(font=font_dropdown, padx=5, pady=5)
    dropdown.grid(row=6, column=0)

    label_test = Label(app, text="", font=font_result, bg="#00a57d")
    label_test.grid(row=7, column=1)
    def callback(*args):
       label_test.configure(text="You chose: {}".format(choice.get()))
    choice.trace("w", callback)


#input
ask_name = Label(app, text="My name: ", padx=10, pady=10, bg="#00a57d", font=font_gen)
ask_name.grid(row=0, column=0)
name = Entry(app, width=35)
name.insert(END, 'your name')
name.grid(row=0, column=1)
ask_favourite = Label(app, text="My favourite designer: ", bg="#00a57d", padx=10, pady=10, font=font_gen)
ask_favourite.grid(row=1, column=0)
favourite = Entry(app, width=35)
favourite.insert(END, 'your favourite')
favourite.grid(row=1, column=1)

#checkbutton
check = Checkbutton(app, text="I've read the terms and conditions", onvalue=1, offvalue=0, variable=is_checked, bg="#00a57d", font=font_check)
check.grid(row=2, column=1)

#submit button
submit = Button(app, text="tell us about yourself", fg="#b75097", bg="#fdc20c", borderwidth="3", width="20", font=font_button, command=userinput)
submit.grid(row=3, column=1)

#clear button
clear = Button(app, text="clear", bg="#b75097", fg="#fdc20c", width=20, font=font_button, command=deleteinput)
clear.grid(row=4, column=1)

#list of options
OptionList=[
    "I'm looking for works by " + favourite.get(),
    "I want to submit information on " + favourite.get(),
    "I just want to explore and learn"
]

app.mainloop()