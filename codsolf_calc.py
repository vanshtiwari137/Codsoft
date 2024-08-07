import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("400x510")
root.resizable(False,False)
root.configure(bg="black")

eq=""
def show(value):
    global eq
    eq = eq + value
    lr.config(text=eq)

def clear():
    global eq
    eq=""
    lr.config(text=eq)

def calculate():
    global eq
    if eq != "":
        result = eval(eq)
    else:
        print("Error")

    lr.config(text=result)

lr = Label(root,text="",font=('arial',30,'bold'),width=25,height=2)
lr.pack()

Button(root,text="C",font=('arial',15,'bold'),width=6,height=2,command=lambda: clear()).place(x=10,y=110)
Button(root,text="/",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("/")).place(x=110,y=110)
Button(root,text="%",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("%")).place(x=210,y=110)
Button(root,text="+",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("+")).place(x=310,y=110)

Button(root,text="7",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("7")).place(x=10,y=190)
Button(root,text="8",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("8")).place(x=110,y=190)
Button(root,text="9",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("9")).place(x=210,y=190)
Button(root,text="-",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("-")).place(x=310,y=190)

Button(root,text="4",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("4")).place(x=10,y=270)
Button(root,text="5",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("5")).place(x=110,y=270)
Button(root,text="6",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("6")).place(x=210,y=270)
Button(root,text="*",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("*")).place(x=310,y=270)

Button(root,text="1",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("1")).place(x=10,y=350)
Button(root,text="2",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("2")).place(x=110,y=350)
Button(root,text="3",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("3")).place(x=210,y=350)
#Button(root,text="/",font=('arial',10,'bold'),width=9,height=3).place(x=310,y=340)

Button(root,text="00",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("00")).place(x=10,y=430)
Button(root,text="0",font=('arial',15,'bold'),width=6,height=2,command=lambda: show("0")).place(x=110,y=430)
Button(root,text=".",font=('arial',15,'bold'),width=6,height=2,command=lambda: show(".")).place(x=210,y=430)
Button(root,text="=",font=('arial',13,'bold'),width=7,height=7,bg="orange",fg="white",command=lambda: calculate()).place(x=310,y=350)



root.mainloop()
