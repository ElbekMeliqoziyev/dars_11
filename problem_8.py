"""0 dan n gacha bo‘lgan sonlardan faqat tub sonlarni 
yield bilan qaytaradigan generator yarating. """

def tub(n):
    for i in range(n):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            yield i

for i in tub(15):
    print(i)