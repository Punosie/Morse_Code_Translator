import customtkinter as ctk
from PIL import Image, ImageTk
from app import encrypt, decrypt

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

def convert():
    morse_value = text_morse.get("1.0", "end-1c")
    text_value = text_text.get("1.0", "end-1c")

    if morse_value:
        decrypted_text = decrypt(morse_value)
        text_text.delete("1.0", "end")         
        text_text.insert("1.0", decrypted_text)
    elif text_value:
        encrypted_morse = encrypt(text_value)
        text_morse.delete("1.0", "end")         
        text_morse.insert("1.0", encrypted_morse)

# Window Configuration
root = ctk.CTk()
root.geometry('500x350')
root.title("Morse Code Translator")

default_font = ('Helvetica', 10)
ctk.CTkFont(default_font)

frame_left = ctk.CTkFrame(master=root)
frame_left.grid(row=0, column=0, pady=20, padx=10)

frame_right = ctk.CTkFrame(master=root)
frame_right.grid(row=0, column=1, pady=20, padx=10)

label_morse = ctk.CTkLabel(master=frame_left, text='Morse Code')
label_morse.grid(row=0, column=0, pady=0, padx=10)

text_morse = ctk.CTkTextbox(master=frame_left)
text_morse.grid(row=1, column=0, pady=5, padx=10)

label_text = ctk.CTkLabel(master=frame_right, text='Text')
label_text.grid(row=0, column=0, pady=0, padx=10)

text_text = ctk.CTkTextbox(master=frame_right)
text_text.grid(row=1, column=0, pady=5, padx=10)

button = ctk.CTkButton(master=root, text='Convert', command=convert)
button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
