import tkinter
from tkinter import messagebox
from tkinter import *


window=tkinter.Tk()
window.title("calculator")
window.geometry("640x400+100+100")
window.resizable(False, False)



uk = 0
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
a = []


w = 0
np = 1
op = 1
gen = 0
isfirst = 0
ph2 = 0
ph1 = 0
#isfirst = StringVar()

def close():
    window.quit()
    window.destroy()

def maker():
    tkinter.messagebox.showinfo("maker", "made by" " teen developer")

def reset():
    global a
    global ph1
    global ph2
    var1.set("")
    var2.set("")
    var3.set("")
    ph1 = ""
    ph2 = ""
    a = []
    listbox.delete(0, 'end')

menubar=tkinter.Menu(window)


menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="reset", command=reset)
menu_1.add_command(label="maker", command=maker)
menu_1.add_separator()
menu_1.add_command(label="close", command=close)
menubar.add_cascade(label="menu", menu=menu_1)

window.config(menu=menubar)



def down(e):
    print ('Key Down: ', e.char)
    if e.char == "1":
        one()
    elif e.char == "2":
        two()
    elif e.char == "3":
        three()
    elif e.char == "4":
        four()
    elif e.char == "5":
        five()
    elif e.char == "6":
        six()
    elif e.char == "7":
        seven()
    elif e.char == "8":
        eight()
    elif e.char == "-":
        nine()
    elif e.char == "0":
        zero()
    elif e.char == "2":
        minus()
    elif e.char == "+":
        plus()
    elif e.char == "-":
        minus()
    elif e.char == "*":
        multiply()
    elif e.char == "/":
        division()
    elif e.char == "=":
        result()

window.bind('<KeyPress>', down)

def one():
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        ph1 = "1"
        isfirst = 1
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "1"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        np = 3
        ph2 = "1"
        var3.set(ph2)
    elif gen == 3:
        ph2 = ph2 + "1"
        var3.set(ph2)

def two():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "2"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "2"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        np = 3
        ph2 = "2"
        var3.set(ph2)
    elif gen == 3:
        ph2 = ph2 + "2"
        var3.set(ph2)
    
def three():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "3"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "3"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        np = 3
        ph2 = "3"
        var3.set(ph2)
    elif isfirst == 3:
        ph2 = ph2 + "3"
        var3.set(ph2)
    

def four():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "4"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "4"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        np = 3
        ph2 = "4"
        var3.set(ph2)
    elif isfirst == 3:
        ph2 = ph2 + "4"
        var3.set(ph2)
    

def five():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "5"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "5"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        np = 3
        ph2 = "5"
        var3.set(ph2)
    elif isfirst == 3:
        ph2 = ph2 + "5"
        var3.set(ph2)
    

def six():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "6"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "6"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        np = 3
        ph2 = "6"
        var3.set(ph2)
    elif isfirst == 3:
        ph2 = ph2 + "6"
        var3.set(ph2)
    

def seven():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "7"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "7"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        ph2 = "7"
        var3.set(ph2)
        np = 3

    elif isfirst == 3:
        ph2 = ph2 + "7"
        var3.set(ph2)
    

def eight():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "8"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "8"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        ph2 = "8"
        var3.set(ph2)
        np = 3
    elif isfirst == 3:
        ph2 = ph2 + "8"
        var3.set(ph2)
    

def nine():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global gen
    global np
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "9"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "9"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        ph2 = "9"
        var3.set(ph2)
        np = 3
    elif isfirst == 3:
        ph2 = ph2 + "9"
        var3.set(ph2)
    

def zero():
    #label = tkinter.Label(window, text=2)
    #label.pack()
    global isfirst
    global ph1
    global ph2
    global np
    global gen
    if isfirst == 0:
        
        isfirst = 1
        ph1 = "0"
        var1.set(ph1)
    elif isfirst == 1:
        ph1 = ph1 + "0"
        var1.set(ph1)
    elif np == 2:
        gen = 3
        ph2 = "0"
        np == 3
        var3.set(ph2)
        
    elif isfirst == 3:
        ph2 = ph2 + "0"
        var3.set(ph2)
   

def minus():
    global np
    global op
    global isfirst
    isfirst = 3
    var2.set("-")
    np = 2
    op = 2

def plus():
    global op
    global np
    global isfirst
    isfirst = 3
    var2.set("+")
    op = 1
    np = 2
        
        
        

    
def multiply():
    global op
    global np
    global isfirst
    isfirst = 3

    var2.set("*")
    np = 2
    op = 3
    
def division():
    global op
    global np
    global isfirst
    isfirst = 3
    var2.set("/")
    np = 2
    op = 4


def result():
    #messagebox.showinfo("이름", label.text)
    #label = tkinter.Label(window, text="=")
    #label.pack()
    global op
    global ww
    if op == 1:
        print(int(ph1) + int(ph2))
        ww = 1
        cr()
    elif op == 2:
        print(int(ph1) - int(ph2))
        ww = 1
        cr()
    elif op == 3:
        print(int(ph1) * int(ph2))
        ww = 1
        cr()
    elif op == 4:
        if ph1 == "0":
            print("no answer")
            ww = 1
            cr()
        elif ph2 == "0":
            print("no answer")
            ww = 1
            cr()
        else:
            print(int(ph1) / int(ph2))
            ww = 1
            cr()
    
listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.place(x = 520, y =10)
def cr():    
    global isfirst
    global a
    
    if ww == 1:
        
        
        if op == 1:
            listbox.delete(0, 'end')
            mg = ph1 + "+" + ph2 + "=" + str(int(ph1) + int(ph2))
            #print(mg)
            a.append(mg)
            #print(a)
            
            for i in a:
                listbox.insert(0, i)
                isfirst = 0
        
            
            
        elif op == 2:
            listbox.delete(0, 'end')
            mg = ph1 + "-" + ph2 + "=" + str(int(ph1) - int(ph2))
            #print(mg)
            a.append(mg)
            #print(a)
            
            for i in a:
                listbox.insert(0, i)
                isfirst = 0
        elif op == 3:
            listbox.delete(0, 'end')
            fv = ph1 + "*" + ph2 + "=" + str(int(ph1) * int(ph2))
            #print(mg)
            a.append(fv)
            #print(a)
            
            for i in a:
                listbox.insert(0, i)
                isfirst = 0
        elif op == 4:
            if ph1 == "0":
                listbox.delete(0, 'end')
                cq = "no answer"
                #print(mg)
                a.append(cq)
                #print(a)
                
                for i in a:
                    listbox.insert(0, i)
                    
                    isfirst = 0
            
            elif ph2 == "0":
                listbox.delete(0, 'end')
                cg = "no answer"
                #print(mg)
                a.append(cg)
                #print(a)
                
                for i in a:
                    listbox.insert(0, i)
                    isfirst = 0
                
            else:
                listbox.delete(0, 'end')
                mm = ph1 + "/" + ph2 + "=" + str(int(ph1) / int(ph2))
                a.append(mm)
            
                
                for i in a:
                    listbox.insert(0, i)
                    isfirst = 0
    

button1 = tkinter.Button(window, overrelief="solid", text = "1", width=5, command = one)
button1.place(x=220, y=100)


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
button0.place(x=320, y=350)

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