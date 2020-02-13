def lijst_sorteren():
    x=0
    y=0
    getallen_lijst = [3,2,3,4,6,7,7,5,6,7,8,9,0,9,8,2,3,4,5,8,3,5,4,1,0,4,5,6,8,2,3,4,1,0,0]
    gesorteerd=[]
    laagste=getallen_lijst[0]

    while len(getallen_lijst)>0:
        for x in range(0,len(getallen_lijst)):
            if getallen_lijst[x]<=laagste:
                laagste=getallen_lijst[x]
        gesorteerd.append(laagste)
        getallen_lijst.remove(laagste)
        if len(getallen_lijst)>1:
            laagste=getallen_lijst[0]
    print('De nieuwe gesorteerde lijst is: {}'.format(gesorteerd))


lijst_sorteren()

#Manually sort a list of 10 integers in python
#Geraadpleegd op 5-2-2020, van:
#https://stackoverflow.com/questions/21816084/manually-sort-a-list-of-10-integers-in-python