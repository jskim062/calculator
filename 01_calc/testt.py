import pymysql
import tkinter
import requests
import json

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window=tkinter.Tk()
window.title("jskim")
window.geometry("1000x1000+100+100")
window.resizable(False, False)
#win = Tk()

from flask import Flask, jsonify
app = Flask (__name__)
 
conn = pymysql.connect(host='localhost', user='', password='',
                       db='jskimdb', charset='utf8')

curs = conn.cursor()



def countUP1():

    contents = requests.get("http://127.0.0.1:5000/useritem/h")
    
    w = contents.content
    
    #print(w)
    
    dict = json.loads(w)

    
    label = tkinter.Label(window, text=dict)
    label.pack()

str1 = StringVar()
str2 = StringVar()    
str3 = StringVar()
   
str4 = StringVar()
str5 = StringVar()    
str6 = StringVar()    

str7 = StringVar() 

textbox = ttk.Entry(window, width=20, textvariable=str1)
textbox.grid(column = 0 , row = 0)
textbox.place(x=300,y=300)
    
textbox2 = ttk.Entry(window, width=20, textvariable=str2)
textbox2.grid(column = 0 , row = 0)
textbox2.place(x=500,y=300)
    
textbox3 = ttk.Entry(window, width=20, textvariable=str3)
textbox3.grid(column = 0 , row = 0)
textbox3.place(x=700,y=300)

textbox4 = ttk.Entry(window, width=20, textvariable=str4)
textbox4.grid(column = 0 , row = 0)
textbox4.place(x=300,y=500)
    
textbox5 = ttk.Entry(window, width=20, textvariable=str5)
textbox5.grid(column = 0 , row = 0)
textbox5.place(x=500,y=500)
    
textbox6 = ttk.Entry(window, width=20, textvariable=str6)
textbox6.grid(column = 0 , row = 0)
textbox6.place(x=700,y=500)

textbox7 = ttk.Entry(window, width=20, textvariable=str7)
textbox7.grid(column = 0 , row = 0)
textbox7.place(x=300,y=700)

def insert():
    x = str1.get()
    y = str2.get()
    z = str3.get()
    
    
    
    contents1 = requests.get("http://127.0.0.1:5000/insert/h?username=" + str(x) + "&userexp=" + str(y) + "&userpoint=" + str(z))
    
def update():
    ab = str4.get()
    cd = str5.get()
    ef = str6.get()
    #http://127.0.0.1:5000/update/h?username=jskim&userexp=10000&userpoint=10000
    contents2 = requests.get("http://127.0.0.1:5000/update/h?username=" + str(ab) + "&userexp=" + str(cd) + "&userpoint=" + str(ef))

def delete():
    gh = str7.get()
    
    #http://127.0.0.1:5000/update/h?username=jskim&userexp=10000&userpoint=10000
    contents2 = requests.get("http://127.0.0.1:5000/delete/h?username="+str(gh))
    


button1 = tkinter.Button(window, overrelief="solid", text = "조회", width=5, command = countUP1)
button1.place(x=100, y=100)
    
button2 = tkinter.Button(window, overrelief="solid", text = "넣기", width=5, command = insert)
button2.place(x=100, y=300)

button3 = tkinter.Button(window, overrelief="solid", text = "업데이트", width=5, command = update)
button3.place(x=100, y=500)

button4 = tkinter.Button(window, overrelief="solid", text = "지우기", width=5, command = delete)
button4.place(x=100, y=700)

'''
button2 = tkinter.Button(window, text = "넣기", overrelief="solid", width=15, command=insert, repeatdelay=1000, repeatinterval=100)
button2.place(x=100, y=300)

button3 = tkinter.Button(window, text = "업데이트", overrelief="solid", width=15, command=update, repeatdelay=1000, repeatinterval=100)
button3.place(x=100, y=500)

button4 = tkinter.Button(window, text = "지우기", overrelief="solid", width=15, command=delete, repeatdelay=1000, repeatinterval=100)
button4.place(x=100, y=700)
'''

window.mainloop()
