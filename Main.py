from tkinter import *
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

#Window
window = Tk()
window.minsize(width=250,height=500)
window.title("Secret Notes")

#Logo / Image
image = Image.open('top_secret.png')
image = ImageTk.PhotoImage(image)
image_label = Label(window, image=image)
image_label.pack(pady=10)

#Title label and entry
title_label = Label(text="Enter Your Title",font=("Arial",9,"bold"))
title_label.pack(pady=5)
title_entry = Entry()
title_entry.pack()

#Secret label and text
secret_label = Label(text="Enter Your Secret",font=("Arial",9,"bold"))
secret_label.pack(pady=5)
secret_text = Text(width=20,height=10)
secret_text.pack()

#Master key label and entry
master_label = Label(text="Enter Master Key",font=("Arial",9,"bold"))
master_label.pack(pady=5)
master_entry = Entry(show="*")
master_entry.pack()

#Fernet key and object
key = Fernet.generate_key()
f = Fernet(key)

smaster_key = None

# Button functions
def encrypt():
    global smaster_key
    if smaster_key is None:
        smaster_key = master_entry.get()
    secret_txt = secret_text.get("1.0", END)
    encrypted_msg = f.encrypt(secret_txt.encode())
    with open('mysecret.txt', 'a') as file:
        file.write(title_entry.get() + '\n')
        file.write(encrypted_msg.decode('utf-8') + '\n')

def decrypt():
    global smaster_key
    if smaster_key is None:
        smaster_key = master_entry.get()
    encrypted_msg = secret_text.get("1.0", END)
    try:
        decoded_msg = f.decrypt(encrypted_msg.encode('utf-8'))
        secret_text.delete("1.0", END)
        secret_text.insert(END, decoded_msg.decode('utf-8'))
    except Exception as e:
        print("Decryption failed:", str(e))

#Save and Encrypt Button
button1 = Button(text="Save and Encrypt",command=encrypt)
button1.pack(pady=10)

#Decrypt Button
button2 = Button(text="Decrypt",command=decrypt)
button2.pack(pady=2)









window.mainloop()
