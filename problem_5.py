"""Dekorator yozing, u funksiyani chaqirgan vaqtni 
datetime yordamida ekranga chiqarsin."""
from datetime import datetime

def check(func):
    def wrap():
        func()
    return wrap

@check
def vaqt():
    print(datetime.now())

vaqt()