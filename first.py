import datetime
# a=True
# b=False
# print(f'{int(a)}{int(b)}{int(b)}')
# bir=datetime.datetime(2022, 10, 1, 23, 59, 59, 999999)
# ikki=datetime.datetime(2020, 11, 2, 22, 28, 28, 999999)
# time=(bir-ikki).total_seconds()
# print(time)
# new_sana=bir+datetime.timedelta(days=40)
# b=datetime.datetime.strftime(bir, '%Y, %d-%B')
# # a = datetime.datetime.strptime(2007, 2, 10, '%Y, %d-%B')
# print(b)

a=input('Kunni kiriting- ')
y=input('Yilni kiriting- ')
c=f'{a}-October, {y}'
dt=datetime.datetime.strptime(c,'%d-%B, %Y')
yangi_sana=dt+datetime.timedelta(days=20)
nwdt=datetime.datetime.strftime(yangi_sana, '%d-%B, %Y')
print(nwdt)