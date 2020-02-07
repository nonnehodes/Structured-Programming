getallen_lijst = range(101)
def fizzBuzz(lijst):
    for getal in lijst:
        if getal % 3 == 0 and getal % 5 == 0:
            print("fizzbuzz")
            continue
        elif getal % 3 == 0:
            print("fizz")
            continue
        elif getal % 5 == 0:
            print("buzz")
            continue
        print(getal)
fizzBuzz(getallen_lijst)
