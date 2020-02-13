def mastermind_PC_code(): #Hier moet de speler de code van de comuter raden

    import random
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    secret_key = []
    for kleur in range(4): #Hier word een random code gegenereerd
        kleur = random.choice(kleuren_lijst)
        secret_key.append(kleur)
    print(secret_key)

    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    guess = [k1, k2, k3, k4]
    print(guess)

    if guess == secret_key:
        print('gefeliciteerd je bent een mastermind!')
    else:
        aantal_guesses = 0
        while guess != secret_key:
            aantal_guesses +=1
            zwart = 0
            wit = 0
            for i in range (0, 4):
                if guess[i] in secret_key: #hier word gekeken of er dingen overeenkomen tussen de code en de guess ÉN word er een nieuwe guess gegenereerd tot max 10
                    if guess[i] == secret_key[i]:
                        zwart += 1
                    else:
                        wit += 1

mastermind_PC_code()