import random

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
    print('antwoord: {}'.format(secret_key))
    return secret_key


def mastermind_pc_code():
    secret_key = generate_secrete_key()
    guess = gok()
    if guess == secret_key:
        print('Gefeliciteerd je bent een mastermind!')
    else:
        aantal_guesses = 0
        while guess != secret_key:
            tips = []
            aantal_guesses += 1
            for i in range(0, 4):
                if (guess[i] == secret_key[i]):
                    tips.append('wit')
                    print('Gefeliciteerd je bent een mastermind!')
                elif (guess[i] in secret_key):
                    tips.append('zwart')


            print(tips)
            print('Je hebt {} van de 10 pogingen gebruikt'.format(aantal_guesses))

            if aantal_guesses <= 9:
                guess = gok()
            else:
                print('game over')
                break


mastermind_pc_code()