from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter.font import Font
import winsound
#  ***************П р о в е р к и 
def klava(event):
    
    prov_fio()
    
def klava_d(event):
    
    prov1()

def prov_fio():

    global nadp1_1
    stroka = fio.get().lower()
    rus_alf = 'йцукенгшщзхъфывапролджэячсмитьбюё '
    fl = True
    for i in range(len(stroka)):
        if stroka[i] not in rus_alf:
            fl = False
    if fl == True and len(stroka) > 0:
        res = '                    '
        nadp1_1.configure(text=res)
        obrabotka_fio()
    else:
        res = "Допущена ошибка ввода"
        nadp1_1.configure(text=res)

# ************************
def prov1():
    global nadp1_1
    if okno == 1:
        x = int(combo1.get())
        y_m = combo2.get()
    if okno == 2:
        x = int(combo3.get())
        y_m = combo4.get()

    spisok_mec = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    y = spisok_mec.index(y_m)+1
 
    if pole1.get() == '':
        god = 0
    else:
        god = int(pole1.get())

    z = god

    if z == 0:
        fl1 = False
    else:
        fl1 = True
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        if x > 31 or x < 0:
            fl = False
        else:
            fl = True

    elif y == 2:
        if x > 29 or x < 0:
            fl = False
        else:
            fl = True

    elif y == 4 or y == 6 or y == 9 or y == 11:
        if x > 30 or x < 0:
            fl = False
        else:
            fl = True
    if fl == True and fl1 == True:
        res = '                    '
        nadp1_1.configure(text=res)
        if okno == 1:
            obrabotka_data_rozhdenia1()
        if okno == 2:
            obrabotka_data_rozhdenia2()
    else:
        res = "Допущена ошибка ввода"
        nadp1_1.configure(text=res)

#  ***************ОКНО 2 *************** ВВОД ДАННЫХ
def new_wind2():
    foregroundColor = "#FFFFFF"
    backgroundColor = "#6699FF"
    
    wind2 = Toplevel()
    wind2.title('Ч И С Л О   С У Д Ь Б Ы.  В В О Д   Д А Н Н Ы Х.')
    wind2.geometry('800x600+100+100')
    wind2.iconbitmap("atom.ico")
    wind2.configure(background= backgroundColor)
    
    global pole1
    global combo1
    global combo2
    global nadp1_1
    global okno

    okno = 1

    ramka = Frame(wind2, bg="#6699FF")
    nadp = Label(wind2, text='Введите дату своего рождения', font=("Monotype Corsiva", "25"), width=60, height=3, bg="#6699FF", fg= "#FFFFFF")
    nadp1 = Label(wind2, text=' день / месяц/ год', font=("Monotype Corsiva", "25"), width=60, height=2, bg="#6699FF", fg= "#FFFFFF")
    pole1 = Entry(ramka, width=4, font="Arial 20")
    knopka_ok = Button(ramka, text=' '.join(list('ОК'.title())), font=("Monotype Corsiva", "15"), width=6, height=1, command=prov1,fg='#FFFF33', bg='#3300CC')
    knopka_nazad = Button(wind2, text=' '.join(list('НАЗАД'.title())), font=("Monotype Corsiva", "20"), width=10, height=1, command=wind2.destroy,fg='#FFFF33', bg='#3300CC')
    nadp1_1 = Label(wind2, text='',  font=("Monotype Corsiva", "25"), width=30, height=1, fg="#3300CC", bg="#6699FF")
    lll = Label(ramka, text=' / ',  font="Arial 20", width=3, height=2, bg="#6699FF", fg= "#FFFFFF")
    lll.grid(column=1, row=0)
    lll1 = Label(ramka, text=' / ', font="Arial 20", width=3, height=2, bg="#6699FF", fg= "#FFFFFF")
    lll1.grid(column=3, row=0)
    pole1.insert(0, "2000")
    combo1 = Combobox(ramka, font="Arial 20", width=3, height=12)
    combo1['values'] = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    combo1.current(0)  # вариант по умолчанию
    combo1.grid(column=0, row=0)

    combo2 = Combobox(ramka, font="Arial 20", width=10, height=12)
    combo2['values'] = (
    'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    combo2.current(0)  # вариант по умолчанию
    combo2.grid(column=2, row=0)
       
    nadp.pack()
    nadp1.pack()
    ramka.pack()
    nadp1_1.pack()
    pole1.grid(row=0, column=5, padx=7, pady=5)
    knopka_ok.grid(row=0, column=6)
    knopka_nazad.pack(pady=7)
    wind2.bind('<Return>',klava_d)
   
       
    wind2.mainloop()

    # *************ОКНО 3   ***  Расчет магического числа

def obrabotka_data_rozhdenia1():

    chislo = int(combo1.get())

    spisok_mec = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    mesaz = spisok_mec.index(combo2.get())+1

    god = int(pole1.get())
    summa = chislo + mesaz + god
    while summa >= 10:
        strsumm = str(summa)
        s = 0
        for i in range(len(strsumm)):
            s += int(strsumm[i])
        summa = s
    mag_ch = str(summa)
  
    # **************************
    foregroundColor = "#FFFFFF"
    backgroundColor = "#6699FF"
    
    wind3 = Toplevel()
    wind3.title('Ч И С Л О   С У Д Ь Б Ы')

    wind3.rowconfigure(0, minsize=300, weight=1)
    wind3.columnconfigure(1, minsize=300, weight=1)
    wind3.geometry('800x600+100+100')
    wind3.iconbitmap("atom.ico") 
    wind3.configure(background= backgroundColor)
    
    ramka = Frame(wind3, bg="#6699FF")
    txt_rez = scrolledtext.ScrolledText(wind3, width=12, height=25, bg="#6699FF", fg= "#FFFFFF")
    l1 = Label(ramka, text=" Число судьбы", font="Arial 100 bold", width=4, height=1, fg="#FFFFFF", bg="#6699FF")
    knopka_nazad = Button(ramka, text=' '.join(list('НАЗАД'.title())), font=("Monotype Corsiva", "20"), width=10, height=1, command=wind3.destroy,fg='#FFFF33', bg='#3300CC')
    c = Canvas(master=ramka, height=250, width=300, bg="#6699FF")
    
    tree = PhotoImage(file="GIF\Пифагор.gif")
    im1 = c.create_image(0, 0, image=tree, anchor ="nw")
   
    ramka.grid(row=0, column=0)
    #, sticky="ns")
    l1.grid(row=0, column=0, sticky="ns")
    c.grid(row=1, column=0)
    
    txt_rez.grid(row=0, column=1, sticky="nsew", pady=40)
    knopka_nazad.grid(row=2, column=0, pady = 40)

    l1["text"] = f"{mag_ch}"
    hh = open(f"Meaning\ch-{mag_ch}.txt", "r", encoding="utf-8")
 
    text = hh.read()
    txt_rez.insert(END, text)
    txt_rez.configure(font=("Monotype Corsiva", "15"))
    wind3.mainloop()


#  ***************ОКНО 4**************** КВАДРАТ*******************

def new_wind4():
    foregroundColor = "#FFFFFF"
    backgroundColor = "#6699FF"

    wind4 = Tk()
    wind4.title('М А Г И Ч Е С К И Й   К В А Д Р А Т . В В О Д   Д А Н Н Ы Х.')
    wind4.geometry('800x600+100+100')
    wind4.iconbitmap("atom.ico")
    wind4.configure(background= backgroundColor)
    
    global pole1
    global combo3
    global combo4
    global nadp1_1
    global okno

    okno = 2
    ramka = Frame(wind4, bg="#6699FF")
    nadp = Label(wind4, text='Введите дату своего рождения', font=("Monotype Corsiva", "25"), width=60, height=3, bg="#6699FF", fg= "#FFFFFF")
    nadp1 = Label(wind4, text=' день / месяц/ год', font=("Monotype Corsiva", "25"), width=60, height=2, bg="#6699FF", fg= "#FFFFFF")
    pole1 = Entry(ramka, width=4, font="Arial 20")
    knopka_ok = Button(ramka, text=' '.join(list('ОК'.title())),font=("Monotype Corsiva", "15"), width=6, height=1,command=prov1,fg='#FFFF33', bg='#3300CC')
    knopka_nazad = Button(wind4, text=' '.join(list('НАЗАД'.title())), font=("Monotype Corsiva", "20"), width=10, height=1, command=wind4.destroy,fg='#FFFF33', bg='#3300CC')
    nadp1_1 = Label(wind4, text='',  font=("Monotype Corsiva", "25"), width=30, height=3, fg="#3300CC", bg="#6699FF")
    pole1.insert(0, "2000")

    lll = Label(ramka, text=' / ', font="Arial 20", width=3, height=2, bg="#6699FF", fg= "#FFFFFF")
    lll.grid(column=1, row=0)
    lll1 = Label(ramka, text=' / ', font="Arial 20", width=3, height=2, bg="#6699FF", fg= "#FFFFFF")
    lll1.grid(column=3, row=0)

    combo3 = Combobox(ramka, font="Arial 20", width=4, height=12)
    combo3['values'] = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    combo3.current(0)  # вариант по умолчанию
    combo3.grid(column=0, row=0)

    combo4 = Combobox(ramka, font="Arial 20", width=10, height=12)
    combo4['values'] = (
    'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    combo4.current(0)  # вариант по умолчанию
    combo4.grid(column=2, row=0)

    nadp.pack()
    nadp1.pack()
    ramka.pack()
    nadp1_1.pack()
    pole1.grid(row=0, column=5, padx=7, pady=5)
    knopka_ok.grid(row=0, column=6)
    knopka_nazad.pack(pady=7)
    wind4.bind('<Return>',klava_d)
    
    wind4.mainloop()
       
   # ****************ОКНО 5 ************************
def obrabotka_data_rozhdenia2():
 
    spisok_mec = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    combo4_ch = spisok_mec.index(combo4.get())+1
    x1 = combo3.get() + str(combo4_ch) + pole1.get()

    sss1 = 0
    for i in range(len(x1)):
        sss1 += int(x1[i])
    if sss1 >= 10:
        sss2 = int(str(sss1)[0]) + int(str(sss1)[1])
    else:
        sss2 = sss1
    sss3 = sss1 - sss2
    if sss3 >= 10:
        sss4 = int(str(sss3)[0]) + int(str(sss3)[1])
    else:
        sss4 = sss3

    x1 = x1 + str(sss1) + str(sss2) + str(sss3) + str(sss4)

    sp_1 = '1' * x1.count('1')
    sp_2 = '2' * x1.count('2')
    sp_3 = '3' * x1.count('3')
    sp_4 = '4' * x1.count('4')
    sp_5 = '5' * x1.count('5')
    sp_6 = '6' * x1.count('6')
    sp_7 = '7' * x1.count('7')
    sp_8 = '8' * x1.count('8')
    sp_9 = '9' * x1.count('9')

    slobar = {
        '1': '  1 — абсолютный эгоист, собственные интересы всегда \n на первом месте, даже если они вредят окружающим;\n',
        '11': '  11 — почти эгоист, но есть шанс, что будет зациклен \n не только на себе. \n Любит заниматься самовосхвалением, постоянно презентует себя с лучшей стороны;\n',
        '111': '  111 — золотая середина.\n Человек покладист, с ним легко договориться. \n Он быстро идёт на контакт;\n',
        '1111': '  1111 — уже ближе к золотой середине. \n Человек с очень большой силой воли, с закалённым характером;\n',
        '11111': '  11111 — прекрасно развиты диктаторские качества.\n  Такого человека можно назвать самодуром. \n Диктует всем свои правила;\n',
        '111111': '  111111 — такое значение бывает у людей очень жёстких, \n с трудным характером. Но несмотря на склонность к диктаторству, \n для близких людей человек готов сделать всё, что угодно;\n',
        '2': '  2 — биоэнергия присутствует, но требуются дополнительные \n источники. Такому человеку желательно заниматься спортом;\n',
        '22': '  22 — достаточно количество биоэнергии, \n способен не только принимать её, но и делиться;\n',
        '222': '  222 — развитые экстрасенсорные способности, \n способен наполнить энергией любого человека;\n',
        '2222': '  2222 — человек обладает мощным природным магнетизмом, \n  невероятно притягателен для противоположного пола.\n',
        '3': '  3 — не зациклены на порядке,\n  упорядоченность их жизни зависит от других черт характера;\n',
        '33': '  33 — хорошо даются естественные науки,\n развита логика;',
        '333': '  333 — у человека сильно выражены способности к науке, \n он невероятно педантичен, может совершать открытия.',
        '4': '  4 — в течение жизни болеет не чаще остальных людей,\n а в старости настигает множество хворей;\n',
        '44': '  44 — у него яркий сексуальный темперамент, крепкое здоровье;\n',
        '444': '  444 — бурный темперамент, здоровье практически железное;\n',
        '5': '  5 — интуиция есть, но развита слабо. \n Редко ошибается в жизни;\n',
        '55': '  55 — интуиция развита прекрасно.\n Такой личности близки профессии юридической сферы — \n судьи, юриста, следователя;\n',
        '555': '  555 — интуиция развита превосходно,\n человек практически экстрасенс. \n Решения принимает, опираясь на предчувствия,\n но при этом почти никогда не ошибается;\n',
        '5555': '  5555 — такое встречается крайне редко. \n Много пятёрок — человек является ясновидящим.  \n Способен осознавать и понимать причины всех происходящих \n событий, предсказывать будущее;\n',
        '6': '  6 — необходима работа, связанная с физическими нагрузками;\n',
        '66': '  66 — заземленный человек, ему не нужен физический труд,  \n но очень любит заниматься спортом и активным отдыхом;\n',
        '666': '  666 — ярко развит темперамент, дает массу энергии партнёру;\n',
        '6666': '  6666 — трудоголик, отдых для него — бесполезно проведённое время;\n',
        '7': '  7 — обладает талантом, который выражен не слишком сильно,\n нужно развивать;\n',
        '77': '  77 — человек с ярко выраженными творческими способностями.  \n Это музыканты, художники;\n',
        '777': '  777 — опасный знак. Такие люди «поцелованы Богом» и,\n  как правило, ненадолго приходят в земной мир.\n Выполняют свое предназначение и уходят в мир иной;\n',
        '7777': '  7777 — ангельский знак. Либо умирает в раннем возрасте, \n либо всю жизнь живёт под какой-то смертельной опасностью;\n',
        '8': '  8 — чувство долга хорошо развито,\n  способен брать ответственность за кого-либо;\n',
        '88': '  88 — человек-помощник.\n Готов помогать окружающим, чувство долга прекрасно развито;\n',
        '888': '  888 — человек создан, чтобы служить народу. \n  Из него получится хороший политик, военнослужащий;\n',
        '8888': '  8888 — крайне редкое явление. \n Человек с сильными парапсихологическими способностями, \n гений точных наук;\n',
        '9': '  9 — умственные способности необходимо  развивать \n тяжелыми усилиями;\n',
        '99': '  99 — умный человек, но ему нужно много учиться,\n чтобы добиться успеха;\n',
        '999': '  999 — сильно развит интеллект, великолепные умственные способности. \n  Опасно то, что благодаря тому, что все легко дается, \n не прилагает усилий и в результате может деградировать;\n',
        '9999': '  9999 — грубый и жестокий, но очень умный человек, \n язвительный интеллектуал'}
    foregroundColor = "#FFFFFF"
    backgroundColor = "#6699FF"
    
    wind5 = Toplevel()
    wind5.title("П С И Х О М А Т Р И Ц А ")

    wind5.rowconfigure(0, minsize=600, weight=1)
    wind5.columnconfigure(1, minsize=600, weight=1)
    wind5.geometry('800x700+100+100')
    wind5.iconbitmap("atom.ico")
    wind5.configure(background= backgroundColor)
    
    ramka1 = Frame(wind5, bg='#6699FF', bd=2, relief=RAISED)
    zzz1 = Label(wind5, text="Нельзя рассматривать значение символов из таблицы Пифагора по отдельности. ",
                  width=70, height=1,font=("Monotype Corsiva", "18"),  bg="#6699FF", fg= "#191970")
    zzz2 = Label(wind5, text="Характер нужно оценивать, анализируя все значения совместно. ", width=70,
                 height=1, font=("Monotype Corsiva", "18"),  bg="#6699FF", fg= "#191970")
    nadp1_1 = Button(ramka1, text='    ХАРАКТЕР    ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_2 = Button(ramka1, text='    ЭНЕРГИЯ     ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_3 = Button(ramka1, text='ИНТЕРЕС К НАУКАМ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_4 = Button(ramka1, text='    ЗДОРОВЬЕ    ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_5 = Button(ramka1, text='     ЛОГИКА     ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_6 = Button(ramka1, text='      ТРУД      ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_7 = Button(ramka1, text='     УДАЧА      ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_8 = Button(ramka1, text=' ЧУВСТВО ДОЛГА  ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    nadp1_9 = Button(ramka1, text='   УМ. ПАМЯТЬ   ', font=("Monotype Corsiva", "15"), width=20, height=1, fg="#FFFFFF",bg='#3300CC')
    ch1 = Label(ramka1, text=f"{sp_1}", font="Arial 12 bold", width=20, height=1)
    ch2 = Label(ramka1, text=f"{sp_2}", font="Arial 12 bold", width=20, height=1)
    ch3 = Label(ramka1, text=f"{sp_3}", font="Arial 12 bold", width=20, height=1)
    ch4 = Label(ramka1, text=f"{sp_4}", font="Arial 12 bold", width=20, height=1)
    ch5 = Label(ramka1, text=f"{sp_5}", font="Arial 12 bold", width=20, height=1)
    ch6 = Label(ramka1, text=f"{sp_6}", font="Arial 12 bold", width=20, height=1)
    ch7 = Label(ramka1, text=f"{sp_7}", font="Arial 12 bold", width=20, height=1)
    ch8 = Label(ramka1, text=f"{sp_8}", font="Arial 12 bold", width=20, height=1)
    ch9 = Label(ramka1, text=f"{sp_9}", font="Arial 12 bold", width=20, height=1)

    nadp1_1.grid(row=0, column=0)
    ch1.grid(row=1, column=0)
    nadp1_2.grid(row=2, column=0)
    ch2.grid(row=3, column=0)
    nadp1_3.grid(row=4, column=0)
    ch3.grid(row=5, column=0)
    nadp1_4.grid(row=0, column=1)
    ch4.grid(row=1, column=1)
    nadp1_5.grid(row=2, column=1)
    ch5.grid(row=3, column=1)
    nadp1_6.grid(row=4, column=1)
    ch6.grid(row=5, column=1)
    nadp1_7.grid(row=0, column=2)
    ch7.grid(row=1, column=2)
    nadp1_8.grid(row=2, column=2)
    ch8.grid(row=3, column=2)
    nadp1_9.grid(row=4, column=2)
    ch9.grid(row=5, column=2)

    txt_rez = scrolledtext.ScrolledText(wind5, width=80, height=16, bg="#6699FF", fg= "#FFFFFF")

    knopka_nazad = Button(wind5, text=' '.join(list('НАЗАД'.title())),font=("Monotype Corsiva", "20"), width=10, height=1, command=wind5.destroy,fg='#FFFF33', bg='#3300CC')

    ramka1.pack()
    zzz1.pack()
    zzz2.pack()
    txt_rez.pack()
    knopka_nazad.pack(pady=7)

    if sp_1 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_1])
    if sp_2 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_2])
    else:
        txt_rez.insert(END,
                       ' \n Если 2 отсутствует — человек лишён собственной энергии,  \n но он, словно пустой сосуд, готов наполняться энергией извне, воспитанный, \n хорошо относится к окружающим;\n')
    if sp_3 in slobar:
        txt_rez.insert(END, '\n'+slobar[sp_3])
    else:
        txt_rez.insert(END,
                       ' \n Если 3 отсутствует — человек с сильно развитой пунктуальностью. \n Перфекционист, порядок должен быть во всём;\n')
    if sp_4 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_4])
    else:
        txt_rez.insert(END,
                       ' \n Если 4 отсутствует — слабое здоровье, легко подхватывает любую заразу,\n нужно постоянно укреплять иммунитет ;\n')
    if sp_5 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_5])
    else:
        txt_rez.insert(END,
                       ' \n Если 5 отсутствует — человек лишён интуиции, у него нет «шестого чувства»,\n поэтому все решения принимает, руководствуясь логикой и здравым смыслом;\n')
    if sp_6 in slobar:
        txt_rez.insert(END,'\n'+ slobar[sp_6] )
    else:
        txt_rez.insert(END,
                       ' \n Если 6 отсутствует — человек-ремесленник, в образовании не нуждается,\n не любит заниматься физическим трудом;\n')
    if sp_7 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_7])
    else:
        txt_rez.insert(END,
                       ' \n Если 7 отсутствует — жизнь человеку дается тяжело, он много работает, \n чтобы обеспечить достойный уровень жизни. \n Есть вероятность, что уйдёт в религию;\n')
    if sp_8 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_8])
    else:
        txt_rez.insert(END, ' \n Если 8 отсутствует: человек-потребитель, \n предпочитает брать и никогда не отдаёт;\n')
    if sp_9 in slobar:
        txt_rez.insert(END, '\n'+ slobar[sp_9])
    txt_rez.configure(font=("Monotype Corsiva", "14"))
   
    wind5.mainloop()

#  ***************ОКНО 6 ************  Ф И О ***************

def new_wind6():
    foregroundColor = "#FFFFFF"
    backgroundColor = "#6699FF"
    
    wind6 = Toplevel()
    wind6.title('К О Д  С У Д Ь Б Ы   П О  И М Е Н И. В В О Д  Д А Н Н Ы Х.')
    wind6.geometry('800x600+100+100')
    wind6.iconbitmap("atom.ico")
    wind6.configure(background= backgroundColor)
    
    global fio
    global nadp1_1

    ramka = Frame(wind6, bg="#6699FF")
    nadp = Label(wind6, text='Введите своё имя и фамилию', font=("Monotype Corsiva", "25"), width=50, height=3, bg="#6699FF", fg= "#FFFFFF")
    nadp1 = Label(wind6, text='буквами русского алфавита', font=("Monotype Corsiva", "25"), width=50, height=2, bg="#6699FF", fg= "#FFFFFF")
    nadp1_1 = Label(wind6, text='', font=("Monotype Corsiva", "25"), width=30, height=2, fg="#3300CC", bg="#6699FF")
    fio = Entry(ramka, width=50, font="Arial 18")
    knopka_ok = Button(ramka, text=' '.join(list('ОК'.title())), font=("Monotype Corsiva", "15"), width=6, height=1, command=prov_fio,fg='#FFFF33', bg='#3300CC')
    knopka_nazad = Button(wind6, text=' '.join(list('НАЗАД'.title())), font=("Monotype Corsiva", "20"), width=10, height=1, command=wind6.destroy,fg='#FFFF33', bg='#3300CC')

    nadp.pack()
    nadp1.pack()
    ramka.pack()
    nadp1_1.pack()
    fio.grid(row=0, column=0)
    fio.focus()
    knopka_ok.grid(row=0, column=1, padx=7, pady=5)
    knopka_nazad.pack()
    
    wind6.bind('<Return>',klava)
    
    wind6.mainloop()


# *************ОКНО 7
# *** Расчет кода судьбы имени
def obrabotka_fio():
    alf = {'а': '1', 'б': '2', 'в': '3', 'г': '4', 'д': '5', 'е': '6', 'ё': '7', 'ж': '8', 'з': '9', 'и': '1', 'й': '2',
           'к': '3', 'л': '4', 'м': '5', 'н': '6', 'о': '7', 'п': '8', 'р': '9', 'с': '1', 'т': '2', 'у': '3', 'ф': '4',
           'х': '5', 'ц': '6', 'ч': '7', 'ш': '8', 'щ': '9', 'ъ': '1', 'ы': '2', 'ь': '3', 'э': '4', 'ю': '5',
           'я': '6', }
    x = fio.get()
    x1 = x.lower()
    x2 = x1.replace(' ', '')
    s = 0
    for i in range(len(x2)):
        if x2[i] in alf:
            s += int(alf[x2[i]])
    summa = s
    while summa >= 10:
        strsumm = str(summa)
        s = 0
        for i in range(len(strsumm)):
            s += int(strsumm[i])
        summa = s

    if summa == 1:
        mag_code = " Солнце"
        tree = PhotoImage(file="GIF\Солнце.gif", height=320, width=300)
    elif summa == 2:
        mag_code = " Луна"
        tree = PhotoImage(file="GIF\Луна.gif", height=320, width=300)
    elif summa == 3:
        mag_code = " Марс"
        tree = PhotoImage(file="GIF\Марс.gif", height=320, width=300)
    elif summa == 4:
        mag_code = " Меркурий"
        tree = PhotoImage(file="GIF\Меркурий.gif", height=320, width=300)
    elif summa == 5:
        mag_code = " Юпитер"
        tree = PhotoImage(file="GIF\Юпитер.gif", height=320, width=300)
    elif summa == 6:
        mag_code = " Венера"
        tree = PhotoImage(file="GIF\Венера.gif", height=320, width=300)
    elif summa == 7:    
        mag_code = " Сатурн"
        tree = PhotoImage(file="GIF\Сатурн.gif", height=320, width=300)
    elif summa == 8:
        mag_code = " Уран"
        tree = PhotoImage(file="GIF\Уран.gif", height=320, width=300)
    elif summa == 9:
        mag_code = " Нептун"
        tree = PhotoImage(file="GIF\Нептун.gif", height=320, width=300)
    else:
        mag_code = " ОШИБКА"
    # **************************
    foregroundColor = "#FFFFFF"
    backgroundColor = "#6699FF"
    
    wind7 = Toplevel()
    wind7.title("К О Д  С У Д Ь Б Ы   П О  И М Е Н И")

    wind7.rowconfigure(0, minsize=400, weight=1)
    wind7.columnconfigure(1, minsize=400, weight=1)
    wind7.geometry('800x600+100+100')
    wind7.iconbitmap("atom.ico")
    wind7.configure(background= backgroundColor)
    
    txt_rez = scrolledtext.ScrolledText(wind7, width=10, height=10, bg="#6699FF", fg= "#FFFFFF")
    ramka = Frame(wind7, bg ="#000000")
    l1 = Label(ramka, text=" Картинка ", font="Arial 40 bold", bg ="#000000",width=8, height=3, fg="#6699FF")
    knopka_nazad = Button(wind7, text=' '.join(list('НАЗАД'.title())), font=("Monotype Corsiva", "20"), width=9, height=1, command=wind7.destroy,fg='#FFFF33', bg='#3300CC')

    c = Canvas(master=ramka, height=320, width=300, bg ="#000000",highlightthickness=0) 
    c.grid(row=1, column=0)
    im1 = c.create_image(20, 0, image=tree, anchor=NW)

    l1.grid(row=0, column=0)
    ramka.grid(row=0, column=0, sticky="ns")
    txt_rez.grid(row=0, column=1, sticky="nsew")

    knopka_nazad.grid(row=1, column=1, pady=7)

    l1["text"] = f"{mag_code}"
    hh = open(f"Meaning\Pech_{summa}.txt", "r", encoding="utf-8")
    text = hh.read()
    txt_rez.insert(END, text)
    txt_rez.configure(font=("Monotype Corsiva", "18"), pady=50)
    wind7.mainloop()

#  ***************ОКНО 1     Г Л А В Н О Е **************

foregroundColor = "#FFFFFF"
backgroundColor = "#6699FF"

#winsound.PlaySound('music.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

root = Tk()
root.title("Н У М Е Р О Л О Г И Я")
root.geometry('800x600+100+100')

root.iconbitmap("atom.ico")
root.configure(background= backgroundColor)


nadp = Label(root, text='Привет!', font=("Monotype Corsiva", "22"), width=10, height=2, fg=foregroundColor, bg=backgroundColor)
nadp1 = Label(root, text='Если ты хочешь узнать себя чуть лучше, то давай приступим!', font=("Monotype Corsiva", "22"), width=60,
              height=3,fg=foregroundColor, bg=backgroundColor)
knopka1 = Button(root, text=' '.join(list('РАССЧИТАТЬ ЧИСЛО СУДЬБЫ'.title())), width=45, height=1, font=("Monotype Corsiva", "18"), bg='#3300CC',
                 command=new_wind2,fg='#FFFF33')
knopka2 = Button(root, text=' '.join(list('МАГИЧЕСКИЙ КВАДРАТ ПИФАГОРА'.title())), width=45, height=1, font=("Monotype Corsiva", "18"), bg='#3300CC',
                 command=new_wind4,fg='#FFFF33')
knopka3 = Button(root, text=' '.join(list('РАССЧИТАТЬ КОД СУДЬБЫ ПО ИМЕНИ'.title())), width=45, height=1, font=("Monotype Corsiva", "18"), bg='#3300CC',
                 command=new_wind6,fg='#FFFF33')
knopka4 = Button(root, text=' '.join(list('ВЫХОД'.title())), width=20, height=1, font=("Monotype Corsiva", "14"), bg='#3300CC', command=root.destroy,fg='#FFFF33')

nadp.pack()
nadp1.pack()
knopka1.pack()
knopka2.pack()
knopka3.pack()
knopka4.pack()
winsound.PlaySound('music.wav',winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
root.mainloop()
