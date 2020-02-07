getallen_lijst = (1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,3)
getallen_lijst_2 = ((2,2,2),(3,3),(4,4,4),(5,5))
def gemiddelde_berekenen(lijst):
    optellen = 0
    for i in lijst:
        optellen += i
    print(optellen/len(lijst))

def gemiddelde_berekenen_lijstVanLijsten(lijsten):
    optellen_lijst = 0
    optellen_lijsten = 0
    for lijst in lijsten:
        for i in lijst:
            optellen_lijst += i
            gemiddelde_lijst = optellen_lijst/len(lijst)
            optellen_lijst = 0
            optellen_lijsten += gemiddelde_lijst
    print(optellen_lijsten/len(lijsten))

gemiddelde_berekenen_lijstVanLijsten(getallen_lijst_2)