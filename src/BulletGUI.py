#==================================
# BulletGUI.py
# JetMake (c) 2022
# Bullet界面生成
#==================================

#import libs=======================
from tkinter import *
import time
from tags import App
#==================================



#logo显示窗口
logo = Tk()
logo.overrideredirect(True)
logo.geometry("+800+400")
photo = PhotoImage(file="C:\\Users\\jackw\\Documents\\GitHub\\bullet\\assets\\logo.png")
imageLabel = Label(logo, image=photo)
imageLabel.pack(side=LEFT)
t0 = time.time()
t1 = time.time()
while t1-t0<1.5:
    logo.update()
    t1 = time.time()
logo.destroy()

#根窗口
root = Tk()
app = App(root)
root.mainloop()


