"""Foydalanuvchidan parol uzunligini oling (int sifatida, agar qiymat bermasa 8 ta olsin) va quyidagi funksiyani yozing:
	def generate_password(length):
		pass
Parolda raqam, harf va maxsus belgilardan iborat  bo‘lsin"""

from random import randint, choices, shuffle, random
from string import punctuation, ascii_letters, octdigits, digits

def generate_password(length: int=8):
    a = punctuation
    b = ascii_letters
    
    c = digits
    c=c+b+a
    v = choices(c  , k=length)
    shuffle(v)
    v="".join(v)

    # while not v.isdigit and not v.isalpha and not [i for i in punctuation if i in v]:
    #     v = choices(c, k= length)
    #     shuffle(v)
    #     v = "".join(v) 
    #     if v.isdigit and v.isalpha and  [i for i in punctuation if i in v]:
    #         print(v)
        
    print(v)

generate_password(8)
