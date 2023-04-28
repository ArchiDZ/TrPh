from tkinter import*
from tkinter import ttk


def finish():
    root.destroy()


root = Tk()
root.title('Check list')
root.geometry('500x700')
root.protocol('WM_DELETE_WINDOW', finish)
root.resizable(False, False)

label_post_1 = Label(text='Техник по наладке', font='bold')
label_post_1.pack(anchor='n')
label_1 = Label(text='Проверка и подготовка оборудования к производству')
label_1.pack(anchor='w')
label_2 = Label(text='Чистка тиглей от шлака')
label_2.pack(anchor='w')
btn_1 = ttk.Button(text='Отметиться', width='50')
btn_1.pack(anchor='w')



label_post_2 = Label(text='Оператор', font='bold')
label_post_2.pack(anchor='n')
label_3 = Label(text='Насторойка конвейерных столов,буфера.Проверка Чистоты')
label_3.pack(anchor='w')
label_4 = Label(text='Чистка флюсосователя (08-00)')
label_4.pack(anchor='w')
label_5 = Label(text='Установка нозлов')
label_5.pack(anchor='w')
label_6 = Label(text='Чистка нозлов')
label_6.pack(anchor='w')
btn_2 = ttk.Button(text='Отметиться', width='50')
btn_2.pack(anchor='w')

label_post_3 = Label(text='Техник - технолог', font='bold')
label_post_3.pack(anchor='n')
label_7 = Label(text='Калибровка нозлов')
label_7.pack(anchor='w')
label_8 = Label(text='Калибровка флюсосователя')
label_8.pack(anchor='w')
label_9 = Label(text='Калибровка флюсосования по бумаге')
label_9.pack(anchor='w')
label_10 = Label(text='Проверка УП на технологичность')
label_10.pack(anchor='w')
btn_3 = ttk.Button(text='Отметиться', width='50')
btn_3.pack(anchor='w')

label_post_4 = Label(text='Монтажник', font='bold')
label_post_4.pack(anchor='n')
label_11 = Label(text='Отдать первую заготовку на ОТК')
label_11.pack(anchor='w')
btn_4 = ttk.Button(text='Отметиться', width='50')
btn_4.pack(anchor='n')

label_post_5 = Label(text='Оператор', font='bold')
label_post_5.pack(anchor='n')
label_12 = Label(text='Чистка флюсосователя (13-00)')
label_12.pack(anchor='w')
label_13 = Label(text='Чистка флюсосователя (17-00)')
label_13.pack(anchor='w')
label_14 = Label(text='Уборка установщика, конвеёера, SEHO')
label_14.pack(anchor='w')
btn_5 = ttk.Button(text='Отметиться', width='50')
btn_5.pack(anchor='n')

label_post_6 = Label(text='Техник по наладке', font='bold')
label_post_6.pack(anchor='n')
label_15 = Label(text='Консервация флюсосователей'
                      '(при простое оборудования больше 12 часов)')
label_15.pack(anchor='w')
btn_6 = ttk.Button(text='Отметиться', width='50')
btn_6.pack(anchor='n')

root.mainloop()