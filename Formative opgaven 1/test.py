regel1 = input('Geef een string: ')
regel2 = input('Geef een string: ')

def verschil(r1, r2):
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

verschil(regel1, regel2)