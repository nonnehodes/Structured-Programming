eerste_string = "hoe laat is het nu echt? Of niet"
tweede_string = "hoe laat is het nu echt?"
if len(eerste_string) >= len(tweede_string):
    for idx, letter in enumerate(eerste_string):
        if idx+1 <= len(tweede_string):
            if letter == tweede_string[idx]:
                print('letter: {}, index: {}'.format(letter, idx))
            else:
                print('{} niet meer in string, op index: {}'.format(letter, idx))