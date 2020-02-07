getallen_lijst = [1,1,4,3,5,2,6,8,9,7,5,4,3,4,6,7,8,1,2,3,6,5,4,6,8,9,3,4,5,6,1,0,3,0,0,8]
lengte_getallen_lijst = len(getallen_lijst)

#deel a

def count(lijst):
    getal = int(input('Geef een getal x(0 t/m 9): '))
    gevonden = []
    for index, suspect in enumerate(lijst):
        if getal == suspect:
            gevonden.append(index)
    print('Het getal {} komt {} keer voor in de lijst.'.format(getal, len(gevonden)))

count(getallen_lijst)
# Check the occurrences in a list against a value
# Geraadpleegd op 5-2-2020, van:
# https://stackoverflow.com/questions/4446380/python-check-the-occurrences-in-a-list-against-a-value/4446385

#deel b

def grootste_verschil(lijst, lengte_lijst):
    grootste_verschil = lijst[1] - lijst[0]

    for i in range(0, lengte_lijst):
        for j in range(i+1, lengte_lijst):
            if(lijst[j] - lijst[i] > grootste_verschil):
                grootste_verschil = lijst[j] - lijst[i]

    print("Het grootste verschil tussen twee op een volgende getallen is: {}".format(grootste_verschil))

grootste_verschil(getallen_lijst, lengte_getallen_lijst)

#Ik heb hulp gehad van Guy en van een Kerel die goed is in programmeren, naast dat ook deze bron:
#Maximum difference between two elements such that larger element appears after the smaller number
#geraadpleegd op 7-2-2020
#https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

#deel c









