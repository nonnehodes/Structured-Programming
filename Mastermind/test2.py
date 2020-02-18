import itertools
from collections import Counter


def input_secret_key():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    secret_key = (k1, k2, k3, k4)
    return secret_key

def evaluate(guess, secret):
    matches = sum((Counter(secret) & Counter(guess)).values())
    bullseye = sum(c == g for c, g in zip(secret, guess))
    return bullseye, matches - bullseye

def key(codes):
    for g in codes:
        for c in codes:
            count_dict = Counter(evaluate(g, c))
    max(count_dict.values())
# Counter geeft een dict terug met telling bijv: {[rood, rood, rood, geel]: 100}
# Counter doet count maken van elke code. Code is combinatie van kleuren

def evalueer_codes(codes, guess, feedback):
    for c in codes:
        if evaluate(guess, c) == feedback:
            codes.append(c)
    return codes

def knuth(secret, key):
    """Run Knuth's 5-guess algorithm on the given secret."""
    all_codes = maak_alle_mogelijkheden()
    assert(secret in all_codes)
    codes = all_codes
    key_codes = key(codes)

    guess = ('rood', 'rood', 'oranje', 'geel')
    while True:
        feedback = evaluate(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            break
        codes = evalueer_codes(codes)
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(all_codes, key_codes=key_codes) # wat doet dit precies?


def maak_alle_mogelijkheden():
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    mogelijkheden_lijst = []
    for prod in itertools.product(kleuren_lijst, repeat=4):
        mogelijkheden_lijst.append(prod)
    return mogelijkheden_lijst

knuth((input_secret_key()), key)

#----------------------------------------------------------------------------------------------------------------------#

