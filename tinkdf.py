from tkinter import *
from tkinter import ttk

window = Tk()

def kgToPounds():
    print("KM success")
    Pound = float(e1Value.get())*2.20462

    t1.delete("1.0", END)
    t1.insert(END, Pound)

    
    
    Grams = float(e1Value.get())*1000

    t2.delete("1.0", END)
    t2.insert(END, Grams)


    Ounces = float(e1Value.get())*35.274

    t3.delete("1.0", END)
    t3.insert(END, Ounces)

b1=Button(window,text="convert",command=kgToPounds,bg="green",fg="white")
b1.grid(column=0,row=1)

e1Value=StringVar() #input box 
e1 = Entry(window, textvariable=e1Value)
e1.grid(column=0,row=0)

t1=Text(window, height=1, width=20)
t1.grid(column=2, row=1)

t2=Text(window,height=1, width=20)
t2.grid(column=2, row=3)

t3=Text(window, height=1, width=20)
t3.grid(column=2,row=4)

h1= Label(window,text="ounces")
h1.grid(column=4,row=4)

h1= Label(window,text="pounds")
h1.grid(column=4,row=1)

h1= Label(window,text="grams")
h1.grid(column=4,row=3)

h1= Label(window,text="insert kg's here")
h1.grid(column=1,row=0)
window.mainloop()



