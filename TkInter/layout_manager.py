from tkinter import *
window = Tk()

window.title("My GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

my_label = Label(text="This is a Label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(text="This is a label", padx=10, pady=10)

button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

#Entry

input = Entry(width=40)
input.insert(END, string='Type to set the label')
input.grid(column=3, row=2)

window.mainloop()