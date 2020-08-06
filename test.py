from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("350x350")
image=Image.open("./image_files/moribdly_obese.png")

photo=ImageTk.PhotoImage(image)
Label=Label(root,text="Yes",image=photo)
Label.pack()
root.mainloop()







