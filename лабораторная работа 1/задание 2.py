diskette = (1.44*1024)*1024 # объём дискеты в байтах

pages = 100
str_ = 50
symbol = 25
massa = 4 #вес одного символа

book = pages*str_*symbol*massa #объём книги в байтах
total= int(diskette//book)

print("Количество книг, помещающихся на дискету:", total)

