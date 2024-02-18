from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(width=500, height=250, padx=20, pady=10)

def calculate():
    miles = float(input.get())
    miles = miles * 1.609
    result = str(miles)
    km_result_label.config(text=result)

input = Entry()
input.grid(column=1, row=0, padx=5, pady=5)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=5, pady=5)

mile_label = Label(text="Mile")
mile_label.grid(column=2, row=0, padx=5, pady=5)

km_label = Label(text="Km")
km_label.grid(column=2, row=1, padx=5, pady=5)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2, padx=5, pady=5)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1, padx=5, pady=5)

window.mainloop()