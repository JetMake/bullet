import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=198
        height=229
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.title("C172")

        GLabel_723=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_723["font"] = ft
        GLabel_723["fg"] = "#333333"
        GLabel_723["justify"] = "center"
        GLabel_723["text"] = "1"
        GLabel_723.place(x=30,y=50,width=30,height=30)

        GLabel_909=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_909["font"] = ft
        GLabel_909["fg"] = "#333333"
        GLabel_909["justify"] = "center"
        GLabel_909["text"] = "2"
        GLabel_909.place(x=30,y=100,width=30,height=30)

        GLabel_116=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_116["font"] = ft
        GLabel_116["fg"] = "#333333"
        GLabel_116["justify"] = "center"
        GLabel_116["text"] = "A"
        GLabel_116.place(x=50,y=10,width=70,height=25)

        GLabel_58=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#333333"
        GLabel_58["justify"] = "center"
        GLabel_58["text"] = "L"
        GLabel_58.place(x=110,y=10,width=70,height=25)

        GLabel_245=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_245["font"] = ft
        GLabel_245["fg"] = "#333333"
        GLabel_245["justify"] = "center"
        GLabel_245["text"] = "1A"
        GLabel_245.place(x=70,y=50,width=41,height=30)

        GLabel_538=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_538["font"] = ft
        GLabel_538["fg"] = "#333333"
        GLabel_538["justify"] = "center"
        GLabel_538["text"] = "1L"
        GLabel_538.place(x=130,y=50,width=35,height=30)

        GLabel_945=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_945["font"] = ft
        GLabel_945["fg"] = "#333333"
        GLabel_945["justify"] = "center"
        GLabel_945["text"] = "2A"
        GLabel_945.place(x=70,y=100,width=33,height=30)

        GLabel_246=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_246["font"] = ft
        GLabel_246["fg"] = "#333333"
        GLabel_246["justify"] = "center"
        GLabel_246["text"] = "2L"
        GLabel_246.place(x=130,y=100,width=33,height=30)

        GLabel_354=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_354["font"] = ft
        GLabel_354["fg"] = "#333333"
        GLabel_354["justify"] = "center"
        GLabel_354["text"] = "登机信息:"
        GLabel_354.place(x=0,y=150,width=70,height=25)

        GLabel_258=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_258["font"] = ft
        GLabel_258["fg"] = "#333333"
        GLabel_258["justify"] = "left"
        GLabel_258["text"] = "label"
        GLabel_258["relief"] = "flat"
        GLabel_258.place(x=20,y=180,width=182,height=30)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
