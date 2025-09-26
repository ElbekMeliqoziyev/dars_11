"""	
Sutudentlar ro’yhati berilgan :
students = [{"name": "Ali", "grade": 85}, {"name": "Vali", "grade": 45}, …. ]
Sizni vazifangiz filter va map yordamida bahosi 60 dan yuqori bo‘lganlarni ajrating va ularning ismlarini katta harflarga olib o’ting. Natijani ekranga chirarib beradigan funksiya yozing. 
"""


students = [{"name": "Ali", "grade": 85}, {"name": "Vali", "grade": 45},]

w= map(lambda x: x['name'], filter(lambda x:  x["grade"]>60, [i for i in students]))

print(list(w))