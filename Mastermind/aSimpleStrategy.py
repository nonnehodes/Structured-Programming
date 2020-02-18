import itertools


def maak_alle_mogelijkheden(): #dit maakt ALLE permutaties
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    mogelijkheden_lijst = []
    for prod in itertools.product(kleuren_lijst, repeat=4):
        mogelijkheden_lijst.append(prod)
    return mogelijkheden_lijst

def input_secret_key():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    secret_key = (k1, k2, k3, k4)
    return secret_key


def ai_mastermind_gok(ai_gok, tip, ai_opties_lijst, ronde):
    mogelijkheden_dict = {}
    if ronde == 0:
        print('AI voert in: {}'.format(ai_opties_lijst[0]))
        return ai_opties_lijst[0], ai_opties_lijst
    else:
        nieuwe_pogingen = []
        for optie in ai_opties_lijst:
            hints = []
            for i in range(0, 4):
                if (optie[i] == ai_gok[i]):
                    hints.append('wit')
                elif (optie[i] in ai_gok[i]):
                    hints.append('zwart')

            if hints.count('wit') == 3:
                hints = ['wit', 'wit', 'wit']

            mogelijkheden_dict[optie] = hints
        print(len(mogelijkheden_dict.items()))
        for k, v in mogelijkheden_dict.items():
            if v == tip:
                nieuwe_pogingen.append(k)
        print('AI voert in: {}'.format(nieuwe_pogingen[0]))
        return nieuwe_pogingen[0], nieuwe_pogingen


def play_game():
    secret_key = input_secret_key()
    print('secret key is: {}'.format(secret_key))
    aantal_guesses = 0
    ai_mogelijkheden = maak_alle_mogelijkheden()
    gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=None, tip=None, ai_opties_lijst=ai_mogelijkheden, ronde=aantal_guesses)

    if gok == secret_key:
        print('Game over! AI heeft gewonnen.')
    else:
        play = True
        while play:
            tips = []
            aantal_guesses += 1
            for i in range(0, 4):
                if (gok[i] == secret_key[i]):
                    tips.append('wit')
                elif (gok[i] in secret_key[i]):
                    tips.append('zwart')

            if tips.count('wit') == 3:
                tips = ['wit', 'wit', 'wit']

            if aantal_guesses <= 10:
                print('ronde {}'.format(aantal_guesses))
                gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=gok, tip=tips, ai_opties_lijst=ai_mogelijkheden, ronde=aantal_guesses)
                if gok == secret_key:
                    print('Game over! AI heeft gewonnen!')
                    play = False
            else:
                print('Meer dan 10 gokken, AI heeft verloren')
                break



play_game()

