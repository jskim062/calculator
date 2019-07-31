from tkinter import *

wn = Tk()
wn.title('KeyDetect')

def down(e):
    print ('Key Down: ', e.char)
    if e.char == "e":
        print("hello")


wn.bind('<KeyPress>', down)

wn.mainloop()