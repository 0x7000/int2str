#!/usr/bin/env python3
from Sayi2Metin import Sayi2Metin


def main():
    sonuc = Sayi2Metin(input("Sayi: "))
    print(sonuc.yaz) #@property ile çağrılırsa () kullanılmasına gerek yok


if __name__ == "__main__":
    main()

'''
Property, özellik, nitelik anlamlarına gelmektedir. 
Property dekoratörünün yaptığı en temel iş, bir metodu, nitelik gibi kullanılabilir hale getirmektir.
'''