import random
from collections import Counter

kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']


def gok():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    guess = [k1, k2, k3, k4]
    print(guess)
    return guess


def generate_secrete_key():
    secret_key = []
    for kleur in range(4):
        kleur = random.choice(kleuren_lijst)
        secret_key.append(kleur)
    # print('antwoord: {}'.format(secret_key))
    return secret_key


def evalueer_guess(gok, secret):
    # Zie voetnoot
    correct = 0
    gevonden = sum((Counter(secret) & Counter(gok)).values())
    for c, g in zip(gok, secret):
        if c == g:
            correct += 1
    return correct, gevonden - correct


def mastermind_pc_code():
    secret_key = generate_secrete_key()
    print(secret_key)
    guess = gok()
    if guess == secret_key:
        print('Gefeliciteerd je bent een mastermind!')
    else:
        aantal_guesses = 0
        while guess != secret_key:
            aantal_guesses += 1
            tips = evalueer_guess(guess, secret_key)
            if guess == secret_key:
                print('Gefeliciteerd je bent een mastermind!')
                break

            print(tips)
            print('Je hebt {} van de 10 pogingen gebruikt'.format(aantal_guesses))

            if aantal_guesses <= 9:
                guess = gok()
            else:
                print('Game over!')
                print('De correcte code was:{}'.format(secret_key))
                break
        if guess == secret_key:
            print('Gefeliciteerd je bent een mastermind!')

# https://stackoverflow.com/questions/20298190/mastermind-minimax-algorithm
# https://www.programiz.com/python-programming/methods/built-in/min