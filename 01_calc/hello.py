from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win = Tk ()
win.title("Raspberry Pi UI")
win.geometry('200x100+200+200')
def clickMe():
        messagebox.showinfo("Button Clicked", str.get())
str = StringVar()
textbox = ttk.Entry(win, width=20, textvariable=str)
textbox.grid(column = 0 , row = 0)
action=ttk.Button(win, text="Click Me", command=clickMe)
action.grid(column=0, row=1)
win.mainloop()
#[출처] TKinter textbox 텍스트박스 위젯|작성자 조만간 빠마장