from tkinter import *
#ques 1:
root = Tk()
label = Label(root,text="Helo World!!").pack()
button= Button(root,text="Quit",command=quit).pack()
root.mainloop()

#ques 2:
root = Tk()
def show():
     print("if you are brother,I am with you, \n and I am here,Flying kiss for clicking")
label = Label(root,text="Helo World!!").pack()
button = Button(root,text="Quit",command=quit).pack()
button2 = Button(root,text="Click me",command=show).pack()
root.mainloop()

#ques 3:

root =Tk()

label = Label(root,text="old text")
def clickf():
    label.config(text="after clicking")

b1 = Button(root,text="Click me to change text",command=clickf)
label.pack()
b1.pack()
root.mainloop()


#ques 4:

root=Tk()
def show():
   ee = v1.get()
   l = Label(root,text=ee).grid(row=2)
v1=IntVar()
bui=Button(root,text="Click",command=show).grid(row=1)
textbox=Entry(root,textvariable=v1).grid(row=0)
root.mainloop()