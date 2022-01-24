#==================================
# tags.py
# JetMake (c) 2022
# Bullet界面生成2
#==================================

#import libs=======================
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
#==================================

#窗口类=============================
class C172:
    fpath = "Data-10313214-20220116.txt"
    PlaneType = 0
    def __init__(self, root):
        #setting title
        root.title("航前计划")
        #setting window size
        width=292
        height=276
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_647=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_647["font"] = ft
        GLabel_647["fg"] = "#333333"
        GLabel_647["justify"] = "left"
        GLabel_647["text"] = "弹幕姬Data文件位置"
        GLabel_647.place(x=20,y=30,width=167,height=30)

        GLabel_803=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_803["font"] = ft
        GLabel_803["fg"] = "#333333"
        GLabel_803["justify"] = "right"
        GLabel_803["text"] = "机型"
        GLabel_803.place(x=70,y=160,width=70,height=25)

        GButton_731=tk.Button(root)
        GButton_731["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_731["font"] = ft
        GButton_731["fg"] = "#000000"
        GButton_731["justify"] = "center"
        GButton_731["text"] = "C172"
        GButton_731.place(x=190,y=110,width=70,height=25)
        GButton_731["command"] = self.GButton_731_command

        GButton_747=tk.Button(root)
        GButton_747["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_747["font"] = ft
        GButton_747["fg"] = "#000000"
        GButton_747["justify"] = "center"
        GButton_747["text"] = "A32N"
        GButton_747.place(x=190,y=160,width=70,height=25)
        GButton_747["command"] = self.GButton_747_command

        GButton_937=tk.Button(root)
        GButton_937["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_937["font"] = ft
        GButton_937["fg"] = "#000000"
        GButton_937["justify"] = "center"
        GButton_937["text"] = "B77W"
        GButton_937.place(x=190,y=210,width=70,height=25)
        GButton_937["command"] = self.GButton_937_command

        GButton_311=tk.Button(root)
        GButton_311["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        GButton_311["font"] = ft
        GButton_311["fg"] = "#000000"
        GButton_311["justify"] = "center"
        GButton_311["text"] = "选择"
        GButton_311.place(x=190,y=30,width=70,height=25)
        GButton_311["command"] = self.GButton_311_command

        GLabel_436=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_436["font"] = ft
        GLabel_436["fg"] = "#333333"
        GLabel_436["justify"] = "center"
        GLabel_436["text"] = self.labletext
        GLabel_436.place(x=10,y=70,width=278,height=30)

    def CallBeacon(self,type):
        print(type)
        print(self.fpath)
        if type == 1:

        elif type == 2:

        elif type == 3:

        else:






    def GButton_731_command(self):
        PlaneType = 1
        print(PlaneType)
        self.CallBeacon(PlaneType)




    def GButton_747_command(self):
        PlaneType = 2
        print(PlaneType)
        self.CallBeacon(PlaneType)


    def GButton_937_command(self):
        PlaneType = 3
        print(PlaneType)
        self.CallBeacon(PlaneType)


    def GButton_311_command(self):
        print("c")
        self.fpath = filedialog.askopenfilename()
        self.labletext = "已选择"+ self.fpath
        print(self.labletext)


    labletext="例如:Data-10313214-20220116.txt"

#==================================





