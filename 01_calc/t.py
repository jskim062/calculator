import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x480+100+100")
window.resizable(False, False)


listbox = tkinter.Listbox(window, selectmode='extended', height=0)
a = ['a', 'b', 'c']
for i in a: 
     listbox.insert(0, i)
     listbox.pack()
window.mainloop()








