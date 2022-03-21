from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
# Initiation
root = Tk()
root.title('Translator')
root.iconbitmap('screenshot.ico')
root.geometry("850x370")


# ################################# Functions ########################################
# To translate
def translate_it():
    # To clear the translation box
    global from_language_key, to_language_key
    translated_text.delete(1.0, END)
    try:
        # Get the key for the original language
        for key, value in languages.items():
            if value == original_combo.get():
                from_language_key = key

            # Get the key for the end language
        for key, value in languages.items():
            if value == translated_combo.get():
                to_language_key = key

        # To turn original text into a textblob
        words = textblob.TextBlob(original_text.get(1.0, END))
            
        # To translate
        words = words.translate(from_lang=from_language_key, to=to_language_key)

        # To show output
        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)


# To delete
def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)


# To copy
def copy(e):
    root.clipboard_clear()
    root.clipboard_append(translated_text.get(1.0, END))


# Get languages
languages = googletrans.LANGUAGES
language_list = list(languages.values())
##########################################################################

# ############################ GUI #######################################
# Original language  box
original_text = Text(root, height=10, width=40, font=18)
original_text.grid(row=0, column=0, pady=20, padx=10)
# Translation language box
translated_text = Text(root, height=10, width=40, font=18)
translated_text.grid(row=0, column=2, pady=20, padx=10)
# Combo for language to translate
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)
# Combo for translation languages
translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)
# Button for initiating translation
translated_button = Button(root, text="💬", font=("Helvetica", 24), command=translate_it)
translated_button.grid(row=0, column=1, padx=10)
# Copy Button
copy_button = Button(root, text="📋", font=("Helvetica", 24), command=lambda: copy(1))
copy_button.grid(row=1, column=1, pady=10, padx=10)
# clear button
clear_button = Button(root, text="🗑", font=("Helvetica", 24), command=clear)
clear_button.grid(row=2, column=1)
################################################################################################
# Loop
root.mainloop()
