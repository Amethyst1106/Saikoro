from dice_make import Dice
from app_flame import App
import tkinter

window = tkinter.Tk()
window.title("サイコロ")
window.geometry("300x300")

if __name__ == "__main__":
    Aplication = App(window = window)
    Aplication.mainloop()