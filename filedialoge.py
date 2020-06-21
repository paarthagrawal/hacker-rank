from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
def file():
    root.filename=filedialog.askopenfilename()
    #my_label=Label(text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()

btn=Button(root,text='click me',command=file).pack()
btn1=Button(root,text='eliminate',command=quit).pack()
root.mainloop()
