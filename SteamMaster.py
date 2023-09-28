import customtkinter as CTk
from tkinter import messagebox
import tkinter as tk
import pickle
from tkinter import *
import subprocess
import webbrowser
import os
from PIL import Image, ImageTk
import threading
import sys


CTk.set_appearance_mode('dark')
CTk.set_default_color_theme('blue')

win_exit_log = 0

#Первое окно

# проверяем, есть ли файл с данными пользователей
try:
    with open("users.pickle", "rb") as f:
        users = pickle.load(f)
except FileNotFoundError:
    users = {}

username = 0
password = 0

# функция регистрации нового пользователя
def register():
    global username
    global password
    username = EntryLogin.get()
    password = EntryPassword.get()
    password_confirm = EntryPasswordRep.get()
    if username and password and password_confirm:
        if username in users:
            messagebox.showinfo("Аккаунт", "Данный логин занят. Пожалуйста, придумайте новый.")
            return
        if password == password_confirm:
            users[username] = password
            with open("users.pickle", "wb") as f:
                pickle.dump(users, f)
            messagebox.showinfo("Аккаунт", "Пользователь зарегистрирован.")
            ex_win1()
        else:
            messagebox.showinfo("Аккаунт", "Пароли не совпадают. Попробуйте еще раз.")
    else:
        messagebox.showinfo("Аккаунт", "Данные введены не во все поля")

def login():
    global username
    global password
    username = EntryLoginLogin.get()
    password = EntryPasswordLogin.get()
    if username and password:
        if username in users and users[username] == password:
            messagebox.showinfo("Аккаунт", "Вы успешно вошли в аккаунт.")
            ex_win1()
        else:
            messagebox.showinfo("Аккаунт", "Неверный логин или пароль.")
    else:
        messagebox.showinfo("Аккаунт", "Данные введены не во все поля")

def pizza_log():
    webbrowser.open('https://dodopizza.ru/irkutsk/pizza/burger-pizza', new=2)

def ex_win1():
    global win_exit_log
    win_exit_log += 1
    win1.destroy()

win1 = CTk.CTk()
win1.geometry('400x300')
win1.resizable(False,False)
win1.title('SteamPro')
icon_steam = 'Images/steam.ico'
win1.iconbitmap('Images/steam.ico')



#Виджеты

tabview = CTk.CTkTabview(win1)
tabview.pack(padx=20, pady=20)

tabview.add("Регистрация")  # add tab at the end
tabview.add("Вход")  # add tab at the end
tabview.add("Что выбрать?")  # add tab at the end
tabview.set("Регистрация")  # set currently visible tab

#reg
EntryLogin = CTk.CTkEntry(tabview.tab("Регистрация"), placeholder_text="Логин", width=170, justify='center')
EntryLogin.pack(padx=20, pady=20)

EntryPassword = CTk.CTkEntry(tabview.tab('Регистрация'),placeholder_text="Пароль",show='*',width=170,justify='center')
EntryPassword.pack(padx=20, pady=1)

EntryPasswordRep = CTk.CTkEntry(tabview.tab('Регистрация'),placeholder_text="Повторите пароль",show='*',width=170,justify='center')
EntryPasswordRep.pack(padx=20, pady=20)

ButtonReg = CTk.CTkButton(tabview.tab("Регистрация"), text='Зарегистрироваться', command=register)
ButtonReg.pack(padx=20, pady=1)

#log

EntryLoginLogin = CTk.CTkEntry(tabview.tab("Вход"), placeholder_text="Логин", width=170, justify='center')
EntryLoginLogin.pack(padx=20, pady=20)

EntryPasswordLogin = CTk.CTkEntry(tabview.tab("Вход"), placeholder_text="Пароль", width=170, justify='center', show='*')
EntryPasswordLogin.pack(padx=20, pady=1)

ButtonLogin = CTk.CTkButton(tabview.tab("Вход"), text='Войти', command=login)
ButtonLogin.pack(padx=20, pady=20)

#What to choose
LabelWhatToChoose = CTk.CTkLabel(tabview.tab("Что выбрать?"), text='Что выбрать?', font=('Arial', 15))
LabelWhatToChoose.pack(padx=20, pady=1)

LabelWhatToChoose2 = CTk.CTkLabel(tabview.tab("Что выбрать?"), text='Если вы здесь впервые, то проходите')
LabelWhatToChoose2.pack(padx=20, pady=0)

LabelWhatToChoose3 = CTk.CTkLabel(tabview.tab("Что выбрать?"), text='регистрацию. Если у вас уже есть')
LabelWhatToChoose3.pack(padx=20, pady=0)

LabelWhatToChoose4 = CTk.CTkLabel(tabview.tab("Что выбрать?"), text='аккаунт, то войдите в него.')
LabelWhatToChoose4.pack(padx=20, pady=0)

ButtonPizza = CTk.CTkButton(tabview.tab("Что выбрать?"), text='Заказать автору пиццу',command=pizza_log)
ButtonPizza.pack(padx=20, pady=20)

win1.mainloop()

#Второе окно

def win():
    win = CTk.CTk()
    win.geometry('800x535')
    win.title('SteamProMaster')
    win.resizable(False, False)
    win.iconbitmap('Images/steam.ico')
    global username
    global password

    tabview = CTk.CTkTabview(win, width=760, height=515)
    tabview.place(x=20, y=0)

    tabview.add('Игры')
    tabview.add('Настройки')
    tabview.add('Накрутка денег')
    tabview.add('Дополнительно')
    tabview.add('Вывести в steam')

    #Вкладка "Игры"
    def get_game():
        messagebox.showinfo('Игры', "Данная игра добавлена в список получаемых")
    def no_get_game():
        messagebox.showinfo('Игры','Чтобы добавить данную игру в список получаемых, нужно купить премиум')
        # Первый ряд игр
    cssource_image = PhotoImage(file='Images/cs source.png')
    cssource_image = cssource_image.subsample(3, 3)
    Button_cs_sourse = Button(tabview.tab('Игры'), image=cssource_image, bd=0, activebackground='#8c8c8b', bg='#8c8c8b',
                              command=get_game)
    Button_cs_sourse.place(x=10, y=10)

    csgo_image = PhotoImage(file='Images/csgo.png')
    csgo_image = csgo_image.subsample(3, 3)
    Button_csgo = Button(tabview.tab('Игры'), image=csgo_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                         command=get_game)
    Button_csgo.place(x=157, y=10)

    rust_image = PhotoImage(file='Images/rust.png')
    rust_image = rust_image.subsample(3, 3)
    Button_rust = Button(tabview.tab('Игры'), image=rust_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                         command=get_game)
    Button_rust.place(x=306, y=10)

    worldbox_image = PhotoImage(file='Images/worldbox.png')
    worldbox_image = worldbox_image.subsample(3, 3)
    Button_worldbox = Button(tabview.tab('Игры'), image=worldbox_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                             command=get_game)
    Button_worldbox.place(x=455, y=10)

    portal2_image = PhotoImage(file='Images/portal2.png')
    portal2_image = portal2_image.subsample(3, 3)
    Button_portal2 = Button(tabview.tab('Игры'), image=portal2_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                            command=get_game)
    Button_portal2.place(x=604, y=10)

        #Второй ряд игр

    raft_image = PhotoImage(file='Images/raft.png')
    raft_image = raft_image.subsample(3, 3)
    Button_raft = Button(tabview.tab('Игры'), image=raft_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                         command=get_game)
    Button_raft.place(x=10, y=230)

    gta5_image = PhotoImage(file='Images/GTAV.png')
    gta5_image = gta5_image.subsample(3, 3)
    Button_gta5 = Button(tabview.tab('Игры'), image=gta5_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                         command=get_game)
    Button_gta5.place(x=157, y=230)

    gta6_image = PhotoImage(file='Images/gta6.png')
    gta6_image = gta6_image.subsample(3, 3)
    Button_gta6 = Button(tabview.tab('Игры'), image=gta6_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                         command=no_get_game)
    Button_gta6.place(x=306, y=230)

    cs2_image = PhotoImage(file='Images/cs2.png')
    cs2_image = cs2_image.subsample(3, 3)
    Button_cs2 = Button(tabview.tab('Игры'), image=cs2_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                        command=no_get_game)
    Button_cs2.place(x=455, y=230)

    rdr3_image = PhotoImage(file='Images/rdr3.png')
    rdr3_image = rdr3_image.subsample(3, 3)
    Button_rdr3 = Button(tabview.tab('Игры'), image=rdr3_image, bg='#8c8c8b', activebackground='#8c8c8b', bd=0,
                         command=no_get_game)
    Button_rdr3.place(x=604, y=230)


    #Настройки

        #Тема
    Label_theme = CTk.CTkLabel(tabview.tab('Настройки'), text='Тема', font=('Arial', 15))
    Label_theme.place(x=72, y=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        CTk.set_appearance_mode(new_appearance_mode)

    def on_select(value):
        change_appearance_mode_event(None, value)

    appearance_mode_optionemenu = CTk.CTkOptionMenu(tabview.tab('Настройки'), values=["Dark", "Light"],
                                                    command=on_select)
    appearance_mode_optionemenu.place(x=20, y=40)

        #Скорость работы

    Label_speed = CTk.CTkLabel(tabview.tab('Настройки'), text='Скорость работы')
    Label_speed.place(x=38, y=80)

    OptionMenu_speed=CTk.CTkOptionMenu(tabview.tab('Настройки'),values=['Высокая',"Выше среднего","Средняя","Низкая","Ах*енная"])
    OptionMenu_speed.place(x=20, y=110)

        #Язык
    Label_language = CTk.CTkLabel(tabview.tab('Настройки'), text='Язык', font=('Arial', 15))
    Label_language.place(x=72, y=150)

    OptionMenu_language = CTk.CTkOptionMenu(tabview.tab('Настройки'),values=['Русский',"Русский","Я русский","Русский"])
    OptionMenu_language.place(x=20, y=180)

    def language():
        messagebox.showinfo("Язык", "Мне кажется, что нужно выбрать русский")

    Button_language = CTk.CTkButton(tabview.tab('Настройки'), text='Как выбрать язык?', command=language)
    Button_language.place(x=20, y=220)

        #Больше функций
    def more_func():
        messagebox.showinfo('Больше функций', "Чтобы разблокировать новые функции, нужно купить премиум")

    Button_more_func = CTk.CTkButton(tabview.tab('Настройки'), text='Больше функций',command=more_func)
    Button_more_func.place(x=20, y=260)

        #switches слева
    Switch_zp_kost = CTk.CTkSwitch(tabview.tab('Настройки'), text='Повысить зп Костяну')
    Switch_zp_kost.place(x=20, y=300)

    Switch_sub_ned = CTk.CTkSwitch(tabview.tab('Настройки'), text='Подписаться на NEDOHACKERS Lite')
    Switch_sub_ned.place(x=20, y=340)

        #Озу
    Label_ozu = CTk.CTkLabel(tabview.tab('Настройки'), text='ОЗУ', font=('Arial', 20))
    Label_ozu.place(x=359, y=370)

    horizontal_Scale_ozu = CTk.CTkSlider(tabview.tab('Настройки'), from_=1, to=128, width=620)
    horizontal_Scale_ozu.place(x=70, y=400)

    Label_1gb = CTk.CTkLabel(tabview.tab('Настройки'), text='1гб', font=('Arial', 15))
    Label_1gb.place(x=45, y=393)

    Label_128gb = CTk.CTkLabel(tabview.tab('Настройки'), text='128гб', font=('Arial', 15))
    Label_128gb.place(x=697, y=393)

        #Switches справа
    Label_cheats_csgo = CTk.CTkLabel(tabview.tab('Настройки'), text='Читы(CS:GO)', font=('Arial', 15))
    Label_cheats_csgo.place(x=580, y=10)

    Switch_AIM = CTk.CTkSwitch(tabview.tab('Настройки'), text='AIM')
    Switch_AIM.place(x=570, y=50)

    Switch_wallhack = CTk.CTkSwitch(tabview.tab('Настройки'), text='WallHack')
    Switch_wallhack.place(x=570, y=80)

    Switch_BunnyHope = CTk.CTkSwitch(tabview.tab('Настройки'), text='Bunny Hop')
    Switch_BunnyHope.place(x=570, y=110)

    Switch_antivac = CTk.CTkSwitch(tabview.tab('Настройки'), text='Anti VAC')
    Switch_antivac.place(x=570, y=140)

    Switch_antipatrul = CTk.CTkSwitch(tabview.tab('Настройки'), text='Анти патруль')
    Switch_antipatrul.place(x=570, y=170)

    Switch_triggerbot = CTk.CTkSwitch(tabview.tab('Настройки'), text='TriggerbBot')
    Switch_triggerbot.place(x=570, y=200)

    Switch_radarhack = CTk.CTkSwitch(tabview.tab('Настройки'), text='RadarHack')
    Switch_radarhack.place(x=570, y=230)

    Switch_ban = CTk.CTkSwitch(tabview.tab('Настройки'), text='Получить бан')
    Switch_ban.place(x=570, y=260)

    Switch_miner = CTk.CTkSwitch(tabview.tab('Настройки'), text='Скачать майнер')
    Switch_miner.place(x=570, y=290)

    Label_Ogurec = CTk.CTkSwitch(tabview.tab('Настройки'), text='Стать огурцом')
    Label_Ogurec.place(x=570, y=320)

    #Накрутка денег
    int_value = 500  # объявляем переменную как локальную

    def money_slider(newVal):
        nonlocal int_value
        float_value = float(newVal)
        int_value = round(float_value)
        Label_money.configure(text=f'Накрутить: {int_value} рублей')

    def wind_up():
        messagebox.showinfo('Накрутка денег', f'Отлично! Вы получите {int_value} рублей после того, как нажмёте на "Получить" в разделе "Вывести в steam"')

    def how_does_it_work():
        messagebox.showinfo('Как это работает?', 'Я хз лол. Главное, что работает')

    horizontal_Scale_Money = CTk.CTkSlider(tabview.tab('Накрутка денег'), from_=0, to=1000, width=580, command=money_slider)
    horizontal_Scale_Money.place(x=90, y=25)

    Label_money = CTk.CTkLabel(tabview.tab('Накрутка денег'), text=f'Накрутить: {int_value} рублей', font=('Arial', 16))
    Label_money.place(x=294, y=45)

    Button_wind_up = CTk.CTkButton(tabview.tab('Накрутка денег'), text='Накрутить', command=wind_up)
    Button_wind_up.place(x=310, y=75)

    Button_how_does_it_work=CTk.CTkButton(tabview.tab('Накрутка денег'),text='Как это работает?',command=how_does_it_work)
    Button_how_does_it_work.place(x=310, y=110)

    #Дополнительно
    def premium():
        webbrowser.open('https://clck.ru/35Rs4Y', new=2)
    def what_premium():
        messagebox.showinfo('Премиум', "Премиум позволяет добавлять новые функции, увеличивать скорость работы программы в 17 раз, а также кастомизировать ваш аккаунт")
    def Support():
        messagebox.showinfo('Поддержка', "Мы вас поддержали")
    def select_level():
        level = Int_var_more.get()
        if level == 2:
            pass
        elif level == 1:
            messagebox.showinfo('Если что, это просто шутка', "Так и знал                       ")
    def secret():
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)
    def acc_info():
        global username
        global password
        messagebox.showinfo('Аккаунт', f"Логин: {username}\nПароль: {password}\nЗарегистрирован: сегодня")
    def prem_free():
        webbrowser.open('https://www.youtube.com/watch?v=johcE5s525M', new=2)
    def ne_nag():
        webbrowser.open('https://www.youtube.com/@nedohackerslite?view_as=subscriber', new=2)
    def author():
        webbrowser.open('https://www.youtube.com/channel/UCxbGYXWuowtcM1_jbTOaEJg', new=2)
    Button_prem = CTk.CTkButton(tabview.tab("Дополнительно"), text='Купить премиум', command=premium)
    Button_prem.place(x=10, y=17)

    Button_what_prem = CTk.CTkButton(tabview.tab("Дополнительно"), text='Что даёт премиум?', command=what_premium)
    Button_what_prem.place(x=10, y=57)

    Button_Support = CTk.CTkButton(tabview.tab("Дополнительно"), text='Поддержка', command=Support)
    Button_Support.place(x=10, y=97)

    Switch_system = CTk.CTkSwitch(tabview.tab("Дополнительно"), state='disabled', text='Сохранить систему')
    Switch_system.place(x=10, y=137)

    var = tk.BooleanVar(value=True)
    Switch_prog_5=CTk.CTkSwitch(tabview.tab("Дополнительно"),variable=var,state='disabled',text='Поставить 5 звёзд за программу')
    Switch_prog_5.place(x=10, y=177)


    Int_var_more = tk.IntVar(value=2)

    Radiobutton_gey1=CTk.CTkRadioButton(tabview.tab("Дополнительно"),variable=Int_var_more,value=1,
                                        text='Быть геем, но Костян скрывает данные',command=select_level)
    Radiobutton_gey1.place(x=10, y=207)

    Radiobutton_gey2=CTk.CTkRadioButton(tabview.tab("Дополнительно"),variable=Int_var_more,value=2,
                                        text='Быть натуралом, Костян не скрывает данные',command=select_level)
    Radiobutton_gey2.place(x=10, y=237)

    Button_Secret = CTk.CTkButton(tabview.tab("Дополнительно"), text='Секретно', command=secret)
    Button_Secret.place(x=10, y=267)

    Button_Acc_Info = CTk.CTkButton(tabview.tab("Дополнительно"), text='Информация об аккаунте',command=acc_info)
    Button_Acc_Info.place(x=10, y=300)

    Button_prem_free = CTk.CTkButton(tabview.tab("Дополнительно"), text='Бесплатный премиум', command=prem_free)
    Button_prem_free.place(x=10, y=333)

    Button_ne_nag = CTk.CTkButton(tabview.tab("Дополнительно"), text='Не нажимать', command=ne_nag)
    Button_ne_nag.place(x=10, y=366)

    Button_author = CTk.CTkButton(tabview.tab("Дополнительно"), text='Автор', command=author)
    Button_author.place(x=10, y=399)

    Button_non = CTk.CTkButton(tabview.tab('Дополнительно'), text='Пусто')
    Button_non.place(x=10, y=432)

    Label_lox = CTk.CTkLabel(tabview.tab('Дополнительно'), text='Прочитал - лох', font=('Arial', 9))
    Label_lox.place(x=670, y=440)

    #Вывести в steam

    def toggle_button_state():
        if checkbox_var.get():
            Button_start.configure(state=tk.NORMAL)
        else:
            Button_start.configure(state=tk.DISABLED)

    def start():
        threading.Thread(target=subprocess.run, args=(["Auto.exe"],)).start()

    scroble_frame = CTk.CTkScrollableFrame(tabview.tab('Вывести в steam'), label_text="Лицензионное соглашение",
                                           width=715)
    scroble_frame.place(x=5, y=20)
    Label_lic = CTk.CTkLabel(scroble_frame, text='Вы соглашаетесь, что вы получите те игры которые выбрали.\n'
                                                 'Вы соглашаетесь, что вы получаете те деньги, которые выбрали.\n'
                                                 'Вы соглашаетесь на то, что вы простак.\n'
                                                 'Вы должны согласиться, что я сигма.\n'
                                                 'Вы обязаны согласиться, что рмыгшвапгышимсгу\n'
                                                 'Ичо\n'
                                                 'Вы вот прямо обязаны согласиться, что нет\n'
                                                 'Ты реально это читаешь?\n'
                                                 'Прикольно))\n'
                                                 'Ладно, вот нормальное:\n'
                                                 '   \n'
                                                 '    \n'
                                                 '    \n'
                                                 'Повёлся', font=('Arial', 23))
    Label_lic.pack()

    checkbox_var = tk.BooleanVar()
    checkbox_var.set(False)
    checkbox = CTk.CTkCheckBox(tabview.tab('Вывести в steam'), text="Я прочитал пользовательское соглашение",
                               variable=checkbox_var, command=toggle_button_state)
    checkbox.place(x=10, y=280)

    Button_start = CTk.CTkButton(tabview.tab('Вывести в steam'), text="Вывести", state=tk.DISABLED,
                                 command=start)
    Button_start.place(x=310, y=330)


    win.mainloop()


if win_exit_log >= 1:
    win()
else:
    sys.exit()

