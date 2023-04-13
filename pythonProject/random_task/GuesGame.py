import random
from tkinter import *
from tkinter import ttk


def finish():
    window.destroy()


def game_logic():
    secret_number = random.randint(1, 1000)


window = Tk()
window.title('Угадай число')
window.geometry('300x150')
window.protocol('WM_DELETE_WINDOW', finish)
window.resizable(False, False)

label = ttk.Label(text='Привет! Я загадал число попробуй отгадать')
label.pack()
text = Text(width=4, height=2)
text.pack()
btn = ttk.Button(text='OK')
btn.pack()
window.mainloop()

