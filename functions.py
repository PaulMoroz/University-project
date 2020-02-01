
from tkinter import * #Імпорт бібліотеки для роботи з графікою
from tkinter import messagebox as mb #Бібліотека для роботи з повідомленнями (Alert на js)
from tkinter import filedialog as fd #Бібліотека для роботи з вікном вибору файлу
import cv2 #Бібліотека для роботи з ші
import PIL #Бібліотека для роботи з картинками
from PIL import Image,ImageTk #Бібліотека для роботи з картинками (імпортується pip import pillow)
import numpy as np #бібліотека для роботи з масивами
import os,re #Бібліотека для роботи з базами даних. Sqlite не вимагає сервера для роботи
"""

root=Tk()     # Створення головного вікна

root.geometry("1366x650")#Розміри головного вікна
root.title("Eye diagnostix")    #Назва вікна
root['bg'] = '#E6E6FA'
photo = Image.open("background.png")
#photo = PhotoImage(file="background.png")    #Cтворення об"єкту з фотографією по шляху

picture = Label()   #Створення label( об"єкту, який не може змінити користувач ) з картинкою
picture.img = ImageTk.PhotoImage(photo)
picture['image'] = picture.img
root.title("Eye diagnostix")    #Назва вікна

picture.place(x = 40,y = 40)
P = ''

def echoimage(path):
    print(path)
    img = cv2.imread(path)
    global P
    P = path
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    image.thumbnail((400,400))
    picture.img = ImageTk.PhotoImage(image)
    picture['image'] = picture.img

def pre_filter():
    f = FROM.get().split()
    t = TO.get().split()
    global P
    print(P)
    if len(f)==len(t)==3:
        try:
            errors = 0
            for i in range(0,3):
                if(1<=len(f[i])<=3 and 1<=len(t[i])<=3) and t[i].isdigit() and f[i].isdigit():
                    f[i] = int(f[i])
                    t[i] = int(t[i])
                else:
                    errors=1
                    break
            if errors==0:
                img = cv2.imread(P)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
                eyes = eyeCascade.detectMultiScale(
                        gray,
                        scaleFactor=1.3,
                        minNeighbors=3,      
                        minSize=(30, 30)
                        )

print(len(eyes))
               # eyes = eyeCascade.detectMultiScale(gimg,scaleFactor= 1.5,minNeighbors=10,minSize=(10, 10))
                if P!='' and len(eyes) == 1:
                    filter()
                else:
                    mb.showerror("Eye recognition","Something wrong with photos")
            else:
                mb.showerror("Eye recognition","Something wrong with colors stage3")
        except:
            mb.showerror("Eye recognition","Something wrong with colors stage2")
    else:
        mb.showerror("Eye recognition","Something wrong with colors stage1")
    FROM.delete(0, END)
    TO.delete(0, END)
    
def filter():
    global P
    maxw,maxd,color = 0,0,""
    colors = {((20,19,8),(210,165,126)):"blue",((6,23,66),(53,58,103)):"brown", ((22,25,30),(169,164,143)):"grey"}
    img = cv2.imread(P)
    for i in colors:
        hsv_min = np.array(i[0], np.uint8)
        hsv_max = np.array(i[1], np.uint8)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        thresh = cv2.inRange(hsv, hsv_min, hsv_max)
        image = Image.fromarray(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
        b,w = 0,0
        for row in thresh:
            for pixel in row:
                if pixel==255:
                    w+=1
                else:
                    b+=1
        if w>maxw:
            maxw = w
            color = colors[i]
            maxd = i
        print("White: ", w,"Black: ",b,"color",colors[i])
    print("Eye color: ",color)
    hsv_min = np.array(maxd[0], np.uint8)
    hsv_max = np.array(maxd[1], np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    image = Image.fromarray(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))    
    image.thumbnail((400,400))
    picture.img = ImageTk.PhotoImage(image)
    picture['image'] = picture.img
    P = ''
 #   window = Toplevel()
 #   window.geometry("500x500")
 #   window.title("Детальні результати діагностики")
 #   label = Label(window, text="a generic Toplevel window")
 #   label.pack()
 #   window.mainloop()
 """
def getImage():
    image_path = fd.askopenfilename()
    print(image_path)
    if image_path.endswith('.png') or image_path.endswith('.jpg') or image_path.endswith('.jpeg'):
        echoimage(image_path)
        print("All is ok)")
    else:
        mb.showwarning("Eye recognition","Choose image")
"""
S = Label(text = "Enter start and finish of diapasone", font = "Arial, 15")
S.place(x = 80,y = 450)
FROM = Entry(width = 11,font = "Arial, 15")
F = Label(text = "From: ", font = "Arial, 15")
F.place(x = 50,y = 480)
TO  = Entry(width = 11,font = "Arial, 15")
T = Label(text = "To: ", font = "Arial, 15")
T.place(x = 275, y = 480)
FROM.place(x = 120,y = 480)
TO.place(x = 320,y = 480)
choose = Button(text = "Вибрати зображення",width = 35, height = 1,bg = "#6495ed",font = "Arial, 15",relief = "flat", command = choosefile)
choose.place(x = 50,y = 510)
filt =  Button(text = "Застосувати фільтр",width = 35, height = 1,bg = "#6495ed",font = "Arial, 15",relief = "flat", command = pre_filter)
filt.place(x = 50,y = 570)
R = Label(text = "Здорове око", font = "Arial, 15")
R.place(x = 550, y = 10)
H = Label(text = "Картинка перед скануванням", font = "Arial, 15")
H.place(x = 100,y = 10)
Rezult = Label(text = "Картинка перед скануванням", font = "Arial, 15" )
Rezult.place(x = 500,y = 40)

rbg = Image.open("rezult_background.jpg")
rbg.thumbnail((400,400))
Rezult.img = ImageTk.PhotoImage(rbg)
    
Rezult['image'] = Rezult.img

reztxt = Label(text = "Знайдені хвороби", font = "Arial, 15",highlightthickness = 3,width = 36,height = 25)
reztxt.place(x = 920, y = 40)
root.mainloop() #
"""