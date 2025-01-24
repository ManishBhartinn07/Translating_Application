# #install pip install googletrans
# #textblob

from tkinter import *
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

root = Tk()
root.title("Language Translator")
# root.iconbitmap('C:/Users/HP/Downloads/translator.ico')  # Optional
root.geometry("880x300")

def translate_it():
    # Clear previous text
    translated_text.delete(1.0, END)

    try:
        # Get language keys for the selected languages
        from_language_key = [key for key, value in languages.items() if value == original_combo.get()][0]
        to_language_key = [key for key, value in languages.items() if value == translated_combo.get()][0]

        # Get the original text
        words = original_text.get(1.0, END).strip()
        if not words:
            raise ValueError("Please enter text to translate.")

        # Use googletrans for translation
        translator = Translator()
        translated_words = translator.translate(words, src=from_language_key, dest=to_language_key)

        # Output the translated text
        translated_text.insert(1.0, translated_words.text)

    except Exception as e:
        messagebox.showerror("Language Translator", f"Something went wrong:\n{e}")

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Initialize language list
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Text boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate", font=("Helvetica", 15), command=translate_it)
translate_button.grid(row=0, column=1, pady=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# Comboboxes
original_combo = ttk.Combobox(root, width=50, values=language_list)
original_combo.current(21)  # Default language
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, values=language_list)
translated_combo.current(26)  # Default language
translated_combo.grid(row=1, column=2)

# Clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()

