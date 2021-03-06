from speluitleg import speluitleg
from aSimpleStrategy import play_game
from aWorstCaseStrategy import minimax
from aHomemadeStrategy import homemade_strategie
from MastermindPCcode import mastermind_pc_code
from aWorstCaseStrategy import input_secret_key


def spel_menu(speluitleg):
    print('\n''Welkom bij mastermind!')
    keuze1 = input('Kies een gamemode ([A]Gamemaster/[B]Gameplayer/[C]Speluitleg): ')
    if keuze1 == 'A' or keuze1 == 'a':
        keuze2 = input('Kies een strategie ([A]A simple strategy/[B]A worst case strategy/[C]A homemade strategy): ')
        if keuze2 == 'A' or keuze2 == 'a':
            play_game()
        elif keuze2 == 'B' or keuze2 == 'b':
            minimax(input_secret_key())
        elif keuze2 == 'C' or keuze2 == 'c':
            homemade_strategie()
        else:
            print('Maak keuze uit een van de opties, A, B of C')
            spel_menu(speluitleg)
    elif keuze1 == 'B' or keuze1 == 'b':
        mastermind_pc_code()
    elif keuze1 == 'C' or keuze1 == 'c':
        print(speluitleg)
        return spel_menu(speluitleg)
    elif keuze1 not in 'AaBbCc':
        print('Maak gebruik van de opties A, B of C')
        spel_menu(speluitleg)


spel_menu(speluitleg)
