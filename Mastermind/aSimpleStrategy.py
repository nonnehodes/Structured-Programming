import itertools
from collections import Counter


def evalueer_guess(gok, secret):
    # Zie voetnoot
    correct = 0
    gevonden = sum((Counter(secret) & Counter(gok)).values())
    for c, g in zip(gok, secret):
        if c == g:
            correct += 1
    return correct, gevonden - correct


def maak_alle_mogelijkheden():
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
    if ronde == 1:
        print('AI voert in: {}'.format(ai_opties_lijst[0]))
        return ai_opties_lijst[0], ai_opties_lijst
    else:
        nieuwe_pogingen = []
        for optie in ai_opties_lijst:
            feedback = evalueer_guess(optie, ai_gok)
            mogelijkheden_dict[optie] = feedback
        # print('Aantal opties voor AI: {}'.format(len(mogelijkheden_dict.items())))
        for k, v in mogelijkheden_dict.items():
            if v == tip:
                nieuwe_pogingen.append(k)
        print('AI voert in: {}'.format(nieuwe_pogingen[0]))
        return nieuwe_pogingen[0], nieuwe_pogingen


def play_game():
    secret_key = input_secret_key()
    print('secret key is: {}'.format(secret_key))
    aantal_guesses = 1
    ai_mogelijkheden = maak_alle_mogelijkheden()
    print('\n Ronde {}'.format(aantal_guesses))
    gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=None, tip=None, ai_opties_lijst=ai_mogelijkheden,
                                              ronde=aantal_guesses)

    if gok == secret_key:
        print('AI heeft gewonnen! Game over!')
    else:
        play = True
        while play:
            tips = evalueer_guess(gok, secret_key)
            print('feedback: {}'.format(tips))
            aantal_guesses += 1
            print('\n Ronde {}'.format(aantal_guesses))
            if aantal_guesses <= 9:
                gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=gok, tip=tips, ai_opties_lijst=ai_mogelijkheden,
                                                          ronde=aantal_guesses)
                if gok == secret_key:
                    print('Game over! AI heeft gewonnen!')
                    play = False
            else:
                print('Meer dan 10 gokken, AI heeft verloren')
                break



# https://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
# https://www.programiz.com/python-programming/methods/built-in/min
