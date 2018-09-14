
from tkinter import *

win=Tk()
win.title("::CAL::")
win.configure(bg="silver")
win.minsize(217,270)

en=Entry(win,width=31,fg="blue")
ans=Entry(win,width=31,fg="red")

def press0():
    en.insert(INSERT,"0")
def press1():
    en.insert(INSERT,"1")
def press2():
    en.insert(INSERT,"2")
def press3():
    en.insert(INSERT,"3")
def press4():
    en.insert(INSERT,"4")
def press5():
    en.insert(INSERT,"5")
def press6():
    en.insert(INSERT,"6")
def press7():
    en.insert(INSERT,"7")
def press8():
    en.insert(INSERT,"8")
def press9():
    en.insert(INSERT,"9")
def pressplus():
    en.insert(INSERT,"+")
def pressminus():
    en.insert(INSERT,"-")
def pressmultiply():
    en.insert(INSERT,"*")
def pressdivide():
    en.insert(INSERT,"/")
def pressdel():
    en.delete(0,END)
    ans.delete(0,END)
def pressequal():
    ans.insert(INSERT,"ANS=")
    s=eval(en.get())
    ans.insert(INSERT,s)

b1=Button(win,text="1",width=4,height=2,fg="black",bg="old lace",font=("Arial",8),bd=4,activebackground="coral",command=press1)
b2=Button(win,text="2",width=4,height=2,fg="black",bg="cyan",font=("Arial",8),bd=4,activebackground="coral",command=press2)
b3=Button(win,text="3",width=4,height=2,fg="black",bg="old lace",font=("Arial",8),bd=4,activebackground="coral",command=press3)
b4=Button(win,text="4",width=4,height=2,fg="black",bg="cyan",font=("Arial",8),bd=4,activebackground="coral",command=press4)
b5=Button(win,text="5",width=4,height=2,fg="black",bg="old lace",font=("Arial",8),bd=4,activebackground="coral",command=press5)
b6=Button(win,text="6",width=4,height=2,fg="black",bg="cyan",font=("Arial",8),bd=4,activebackground="coral",command=press6)
b7=Button(win,text="7",width=4,height=2,fg="black",bg="old lace",font=("Arial",8),bd=4,activebackground="coral",command=press7)
b8=Button(win,text="8",width=4,height=2,fg="black",bg="cyan",font=("Arial",8),bd=4,activebackground="coral",command=press8)
b9=Button(win,text="9",width=4,height=2,fg="black",bg="old lace",font=("Arial",8),bd=4,activebackground="coral",command=press9)
b0=Button(win,text="0",width=4,height=2,fg="black",bg="cyan",font=("Arial",8),bd=4,activebackground="coral",command=press0)

bplus=Button(win,text="+",width=4,height=2,fg="black",bg="pink",font=("Arial",8,"bold"),bd=4,activebackground="coral",command=pressplus)
bminus=Button(win,text="--",width=4,height=2,fg="black",bg="pink",font=("Arial",8,"bold"),bd=4,activebackground="coral",command=pressminus)
bdivide=Button(win,text="/",width=4,height=2,fg="black",bg="pink",font=("Arial",8,"bold"),bd=4,activebackground="coral",command=pressdivide)
bmultiply=Button(win,text="*",width=4,height=2,fg="black",bg="pink",font=("Arial",8,"bold"),bd=4,activebackground="coral",command=pressmultiply)
bequal=Button(win,text="==",width=4,height=2,fg="black",bg="cyan",font=("Arial",8,"bold"),bd=4,activebackground="yellow",command=pressequal)
bdel=Button(win,text="DEL",width=4,height=2,fg="black",bg="violet",font=("Arial",8,"bold"),bd=3,activebackground="yellow",command=pressdel)
bdel.config(relief="groove")

en.place(x=10,y=5)
ans.place(x=10,y=35)
b1.place(x=10,y=65)
b4.place(x=10,y=115)
b7.place(x=10,y=165)
b0.place(x=10,y=215)
b2.place(x=60,y=65)
b5.place(x=60,y=115)
b8.place(x=60,y=165)
bdel.place(x=62,y=217)
b3.place(x=110,y=65)
b6.place(x=110,y=115)
b9.place(x=110,y=165)

bequal.place(x=110,y=215)
bminus.place(x=160,y=65)
bdivide.place(x=160,y=115)
bmultiply.place(x=160,y=165)
bplus.place(x=160,y=215)

win.mainloop()
