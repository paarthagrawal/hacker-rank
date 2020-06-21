from tkinter import *
root=Tk()

#r=IntVar()
#r.set(2)
pizza=IntVar()
pizza.get()
def clicked(value):
    label=Label(root,text=pizza.get()).pack()
hi=[('pepporoni',1),('cheese',2),('onion',3),('tomato',4)]

for text,mode in hi:
    radio_button1=Radiobutton(root,text=text,variable=pizza,value=mode).pack()

#radio_button1=Radiobutton(root,text='1',variable=r,value=1).pack()
#adio_button2=Radiobutton(root,text='2',variable=r,value=2).pack()

button1=Button(root,text='click me',command=lambda: clicked(pizza.get())).pack()
#label=Label(root,text=r.get()).pack()
root.mainloop()
