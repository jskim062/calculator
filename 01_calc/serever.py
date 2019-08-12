import tkinter
#import urllib.request
import requests
import json

window=tkinter.Tk()
window.title("jskim")
window.geometry("640x400+100+100")
window.resizable(False, False)

count=0

list1 = []

def countUP():
    global count
    global list1
    count +=1
    contents = requests.get("http://127.0.0.1:5000/useritem/h")
    
    w = contents.content
    
    # with를 이용해 파일을 연다.
    # json 파일은 같은 폴더에 있다고 가정!
    
    dict = json.loads(w)

    for i in dict:
        
    
        print(i['username'])
        print(i['exppoint'])
        print(i['userpoint'])
        
    
 
    label.config(text=str(count))
    
label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()