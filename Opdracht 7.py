import random
def gokken():
    for x in range(1):
        random_getal = random.randint(1,11)
        while True:
            gok = input('Gok een getal: ')
            if random_getal == int(gok):
                print('Gefeliciteerd je hebt het geraden!')
                break
            else:
                print('Probeer het nog een keer.')

gokken()