import tkinter
from tkinter import messagebox
from tkinter import *

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

var1 = StringVar()
var2= StringVar()
var3 = StringVar()


op = 1


isfirst = 0
ph2 = 0
ph1 = 0
#isfirst = StringVar()

def one():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("1")
        isfirst = 1
        ph1 = 1
    else:
        var3.set("1")
        ph2 = 1

def two():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("2")
        isfirst = 1
        ph1 = 2
    else:
        var3.set("2")
        ph2 = 2
    

def three():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("3")
        isfirst = 1
        ph1 = 3
    else:
        var3.set("3")
        ph2 = 3
    

def four():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("4")
        isfirst = 4
        ph1 = 1
    else:
        var3.set("4")
        ph2 = 4
    

def five():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("5")
        isfirst = 1
        ph1 = 5
    else:
        var3.set("5")
        ph2 = 5
    

def six():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("6")
        isfirst = 1
        ph1 = 6
    else:
        var3.set("6")
        ph2 = 6
    

def seven():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("1")
        isfirst = 7
        ph1 = 7
    else:
        var3.set("7")
        ph2 = 7
    

def eight():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("8")
        isfirst = 1
        ph1 = 8
    else:
        var3.set("8")
        ph2 = 8
    

def nine():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("9")
        isfirst = 1
        ph1 = 9
    else:
        var3.set("9")
        ph2 = 9
    

def zero():
    global isfirst
    global ph1
    global ph2
    if isfirst == 0:
        var1.set("0")
        isfirst = 1
        ph1 = 0
    else:
        var3.set("0")
        ph2 = 0
    

def minus():
    global op
    var2.set("-")
    op = 2

def plus():
    global op
    var2.set("+")
    op = 1
        
        
        

    
def multiply():
    global op
    var2.set("*")
    op = 3
    
def division():
    global op
    var2.set("/")
    op = 4


def result():
    #messagebox.showinfo("이름", label.text)
    #label = tkinter.Label(window, text="=")
    #label.pack()
    global op
    if op == 1:
        print(ph1 + ph2)
    elif op == 2:
        print(ph1 - ph2)
    elif op == 3:
        print(ph1 * ph2)
    elif op == 4:
        print(ph1 / ph2)

button1 = tkinter.Button(window, overrelief="solid", text = "1", width=5, command = one)
button1.place(x=220, y=100)

#label = tkinter.Label(window, text=result)
#label.pack()

button2 = tkinter.Button(window, overrelief="solid", text = 2, width=5, command = two, repeatdelay=1000, repeatinterval=100)
button2.place(x=320, y=100)

button3 = tkinter.Button(window, overrelief="solid", text = 3, width=5, command = three, repeatdelay=1000, repeatinterval=100)
button3.place(x=420, y=100)

button4 = tkinter.Button(window, overrelief="solid", text = 4, width=5, command = four, repeatdelay=1000, repeatinterval=100)
button4.place(x=220, y=200)

button5 = tkinter.Button(window, overrelief="solid", text = 5, width=5, command = five, repeatdelay=1000, repeatinterval=100)
button5.place(x=320, y=200)

button6 = tkinter.Button(window, overrelief="solid", text = 6, width=5, command = six, repeatdelay=1000, repeatinterval=100)
button6.place(x=420, y=200)

button7 = tkinter.Button(window, overrelief="solid", text = 7, width=5, command = seven, repeatdelay=1000, repeatinterval=100)
button7.place(x=220, y=300)

button8 = tkinter.Button(window, overrelief="solid", text = 8, width=5, command = eight, repeatdelay=1000, repeatinterval=100)
button8.place(x=320, y=300)

button9 = tkinter.Button(window, overrelief="solid", text = 9, width=5, command = nine, repeatdelay=1000, repeatinterval=100)
button9.place(x=420, y=300)

button0 = tkinter.Button(window, overrelief="solid", text = 0, width=5, command = zero, repeatdelay=1000, repeatinterval=100)
button0.place(x=50, y=350)

buttonminus = tkinter.Button(window, overrelief="solid", text = "-", width=5, command = minus, repeatdelay=1000, repeatinterval=100)
buttonminus.place(x=50, y=50)

buttonplus = tkinter.Button(window, overrelief="solid", text = "+", width=5, command = plus, repeatdelay=1000, repeatinterval=100)
buttonplus.place(x=50, y=200)

buttonmultiply = tkinter.Button(window, overrelief="solid", text = "*", width=5, command = multiply, repeatdelay=1000, repeatinterval=100)
buttonmultiply.place(x=50, y=300)

buttondivision = tkinter.Button(window, overrelief="solid", text = "/", width=5, command = division, repeatdelay=1000, repeatinterval=100)
buttondivision.place(x=50, y=350)

buttondivision = tkinter.Button(window, overrelief="solid", text = "=", width=5, command = result, repeatdelay=1000, repeatinterval=100)
buttondivision.place(x=50, y=150)

label=tkinter.Label(window, text="파이썬", textvariable=var1, width=10, height=5, fg="red", relief="solid")
label.place(x=220, y=10)

label=tkinter.Label(window, text="파이썬", textvariable=var2, width=10, height=5, fg="red", relief="solid")
label.place(x = 320, y=10)

label=tkinter.Label(window, text="파이썬", textvariable=var3, width=10, height=5, fg="red", relief="solid")
label.place(x=420, y=10)



window.mainloop()