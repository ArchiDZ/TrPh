from tkinter import*
from tkinter import ttk

clicks = 0
def click_button():
    global clicks #переменная которая создана вне метода, для использования в методе используется параметр глобал
    clicks+=1
    print(f'\nHello Clicked {clicks}')


def finish():
    root.destroy() #ручное закрытие окна и всего приложения
    print('Завершение работы приложения')

root = Tk() #Создаем корневой обьект - окно
root.title("Приложуха") #Устанавливаем заголовок окна
root.geometry('300x300') #устанавливаем размеры окна
root.protocol('WM_DELETE_WINDOW',finish) #(ИМЯ_СОБЫТИЯ,метод - который выполняется при возникновении события)
root.resizable(False,False) #Окно нельзя изменить в размерах

label = Label(text='Hello world!') #создаем текстовую метку
label.pack() #размещаем метку в окне

btn = ttk.Button(text='Start') #создаем кнопку
btn['command'] = click_button
btn.pack() #размещаем кнопку в окне

root.mainloop() 