
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=10)
input_text = Entry(width=7)
input_text.grid(column = 1,row=0)
miles_label = Label(text="Miles")
miles_label.grid(column = 2,row = 0)
output_label = Label(text="")
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
km_output_label = Label(text="0")
km_output_label.grid(column=1, row=2)
km_label = Label(text="km")
km_label.grid(column=2, row=2)


def convert_miles_to_km():
    km = float(input_text.get())*1.609
    km_output_label.config(text=f"{km}")

calculate = Button(text="Calculate", command=convert_miles_to_km)
calculate.grid(column=1, row=3)
window.mainloop()