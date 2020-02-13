
import random
kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
secret_key = []
for kleur in range(4):
    kleur = random.choice(kleuren_lijst)
    secret_key.append(kleur)
print(secret_key)


def gok():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')
    guess = [k1, k2, k3, k4]
    print(guess)
gok()



def mastermind_pc_code(secret_key):
    if(gok() == secret_key()):
        print('Gefeliciteerd je bent een mastermind!')
    else:
        while(gok() != secret_key):
            aantal_guesses = 0
            guess = str(guess)
            secret_key = str(secret_key)

            for i in range(0,4):
                if(guess[i] == secret_key[i]):
                    aantal_guesses += 1
                else:
                    continue


            if aantal_guesses <= 10:
                gok()
            else:
                print('game over')


mastermind_pc_code(secret_key)