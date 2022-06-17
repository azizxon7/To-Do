a=input("Siz bizga 2 ta son kiritasiz (ularning 1-si davlatlar soni, 2-si nechanchi davlatning o'rin kerak ekanligi)\nKiriting - ")
b=a.split()
d=[]
kerak=''
orin=0
for i in range(int(b[0])):
    c=input('Kiriting - ')
    e=c.split()
    d.append(e)
    if int(e[0])==int(b[1]):
        kerak=e
        d.remove(kerak)
for i in range(int(b[0])-1):
    if int(kerak[1])>int(d[i][1]):
        orin+=1
    if int(kerak[1])==int(d[i][1]):
        n=int(kerak[2])+int(kerak[3])
        m=int(d[i][2])+int(d[i][3])
        if n>=m:
            orin+=1
        else:
            orin+=0
    if int(kerak[1])<int(d[i][1]):
        orin+=0
lol=0
while orin!=int(b[0]):
    b[0]=int(b[0])-1
    lol+=1
    if orin==int(b[0]):
        print(f'{kerak[1]} ta OLTIN, {kerak[2]} ta KUMUSh, {kerak[3]} ta BRONZA')
        print(f"{lol}-o'rin")