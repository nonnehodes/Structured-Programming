#de code werkt nog niet met zinnen, alleen woorden.
#Probeer input:
    #hoihoihai
    #hoihoihoi
        #dan geeft hij index 8 terug
#Probeer input:
    #hallo wereld
    #hallo wereld! ik ben naam
        #dan geeft hij index 13 terug
#probeer input
    #hallow
    #hallo
        #dan geeft hij een foutmelding


regel1 = input('Geef een string: ')
regel2 = input('Geef een string: ')
indexFout = 0
def tekstCheck(r1, r2, index):
    if len(r1) > len(r2):
        longest = r1
        shortest = r2
    else:
        longest = r2
        shortest = r1
    for x in range(0, len(longest)-1):
        if x > len(shortest)-1:
            x +=1
            return print(f'verschil is index {x}')
        if shortest[x] != longest[x]:
            x+=1
            return print(f'verschil is index {x}')

    if len(r1) < len(r2):
            for item in r2:
                if item != r1[index]:
                    print('Het eerste verschil zit op index: {}'.format(str(index +1)))
                else:
                    index += 1


    elif len(r1) >= len(r2):
        for item in r1:
            if item != r2[index]:
                print('het eerste verschil zit op index: {}'.format(str(index +1)))

            else:
                index += 1


tekstCheck(regel1, regel2, indexFout)

#code gemaakt met de hulp van guy
#guy heeft zijn code zelf gemaakt en mij er vervolgens mee geholpen