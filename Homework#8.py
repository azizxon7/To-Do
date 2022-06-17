import datetime as dt
import _thread as th
import time as t
sr=t.time()
now = dt.datetime.now()
time = now.strftime("%H:%M")
print(f"Hozirgi vaqt: {time}")
# Vazifa #2
# a
sana = now.strftime("%Y, %d-%B")
print(f"Sana: {sana}")
# b
sana = now.strftime("%d.%m.%Y")
print(f"Sana: {sana}")
# c
sana = now.strftime("%d-%B, %Y-yil")
print(f"Sana: {sana}")
# Vazifa #3
d =now.strptime('April 1, 2015 12:40',"%B %d, %Y %H:%M")
print(d)
# Vazifa #4
x =dt.datetime(2021, 5, 12)
print(x.strftime("%A"))
# Vazifa #5
a=('Assalomu alaykum', 'ZED IT Academyga xush kelibsiz', 'Bizni tanlaganingiz uchun tashakkur', 'Murojaat uchun +998 94 532 77 44')
for i in a:
    print(i)
    t.sleep(5)
# Vazifa #6
def san():
    a=100
    while a!=0:
        print(a)
        a-=1
def sana(a, b):
    for i in range(a, b):
        print(i)
for i in range(2):
    th.start_new_thread(san, ())
for i in range(2):
    th.start_new_thread(sana, (100, 1))
sp=t.time()
print(f"Sarflangan vaqt: {sp-sr}")