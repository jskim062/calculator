
import cv2
import tkinter
import numpy as np
#import ImageTk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import Tk, Label


#im = Image
kd = 0

def convert_to_tkimage():
    global src
    global kd
    dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    #_, binary = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY) 
    #im = Image.fromarray(dst)
    img = Image.fromarray(dst)
    imgtk = ImageTk.PhotoImage(image=img)

    label.config(image=imgtk)
    label.image = imgtk
    kd = 1
def turn():
     global src
     global kd
     print("a66", type(src))
     print("a77", src.shape)
     height, width, channel = src.shape
     
     matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
     dst = cv2.warpAffine(src, matrix, (width, height))
     #im = cv2.warpAffine(src, matrix, (width, height))
     #cv2.imshow("dst", dst)
     img = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
     img = Image.fromarray(img)
     #img.show()
     imgtk = ImageTk.PhotoImage(image=img)
     
     label.config(image=imgtk)
     label.image = imgtk
     kd = 2
def save():
     global src
     if kd == 1:
          '''
          dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
          cv2.imshow("dst", dst)
          
          im.save("result.jpg")
          '''
          grayImg = cv2.imread('google.jpg', cv2.IMREAD_GRAYSCALE)
          cv2.imwrite('result.jpg', grayImg)

     elif kd == 2:
          print(type(src))
          #vis = np.zeros((640, 400), np.float32)
          #src = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)
          print(type(src))
          
          height, width, channel = src.shape
          #matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
          cg = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
          dstx = cv2.warpAffine(src, cg, (width, height))
          #turning = cv2.imread('google.jpg', cv2.getRotationMatrix2D((width/2, height/2), 90, 1))
          cv2.imwrite('pp.jpg', dstx)

     #im.save("result.jpg")

def openfile():
     global src
     
     root = Tk()
     root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
     print("a7", root.filename)
     img2 = ImageTk.PhotoImage(Image.open(root.filename))
     src = np.array(img2)
     print("a78", src)
     print("a79", src.shape)
     #print("a9",type(img2))
     #print(type(src))

     label.configure(image=img2)
     label.image = img2
     
     '''
     print(root.filename)
     src = cv2.imread(root.filename)
     src = cv2.resize(src, (640, 400))
     img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

     img = Image.fromarray(img)
     imgtk = ImageTk.PhotoImage(image=img)

     label = tkinter.Label(window, image=imgtk)
     label.pack(side="top")
     
     '''     

window=tkinter.Tk()
window.title("")
window.geometry("640x640+100+100")

src = cv2.imread("google.jpg")

src = cv2.resize(src, (640, 400))

img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

img = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=img)

label = tkinter.Label(window, image=imgtk)
label.pack(side="top")

button = tkinter.Button(window, text="이진화 처리", command=convert_to_tkimage)
button.pack(side="bottom", expand=True, fill='both')

button = tkinter.Button(window, text="회전", command=turn)
button.pack(side="bottom", expand=True, fill='both')


button = tkinter.Button(window, text="저장", command=save)
button.pack(side="bottom", expand=True, fill='both')

button = tkinter.Button(window, text="열기", command=openfile)
button.pack(side="bottom", expand=True, fill='both')

window.mainloop()






