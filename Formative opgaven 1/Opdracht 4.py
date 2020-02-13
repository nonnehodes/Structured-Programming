
def palindroom_check():
    string = input('Geef een woord of string: ')
    palindroom = string[::-1]
    if palindroom == string:
        print('Ja, het woord "{}" is een palindroom.'.format(string))
    else:
        print('Nee, het woord "{}" is geen palindroom.'.format(string))


def palindroom_check_2():
    woord = input('Geef een woord of string: ')
    palindroom = ''
    for i in woord:
        palindroom = i + palindroom

    if palindroom == str(woord):
        print('Ja, het woord "{}" is een palindroom.'.format(woord))
    else:
        print('Nee, het woord "{}" is geen palindroom.'.format(woord))

palindroom_check_2()
    #How to Reverse a String in Python
#Geraadpleegd op 5-2-2020, van:
#https://www.w3schools.com/python/python_howto_reverse_string.asp


