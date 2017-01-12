from Tkinter import *

root = Tk()

root.title("menu dla zbiorow")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="nowy", command=None)
filemenu.add_command(label="otworz", command=None)
filemenu.add_command(label="nagraj", command=None)
filemenu.add_command(label="nagraj jako...", command=None)
filemenu.add_command(label="zamknij", command=None)

filemenu.add_separator()

filemenu.add_command(label=u"wyjscie", command=root.quit)
menubar.add_cascade(label="Zbior", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="cofnij", command=None)

editmenu.add_separator()

editmenu.add_command("wytnij", command=None)
editmenu.add_command("kopiuj", command=None)
editmenu.add_command("wklej", command=None)
editmenu.add_command("usun", command=None)
editmenu.add_command("wybierz wszystko", command=None)

menubar.add_cascade(label="edycja, menu=editmenu")
helpmenu = Menu(menubar, tearoof=0)
helpmenu.add_command(label="indeks pomocy", command=None)
helpmenu.add_command(label="0...", command=None)
menubar.add_cascade(label="Pomoc", menu=helpmenu)

root.config(menu=menubar)
root.mainloop
