#ZONDER WHILE
#ZONDER WHILE
#ZONDER WHILE
#ZONDER WHILE
def pyramide():
    getal = int(input('Hoe groot?: '))
    for ster in range(0, getal):
        for sterretjes in range(0, ster+1):
            print('* ',end='')
        print()

    for sterretje in range(0, getal):
        for sterretjes_deel2 in range(getal-1, sterretje, -1):
            print('* ',end='')
        print()


def reversepyramide():
    getal = int(input('Hoe groot?: '))
    for ster in range(0, getal):
        for sterretjes in range(getal, ster, -1):
            print('* ',end='')
        print()

    for ster in range(1, getal):
        for sterretjes_deel2 in range(0, ster+1):
            print('* ',end='')
        print()

#MET WHILE
#MET WHILE
#MET WHILE
#MET WHILE
def pyramide_met_while():
    getal = int(input('Hoe groot?: '))
    i = 0
    while i < getal:
        i+=1
        print(i*'*')

    while i > 0:
        i-=1
        print(i*'*')



def reversepyramide_met_while():
    getal = int(input('Hoe groot?: '))
    x = getal
    i=1

    while getal > 0:
        print(getal*'*')
        getal -=1

    while i < x:
        i+=1
        print(i*'*')

reversepyramide_met_while()





#Python Program to Print Star Pyramid Patterns,
#Geraadpleegd op 4-2-2020, van:
#https://codescracker.com/python/program/python-program-print-star-pyramid-patterns.htm

