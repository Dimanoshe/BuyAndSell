from tkinter import *
from random import *


def button():
    minimum_pay = 3 + (_level['text'] * 2) ** 2
    maximum_pay = 10 + (_level['text'] * 2) ** 3
    _day['text'] += 1
    pribil = randint(minimum_pay, maximum_pay)

    _money['text'] += pribil

    komis = randint(10, 100)
    _dolar_buy['text'] += uniform(-1, 1)
    if _dolar_buy['text'] < 50:
        _dolar_buy['text'] += uniform(-1, 3)
    elif _dolar_buy['text'] > 80:
        _dolar_buy['text'] += uniform(-3, 1)


    _dolar_buy['text'] = round(_dolar_buy['text'], 2)

    _dolar_sell['text'] = round(_dolar_buy['text'] - _dolar_buy['text'] / komis, 2)
    prib['text'] = 'Прибыль за день: '+str(pribil)
    #fram.info['text'] = 'Туые'

def buy():
    def buy_1():
        summ = shkala.get()
        _money['text'] -= summ * _dolar_buy['text']
        _moneyS['text'] += summ
        _money['text'] = round(_money['text'], 2)
        win_b.withdraw()

    win_b = Toplevel(root)
    win_b.configure(bg='black')

    shkala = Scale(win_b, fg='green', bg='black', font='Times 20', orient=HORIZONTAL, length=300, from_=0, to=_money['text']/_dolar_buy['text'], resolution=1)
    shkala.grid(row=1, column=1, columnspan=8, )
    but_buy = Button(win_b, fg='green', bg='black', font='Times 20', height='3', width='10', text='Купить', command=buy_1)
    but_buy.grid(row=2, column=4, columnspan=1, )

def sell():
    def sell_1():
        summ = shkala.get()
        _moneyS['text'] -= summ
        _money['text'] += summ * _dolar_sell['text']
        _money['text'] = round(_money['text'], 2)
        win_s.withdraw()

    win_s = Toplevel(root)
    win_s.configure(bg='black')

    shkala = Scale(win_s, fg='green', bg='black', font='Times 20', orient=HORIZONTAL, length=300, from_=0, to=_moneyS['text'], resolution=1)
    shkala.grid(row=1, column=1, columnspan=8, )
    but_buy = Button(win_s, fg='green', bg='black', font='Times 20', height='3', width='10', text='Продать', command=sell_1)
    but_buy.grid(row=2, column=4, columnspan=1, )

def lvl_up():
    def lvl_up_1():
        win_up.withdraw()
        if _moneyS['text'] >= _lvl_info['text']:
            _moneyS['text'] -= _lvl_info['text']
            _level['text'] += 1
    price = (10 * _level['text'])**2
    price = round(price)
    if _level['text'] == 1:
        price = 100
    win_up = Toplevel(root)
    win_up.configure(bg='black')
    lvl_info = Label(win_up,  fg='green', bg='black', font='Times 20', text='Это будет стоить: ($)')
    lvl_info.grid(row=1, column=2, columnspan=1)
    _lvl_info = Label(win_up, fg='green', bg='black', font='Times 20', text=price)
    _lvl_info.grid(row=1, column=3, columnspan=1)
    but_buy = Button(win_up, fg='green', font='Times 15', bg='black', height='1', width='6', text='Ok', command=lvl_up_1)
    but_buy.grid(row=3, column=2, columnspan=1)




root = Tk()
root.title('Bay&Sell (B&S)')
root.geometry('900x400+600+300')
root.resizable(True, True)
root.iconbitmap('icon.ico')
root.configure(bg='black')


day = Label(root, fg='green', bg='black', font='Times 25', text='День: ')
_day = Label(root, fg='green', bg='black', font='Times 25', text=0)

money = Label(root, fg='green', bg='black', font='Times 25', text='Руб.: ')
_money = Label(root, fg='green', bg='black', font='Times 25', text=0)
moneyS = Label(root, fg='green', bg='black', font='Times 25', text='$: ')
_moneyS = Label(root, fg='green', bg='black', font='Times 25', text=10)

level = Label(root, fg='green', bg='black', font='Times 25', text='Уровень: ')
_level = Label(root, fg='green', bg='black', font='Times 25', text=1)

dolar_buy = Label(root, fg='green', bg='black', font='Times 20', text='покупка $ ')
_dolar_buy = Label(root, fg='green', bg='black', font='Times 20',  text=60)

dolar_sell = Label(root, fg='green', bg='black', font='Times 20',  text='продажа $ ')
_dolar_sell = Label(root, fg='green', bg='black', font='Times 20',  text=63)

prib = Label(root, fg='green', bg='black', font='Times 15', text='Прибыль за день: 0')


button_next_day = Button(root, fg='green', bg='black', height='3', width='14', text='Следующий день ', relief=RIDGE,
                         bd=5, activebackground='#006400', command=button)
button_buy = Button(root, fg='green', bg='black', height='3', width='8', text='Купить $', activebackground='#006400',
                    relief=RIDGE, command=buy)
button_sell = Button(root, fg='green', bg='black', height='3', width='8', text='Продать $', activebackground='#006400',
                     relief=RIDGE, command=sell)
button_lvl_ap = Button(root, fg='green', bg='black', height='3', width='14', text='Поднять уровень', activebackground='#006400',
                       relief=RIDGE, command=lvl_up)
#fram = LabelFrame(height='100', width='300')
#info = Label(fram, fg='green', bg='black', height='10', width='30', text="Новое сообщение").pack()

#VISUALIZATION

day.grid(row=1, column=0)
_day.grid(row=1, column=1)
money.grid(row=1, column=3)
_money.grid(row=1, column=4, columnspan=1)
moneyS.grid(row=1, column=5)
_moneyS.grid(row=1, column=6)
level.grid(row=2, column=4, padx=10)
_level.grid(row=2, column=5, padx=5)

dolar_buy.grid(row=3, column=0)
_dolar_buy.grid(row=3, column=1)
dolar_sell.grid(row=4, column=0)
_dolar_sell.grid(row=4, column=1)

button_next_day.grid(row=2, column=0)
button_buy.grid(row=2, column=1)
button_sell.grid(row=2, column=2)
button_lvl_ap.grid(row=2, column=3)

prib.grid(row=6, column=0, columnspan=1)
#fram.grid(row=3, column=1, columnspan=6, rowspan=5)
#-----------------------------------

root.mainloop()

