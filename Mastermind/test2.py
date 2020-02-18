import itertools
from collections import Counter

def evaluate(guess, secret):
    matches = sum((Counter(secret) & Counter(guess)).values())
    bullseye = sum(c == g for c, g in zip(secret, guess))
    return bullseye, matches - bullseye

def knuth(secret):
    """Run Knuth's 5-guess algorithm on the given secret."""
    all_codes = maak_alle_mogelijkheden()
    assert(secret in all_codes)
    codes = all_codes
    key = lambda g: max(Counter(evaluate(g, c) for c in codes).values())
    # key is de kleurencombinatie die het meest voorkomt
    # for g in codes:
    #   for c in codes:
    #       count_dict = Counter(evaluate(g, c))
    # max(count_dict.values())
    # Counter geeft een dict terug met telling bijv: {[rood, rood, rood, geel]: 100}
    # Counter doet count maken van elke code. Code is combinatie van kleuren
    guess = ('rood', 'rood', 'oranje', 'oranje')
    while True:
        feedback = evaluate(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            break
        codes = [c for c in codes if evaluate(guess, c) == feedback]
        # def evalueer codes:
        #   for c in codes:
        #         if evaluate(guess, c) == feedback
        #             codes.append(c)
        #  return codes
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(all_codes, key=key) # wat doet dit precies?


def maak_alle_mogelijkheden():
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    mogelijkheden_lijst = []
    for prod in itertools.product(kleuren_lijst, repeat=4):
        mogelijkheden_lijst.append(prod)
    return mogelijkheden_lijst

knuth(('rood', 'oranje', 'geel', 'groen'))