class Cevir:
	def __init__(self, sayi):
		self.sayi = sayi

	def __del__(self):
		print("Obje silindi....")

	@property
	def yaz(self):
		if "," in self.sayi:
			self.sayi = self.sayi.split(",")
			kurus = self.sayi[1][0:2]
			if kurus.startswith("0"):
				return "{}, {} {}".format(self.cevir(self.sayi[0]), "Sıfır", self.cevir(kurus))
			else:
				return "{}, {}".format(self.cevir(self.sayi[0]), self.cevir(kurus))
		else:
			return "{}".format(self.cevir(self.sayi))

	@staticmethod
	def cevir(deger):
		if len(deger) == 1 and deger == "0":
			return "Sıfır"
		else:
			deger = deger.lstrip("0")
			dizi = []
			isaret = "+"
			try:
				for i in deger:
					dizi.append(i)
				if dizi[0] == "-":
					isaret = "Eksi"
					dizi.pop(0)
				dizi.reverse()
				basamak = len(dizi)
				if basamak == 1:
					sonuc = "{}".format(BIRLER[dizi[0]])
				elif basamak == 2:
					sonuc = "{} {}".format(
						ONLAR[dizi[1]],
						BIRLER[dizi[0]])
				elif basamak == 3:
					sonuc = "{} {} {}".format(
						YUZLER[dizi[2]],
						ONLAR[dizi[1]],
						BIRLER[dizi[0]])
				elif basamak == 4:
					sonuc = "{} {} {} {}".format(
						BINLER[dizi[3]],
						YUZLER[dizi[2]],
						ONLAR[dizi[1]],
						BIRLER[dizi[0]])
				elif basamak == 5:
					if dizi[3] == "0":
						sonuc = "{} {} {} {}".format(
							ONLAR[dizi[4]]+" Bin",
							YUZLER[dizi[2]],
							ONLAR[dizi[1]],
							BIRLER[dizi[0]])
					else:
						sonuc = "{} {} {} {} {}".format(
							ONLAR[dizi[4]],
							BIRLER[dizi[3]]+" Bin",
							YUZLER[dizi[2]],
							ONLAR[dizi[1]],
							BIRLER[dizi[0]])
				elif basamak == 6:
					if dizi[3] == "0":
						sonuc = "{} {} {} {} {}".format(
							YUZLER[dizi[5]],
							ONLAR[dizi[4]]+" Bin",
							YUZLER[dizi[2]],
							ONLAR[dizi[1]],
							BIRLER[dizi[0]])
					else:
						sonuc = "{} {} {} {} {} {}".format(
							YUZLER[dizi[5]],
							ONLAR[dizi[4]],
							BIRLER[dizi[3]]+" Bin",
							YUZLER[dizi[2]],
							ONLAR[dizi[1]],
							BIRLER[dizi[0]])
				else:
					sonuc = "Aralık Dışında."
				if isaret == "Eksi":
					sonuc = "{} {}".format(isaret, sonuc.replace("  ", "").strip())
				return sonuc.replace("  ", "").strip()
			except Exception as e:
				return "Hata: {}".format(e)


BIRLER = {"1": "Bir", "2": "İki", "3": "Üç", "4": "Dört", "5": "Beş", "6": "Altı", "7": "Yedi", "8": "Sekiz", "9": "Dokuz", "0": " "}
ONLAR = {"1": "On", "2": "Yirmi", "3": "Otuz", "4": "Kırk", "5": "Elli", "6": "Altmış", "7": "Yetmiş", "8": "Seksen", "9": "Doksan", "0": " "}
YUZLER = {"1": "Yüz", "2": "İki Yüz", "3": "Üç Yüz", "4": "Dört Yüz", "5": "Beş Yüz", "6": "Altı Yüz", "7": "Yedi Yüz", "8": "Sekiz Yüz", "9": "Dokuz Yüz", "0": " "}
BINLER = {"1": "Bin", "2": "İki Bin", "3": "Üç Bin", "4": "Dört Bin", "5": "Beş Bin", "6": "Altı Bin", "7": "Yedi Bin", "8": "Sekiz Bin", "9": "Dokuz Bin", "0": " "}
