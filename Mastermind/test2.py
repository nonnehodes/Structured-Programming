def mogelijkheden_lijst_maken():
    import itertools
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    mogelijkheden_lijst = []
    for prod in itertools.product(kleuren_lijst, repeat=4):
        mogelijkheden_lijst.append(prod)
    print(mogelijkheden_lijst)

def speler_code():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    secret_key = [k1, k2, k3, k4]
    print(secret_key)
    return secret_key

def gok():
    mogelijkheden_lijst = mogelijkheden_lijst_maken()
    eerste_gok = mogelijkheden_lijst[1]
    secret_key = speler_code()
    if eerste_gok == secret_key:
        print('Game over!')
    else:
        aantal_guesses = 0
        while eerste_gok != secret_key:
            tips = []
            aantal_guesses += 1
            for i in range(0, 4):
                if (eerste_gok[i] == secret_key[i]):
                    tips.append('wit')
                elif (eerste_gok[i] in secret_key):
                    tips.append('zwart')