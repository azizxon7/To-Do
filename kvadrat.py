a=input("Siz bizga 2 ta son kiritasiz (ularning 1-si nechta qator bo'lishi, 2-si nechta son bo'lishi)\nSonlarni Kiriting - ")
b=a.split()
d=[]
bd=[]

m=1
for i in range(int(b[0])):
    c=input('Kiriting - ')
    for i in c:
        d.append(i)
    bd.append(d)
    d=[]
print(bd)
 
for j in range(int(b[0])):
    n=1
    for i in range(1, int(b[1])):
        if bd[j][0]==bd[j][i] and bd[n][i]==bd[j][i] and bd[n][0]==bd[j][i]:
            m+=1
            if m==2:
                print('JAVOB:', (n+1)**2)
                print(n, m, j, i)
                break
        else:
            n+=1