from tkinter import *
window = Tk()

window.title("My GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="This is a Label", font=("Arial", 24))
# my_label.pack(side="left")
my_label.pack()

# my_label["text"] = 'New Text'
my_label.config(text="This is a label")

#Button

# def button_clicked():
#     my_label.config(text="Button got clicked 😁")
# button = Button(text="Click Me", command=button_clicked)
# button.pack()

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=40)
input.insert(END, string='Type to set the label')
input.pack()
# new_text = input.get()
# print(new_text)  --> Nothing is printed here. But Why?

#Text Box

text = Text(height=5, width=30)
text.focus()   #Puts cursor in a text box automatically.
text.insert(END, "Multiline text entry.")
print(text.get("1.0", END)) #"1.0 means the text will be read from the 1st line at the character 0."
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=10, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to= 100, command=scale_used)
scale.pack()

#Check Button
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#Radio Button
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio_button1 = Radiobutton(text="Sirat", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Nishat", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


#List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
names = ["Habibullah", "Nahian", "Noureen", "Sirat", "Nishat"]
for name in names:
    listbox.insert(names.index(name), name)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()