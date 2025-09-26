"""0 dan n gacha bo‘lgan sonlardan faqat tub sonlarni 
yield bilan qaytaradigan generator yarating. """

def tub(n):
    c=0
    for i in range(n):
        if i%i==0 and i%1==0:
            c+=1