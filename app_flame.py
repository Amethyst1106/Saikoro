import tkinter
from dice_make import Dice

class App(tkinter.Frame):

    def __init__(self,window = None):
        #継承元のinit書き換え
        super().__init__(window,
                        width = 300,
                        height = 300,
                        borderwidth = 1,
                        relief = "groove"
                        )
        self.window = window
        self.pack()
        self.pack_propagate(0)
        self.widgets()
        self.text = None
    
        
    def widgets(self):

        #min
        tkinter.Label(text="以上").place(x=200,y=50)
        min = tkinter.Entry(width = 10)
        min.place(x=90, y=50)

        #max
        tkinter.Label(text="以下").place(x=200,y=100)
        max = tkinter.Entry(width = 10)
        max.place(x=90, y=100)

        #実行ボタン
        runButton = tkinter.Button(self) 
        runButton["text"] = "サイコロを振る"
        runButton["command"] = lambda:self.result(min.get(),max.get())
        runButton.place(x=100,y=150)

    def roll(self,a,b):
        dice = Dice(a,b)
        return dice.roll()
    
    #結果表示
    def result(self,a,b):

        #前の結果があれば消す
        if self.text:
            self.text.place_forget()

        try:
            a, b = eval(a), eval(b)
            kekka = self.roll(a,b)
            size = 20
            x1 = 100
        
        except (SyntaxError, ValueError, TypeError, NameError):
            kekka = "エラー：数字を入力してください"
            size = 10
            x1 = 5

        self.text = tkinter.Label(
            self,text=kekka, font = ("nomal", size, "bold")
            )
        self.text.place(x=x1,y=215)