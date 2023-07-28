import qrcode
from tkinter import *
from tkinter import ttk


def gen_qr():
    key = tkey.get()
    img = qrcode.make(key)
    file_name = entry.get()+'.png'
    img.save(file_name)
    tkey.delete(0, END)
    entry.delete(0, END)


root = Tk()
root.title('StarLine QR Generator')
root.iconbitmap(default='SL.ico')
root.geometry('500x110')
l1 = Label(text='Введите ключ для генерации QR-кода')
tkey = Entry(width=45)
l2 = Label(text='Введите имя файла')
entry = ttk.Entry(width=45)
btn = ttk.Button(text='OK', width=25, command=gen_qr)

l1.pack()
tkey.pack()
l2.pack()
entry.pack()
btn.pack()

root.mainloop()
