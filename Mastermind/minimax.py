import itertools
from collections import Counter

def input_secret_key():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    secret_key = (k1, k2, k3, k4)
    return secret_key

def maak_alle_mogelijkheden():
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    mogelijkheden_lijst = []
    for prod in itertools.product(kleuren_lijst, repeat=4):
        mogelijkheden_lijst.append(prod)
    return mogelijkheden_lijst

def evalueer_guess(gok, secret):
    # Zie voetnoot
    correct = 0
    gevonden = sum((Counter(secret) & Counter(gok)).values())
    for c, g in zip(gok, secret):
        if c == g:
            correct += 1
    return correct, gevonden - correct


def minimax(secret):
    all_codes = maak_alle_mogelijkheden()
    assert (secret in all_codes)
    codes = all_codes
    key_functie = lambda g: max(Counter(evalueer_guess(g, c) for c in codes).values()) # Zie voetnoot
    guess = ('rood', 'rood', 'oranje', 'oranje')
    ronde = 1
    while True:
        print('Speelronde: {}'.format(ronde))
        ronde += 1
        feedback = evalueer_guess(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            print('AI heeft gewonnen! Game Over!')
            break
        codes = [c for c in codes if evalueer_guess(guess, c) == feedback]
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(all_codes, key=key_functie)



# https://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
# https://www.programiz.com/python-programming/methods/built-in/min
