########################################
###### VERSION 1.0 ######################
########################################

import subprocess as sp
import tkinter.filedialog as tfd
import tkinter.messagebox as tmb
import pyperclip as pc
import ast
import webbrowser as wb
from PIL import ImageGrab
from tkinter import *
import os
import urllib.request

global root
root = Tk()

def openfd():
    root.destroy()
    print("Выбери файл в окошке")
    sad = tfd.askopenfilename()
    sadL = []
    for i in range(len(sad)):
        sadL.append(sad[i])
    sadL.remove(sadL[0])
    sadL.remove(sadL[0])
    sadL.insert(0, '@')
    sad = ''
    for i in range(len(sadL)):
        sad += sadL[i]
    print("Гачи гейинг...")
    asd = sp.run(f'curl "https://gachi.gay/api/upload" -F "file={sad}"', stdout=sp.PIPE)
    print(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    if ch_copy.get(): pc.copy(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    if ch_open.get(): wb.open(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    '''if not os.path.exists("top5gays.gachigayingfile"):
        wd = open("top5gays.gachigayingfile", 'w')
        wd.write("[]")
        wd.close()
    rd = open("top5gays.gachigayingfile", 'r').read()
    rd = rd.strip('][').split(', ')
    pen123 = {}
    pen123['link'] = ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link']
    pen123['delete'] = ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['delete']
    rd.append(pen123)
    wd = open("top5gays.gachigayingfile", 'w')
    wd.write(str(rd))
    wd.close()'''
    

def pickimg():
    root.destroy()
    im = ImageGrab.grabclipboard()
    try: im.save("temp.png", 'png')
    except AttributeError:
        tmb.showinfo("Ой ой", "Кажеться в буфере обмена не картинка")
        return
    cwd = '/'
    for i in range(1, len(os.getcwd().split("\\"))):
        cwd += os.getcwd().split("\\")[i]
        cwd += "/"
    print("Гачи гейинг...")
    asd = sp.run(f'curl "https://gachi.gay/api/upload" -F "file=@{cwd}temp.png"', stdout=sp.PIPE)
    print(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    if ch_copy.get(): pc.copy(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    if ch_open.get(): wb.open(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    os.remove("temp.png")
    '''if not os.path.exists("top5gays.gachigayingfile"):
        wd = open("top5gays.gachigayingfile", 'w')
        wd.write("[]")
        wd.close()
    rd = open("top5gays.gachigayingfile", 'r').read()
    rd = rd.strip('][').split(', ')
    pen123 = {}
    pen123['link'] = ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link']
    pen123['delete'] = ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['delete']
    rd.append(pen123)
    wd = open("top5gays.gachigayingfile", 'w')
    wd.write(str(rd))
    wd.close()'''

'''def showList(p, rd):
    global root
    root.destroy()
    root = Tk()
    root.title(f"Мои геи | Cтраница {p}")
    root.geomtry("340x600")
    if p == int(len(rd)/5):
        
        
    
def controlAward():
    global root

    rd = open("top5gays.gachigayingfile", 'r').read()
    rd = rd.strip('][').split(', ')

    showList(1, rd)'''


def pickfile():
    root.destroy()
    try: pp = ImageGrab.grabclipboard()[0]
    except TypeError:
        tmb.showinfo("Ой ой", "Кажется в буфере обмена не файл")
        return
    cwd = '/'
    for i in range(1, len(os.getcwd().split("\\"))+1):
        cwd += pp.split("\\")[i]
        cwd += "/"
    print("Гачи гейинг...")
    asd = sp.run(f'curl "https://gachi.gay/api/upload" -F "file=@{cwd[:len(cwd)-1]}"', stdout=sp.PIPE)
    print(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    if ch_copy.get(): pc.copy(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    if ch_open.get(): wb.open(ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link'])
    '''if not os.path.exists("top5gays.gachigayingfile"):
        wd = open("top5gays.gachigayingfile", 'w')
        wd.write("[]")
        wd.close()
    rd = open("top5gays.gachigayingfile", 'r').read()
    rd = rd.strip('][').split(', ')
    pen123 = {}
    pen123['link'] = ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['link']
    pen123['delete'] = ast.literal_eval(str(asd.stdout)[2:len(str(asd.stdout))-1])['delete']
    rd.append(pen123)
    wd = open("top5gays.gachigayingfile", 'w')
    wd.write(str(rd))
    wd.close()'''
    


root.title("Welcome to gachi gaying!")

root.geometry("500x200")

#urllib.request.urlretrieve("https://vk.com/doc376080925_652583767?hash=uY3qgnHCTj7zINY4mZZv1RaLZZNWzCDDdngiWKm8zBP&dl=WEwkZXKnJxszaXfQMci4KthlDziWZiZcZZZLMhtIUuP", "gachi.ico")

#root.iconbitmap("gachi.ico")

#os.remove("gachi.ico")

root.resizable(False, False)

Label(root, text = "Добро пожаловать в гачи гейинг! Выбери свой путь", font=("Arial", 12)).place(x=10,y=0,height=60,width=500)

Button(root, text = "Открыть проводник и пикнуть файл", command = openfd).place(x=10, y=120)
Button(root, text = "Вставить КАРТИНКУ из буфера обмена", command = pickimg).place(x=230, y=120)
#Button(root, text = "Мои геи", command = controlAward).place(x=465, y=90)
Button(root, text = "Вставить ФАЙЛ (Путь до файла проводниковый) из буфера обмена", command = pickfile).place(x=10, y=160)

ch_open = BooleanVar()

Checkbutton(root, text = "Открыть ссылку в браузере", variable=ch_open).place(x=10, y = 60)
ch_open.set(True)

ch_copy = BooleanVar()

Checkbutton(root, text = "Скопировать ссылку в буфер обмена", variable=ch_copy).place(x=10, y=85)
ch_copy.set(True)

Label(root, text = "V.1.0    By POAL48      gachi.gay by supa", font=("Arial", 5)).place(x=2, y=190)

root.mainloop()

if not ch_open.get():
    print("Отхерачь любую кнопку для выхода . . . ")
    os.system("pause")


