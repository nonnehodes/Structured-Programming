def mastermind_PC_code(): #Hier moet de speler de code van de comuter raden

    import random
    kleuren_lijst = ['Rood', 'Oranje', 'Geel', 'Groen', 'Blauw', 'Paars']
    secret_key = []
    for kleur in range(4): #Hier word een random code gegenereerd
        kleur = random.choice(kleuren_lijst)
        secret_key.append(kleur)
    print(secret_key)

    guess = []
    for j in range(4): #hier word de eerste guess gegenereerd
        k1 = print(input('Geef je 1e kleur: '))
        k2 = print(input('Geef je 2e kleur: '))
        k3 = print(input('Geef je 3e kleur: '))
        k4 = print(input('Geef je 4e kleur: '))

    print(guess)

def check_key(guess, secret_key):
    zwart = 0
    wit = 0
    for i in range(4):
        if guess[i] in secret_key: #hier word gekeken of er dingen overeenkomen tussen de code en de guess ÉN word er een nieuwe guess gegenereerd tot max 10
            if guess[i] == secret_key[i]:
                zwart += 1
            else:
                wit += 1


mastermind_PC_code()
