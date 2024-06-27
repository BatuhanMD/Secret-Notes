from tkinter import *
from PIL import Image, ImageTk

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

title_label = Label("Enter Your Title")
title_label.pack()

title_entry = Entry()
title_entry.pack()

















window.mainloop()
