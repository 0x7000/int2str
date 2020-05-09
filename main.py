#!/usr/bin/env python3
from Sayi2Metin import Cevir
from tkinter import Tk, Label, Entry, Button, END


def main():
	Pencere.geometry("450x250+10+10")
	Pencere.mainloop()


def hesapla():
	veri = str(xinput.get())
	if veri.isnumeric():
		veri = veri.lstrip("0")
	if len(veri) <= 6:
		sonuc = Cevir(veri)
		xlabel2.config(text=sonuc.yaz)
	elif len(veri) == 7:
		milyon = Cevir(veri[0])
		yuzbin = Cevir(veri[1:])
		x, y = milyon.yaz, yuzbin.yaz
		xlabel2.config(text=x + " Milyon. " + y)
	elif len(veri) == 8:
		milyon = Cevir(veri[:2])
		yuzbin = Cevir(veri[2:])
		x, y = milyon.yaz, yuzbin.yaz
		xlabel2.config(text=x + " Milyon " + y)
	else:
		xlabel2.config(text="Sekiz basamaktan büyük sayı girdiniz.")


Pencere = Tk()
Pencere.title("Sayı > Metin")
xlabel = Label(Pencere, text="Sayı Girişi : ")
xlabel.place(x=10, y=10)
xlabel2 = Label(Pencere, text="Sonuç : ")
xlabel2.place(x=90, y=40)
xinput = Entry(Pencere, bd=1)
xinput.place(x=90, y=10)
xbuton = Button(Pencere, text="Yazdır.", command=hesapla)
''' KP_enter = numpad altındaki küçük enter, Return = büyük olan '''
xbuton.bind_all("<KP_Enter>", lambda x: hesapla())
xbuton.place(x=10, y=30)
xbuton2 = Button(Pencere, text="Sil.", command=lambda: xinput.delete(0, END))
xbuton2.bind_all("<Delete>", lambda x: xinput.delete(0, END))
xbuton2.place(x=10, y=60)


if __name__ == "__main__":
	main()
