#!/usr/bin/env python3
from Sayi2Metin import Cevir
from tkinter import Tk, Label, Entry, Button, END


def main():
	Pencere.geometry("780x280+10+10")
	Pencere.mainloop()


def hesapla():
	veri = str(xinput.get())
	sonuc = Cevir(veri)
	mesaj = sonuc.yaz
	xinput2.delete(0, END)
	xinput2.insert(0, mesaj)


Pencere = Tk()
Pencere.title("Sayı > Metin")

xlabel = Label(Pencere, text="Sayı Girişi : ")
xlabel.place(x=10, y=10)

xlabel2 = Label(Pencere, text="Sonuç : ")
xlabel2.place(x=90, y=40)

xinput = Entry(Pencere, bd=1)
xinput.place(x=90, y=10)

xinput2 = Entry(Pencere, bd=1, width=90)
xinput2.place(x=90, y=60)

xbuton = Button(Pencere, text="Yazdır.", command=hesapla)
xbuton.bind_all("<KP_Enter>", lambda x: hesapla())
# bazı linux sistemlerde Return ve KP_Enter olarak ayrı ayrı kullanılıyor
xbuton.place(x=10, y=30)

xbuton2 = Button(Pencere, text="Sil.", command=lambda: xinput.delete(0, END))
xbuton2.bind_all("<Delete>", lambda x: xinput.delete(0, END))
xbuton2.place(x=10, y=60)


if __name__ == "__main__":
	main()
