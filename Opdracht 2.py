#de code werkt nog niet met zinnen, alleen woorden.
#Probeer input:
    #hoihoihai
    #hoihoihoi
        #dan geeft hij index 8 terug
#Probeer input:
    #hallo wereld
    #hallo wereld! ik ben naam
        #dan geeft hij een foutmelding

regel1 = input('Geef een string: ')
regel2 = input('Geef een string: ')
indexFout = 0
def tekstCheck(r1, r2, index):
    if len(r1) < len(r2):
        for item in r2:
            if item != r1[index]:
                print('Het eerste verschil zit op index: {}'.format(str(index +1)))
                break
            else:
                index += 1

    elif len(r1) >= len(r2):
        for item in r1:
            if item != r2[index]:
                print('het eerste verschil zit op index: {}'.format(str(index +1)))
                break
            else:
                index += 1





tekstCheck(regel1, regel2, indexFout)