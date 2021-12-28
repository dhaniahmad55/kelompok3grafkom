import numpy as np 
import matplotlib.pyplot as plt

#Inisialisasikan titik kordinat (x1,y1) dan kordinat (x2,y2)
x1 = int(input("Masukan nilai x1  : "))
y1 = int(input("Masukan nilai y1  : "))
x2 = int(input("Masukan nilai x2  : "))
y2 = int(input("Masukan nilai y2  : "))
print('===========================================================')

#N adalah banyaknya iterasi yang dilakukan apabila x1 != x2 atau y1 != y2
nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

# titik awalnya adalah x dan y
x = x1
y = y1

i = 1


if x1 == x2:
    titikA = []
    titikB = []
    while i < y2:
        if y1 == y2:
            print('Garis yang di lewati yaitu', x,',', y )
            titikA.append(x)
            titikB.append(y)
        else:
            print('titik-titik pembentuk garis', x,',', y+i )
            titikA.append(x)
            titikB.append(y+i)
        i+=1
    plt.plot(titikA,titikB)
    plt.show()
elif y1 == y2:
    titikA = []
    titikB = []
    while i < y2:
        if x1 == x2:
            print('titik-titik pembentuk garis', x,',', y )
            titikA.append(x)
            titikB.append(y)
        else:
            print('titik-titik pembentuk garis', x+i,',', y )
            titikA.append(x+i)
            titikB.append(y)
        i+=1
    plt.plot(titikA,titikB)
    plt.show()
else:
    titikA = []
    titikB = []
    while i <= N:
        m = nilaiY / nilaiX
        rumusY = m * (x - x1) + y1
        kordinatY = round(rumusY)
        x+=1
        print('titik-titik pembentuk garis', x-1,',', kordinatY)
        titikA.append(x-1)
        titikB.append(kordinatY)
        i+=1

    plt.plot(titikA,titikB)
    plt.show()
#grafkom
