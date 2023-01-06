1256983%28
Out[1]: 7

12**52/15 < 8 or 3**5 > 100
Out[2]: True

not (3**3*5 == 900/75)
Out[3]: True

'[[' + 'Python' + ']]'
Out[4]: '[[Python]]'

'Python'[-2:] * 4
Out[5]: 'onononon'

'Perl'[2:3:1] * 6
Out[6]: 'rrrrrr'

'python'[:6:6] * 6
Out[7]: 'pppppp'

'suffering'[:8:8] * 8
Out[8]: 'ssssssss'

print(7+3*2)
13

print('7' + str(3*2))
76

print('7' + '3*2')
73*2

print('7' + 3*2)
Traceback (most recent call last):

  File "C:\Users\tverd\AppData\Local\Temp\ipykernel_33024\1460442380.py", line 1, in <module>
    print('7' + 3*2)

TypeError: can only concatenate str (not "int") to str


print(7 + 3*2)
13

print('7' + '3*2')
73*2

#možeme spojiť iba str+str alebo int+int

x = 'crying'
f'My hobby is {x}!'
Out[16]: 'My hobby is crying!'

list = []

list = []
hobby = ['crying', 'reading', 'sleeping', 'working_the_whole_free_time']
list.extend(hobby)

print(list)
['crying', 'reading', 'sleeping', 'working_the_whole_free_time']

print(list[0])
crying

print(list[-1])
working_the_whole_free_time

del(list)

cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
print(cities)
['Brno', 'Ceske Budejovice', 'Hradec Kralove', 'Liberec', 'Olomouc', 'Ostrava', 'Pardubice', 'Plzen', 'Prague', 'Usti nad Labem']

#moj mozog zomrel na triedeni miest podla poctu obyvatelej aj na set()

"*".join(cities)
Out[25]: 'Brno*Ceske Budejovice*Hradec Kralove*Liberec*Olomouc*Ostrava*Pardubice*Plzen*Prague*Usti nad Labem'


