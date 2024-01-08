from tkinter import *
from tkinter import ttk
import tkinter as tk
from googletrans import Translator, LANGUAGES


def on_button_click():
    translator = Translator()
    translator.detect(entered_language_combo_box.get())

    translated_text = translator.translate(text=main_text.get(1.0, END), src=entered_language_combo_box.get(), dest=translated_language_combo_box.get()).text
    translated_text_box.delete(1.0, END)
    translated_text_box.insert(END, translated_text)
    

root = Tk()

root.geometry("300x400")
root.title("Google Translate")
root.config(background='skyblue')

label = tk.Label(root, text="Google Translate")
label.config(background='skyblue')
label.pack(pady=10)

label = tk.Label(root, text="Enter your text to translate")
label.config(background='skyblue')
label.pack(pady=10)

main_text = tk.Text(root, height=1, width=30)
main_text.pack(pady=5)

language_list = list(LANGUAGES.values())

label = tk.Label(root, text="Select Entered language")
label.config(background='skyblue')
label.pack(pady=10)

entered_language_combo_box = ttk.Combobox(root, value=language_list)
entered_language_combo_box.set("Select language")
entered_language_combo_box.pack(pady=10)


label = tk.Label(root, text="Select Language to Translate")
label.config(background='skyblue')
label.pack(pady=10)

translated_language_combo_box = ttk.Combobox(root, value=language_list)
translated_language_combo_box.set("Select language")
translated_language_combo_box.pack(pady=10)

translate_language = translated_language_combo_box.get()


translated_language_button = Button(root, text="Translate", relief=RAISED, command=on_button_click)
translated_language_button.pack()


translated_text_box = tk.Text(root, height=10, width=30)
translated_text_box.pack(pady=5)

root.mainloop()
