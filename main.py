#!/usr/bin/env python3
from Sayi2Metin import Cevir
from tkinter import *


def main():
	Pencere.geometry("450x250+10+10")
	Pencere.mainloop()


def hesapla():
	sonuc = Cevir(xinput.get())
	xlabel2.config(text=sonuc.yaz)


Pencere = Tk()
Pencere.title("Sayı2Metin")
xlabel = Label(Pencere, text="Sayı Girişi : ")
xlabel.place(x=10, y=10)
xlabel2 = Label(Pencere, text="Sonuç : ")
xlabel2.place(x=90, y=40)
xinput = Entry(Pencere, bd=1)
xinput.place(x=90, y=10)
xbuton = Button(Pencere, text="Yazdır.", command=hesapla)
xbuton.bind_all("<Return>", lambda x: hesapla())
xbuton.place(x=10, y=30)
xbuton2 = Button(Pencere, text="Sil.", command=lambda: xinput.delete(0, END))
xbuton2.place(x=10, y=60)


if __name__ == "__main__":
	main()
