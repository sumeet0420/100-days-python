from tkinter import *
from tkinter import Label

window = Tk()

window.title('This is a title')

window.minsize(width=600, height=600)

##Creating first name Label
first_name: Label = Label(text="First Name", font=("Arial",22,"bold"))
first_name.pack(side="left", padx=5)


def change_label():
    first_name['text']="Changed"


button = Button(text="Click Me!", command=change_label)
button.pack()






window.mainloop()