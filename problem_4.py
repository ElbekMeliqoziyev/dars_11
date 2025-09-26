""" register_user(**kwargs) funksiyasini yozing. 
Agar email yoki username yo‘q bo‘lsa, ValueError chiqarsin. Aks holda, ma’lumotlarni dict sifatida qaytarsin."""

def register_user(**kwargs):
    if "username" not in kwargs or "email" not in kwargs:
        raise ValueError
    else:
        print(kwargs)



register_user(username="Ali", email="ali@gmail.com")