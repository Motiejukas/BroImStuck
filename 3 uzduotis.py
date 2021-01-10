"""Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių,
kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas.
Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. Pabaigus funkciją, praiteruokite sukurtą
generatorių su for ciklu, kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, parašytų 'PIN is XXXX(jųsų pin'as)'.
Atkreipkite dėmesį, kad kodas gali prasidėti nuliu. Sugalvokite, kaip apeiti šią problemą (hint - type conversion, if sąlygos)."""

#Tarkime, kad teisingas pin yra 0123
PIN = '0123'

def pin_breaker():
    guess = 0
    while True:
        yield guess
        if guess == int(PIN):
            if len(str(guess)) < 4:
                if len(str(guess)) == 3:
                    print(f'PIN is 0{guess}!')
                elif len(str(guess)) == 2:
                    print(f'PIN is 00{guess}!')
                else:
                    print(f'PIN is 000{guess}!')
            else:
                print(f'PIN is {guess}!')
            break
        guess += 1


generator = pin_breaker()
for num in generator:
    #Čia irgi galime įterpti logiką, kad spausdintų nulius prieky
    print(num)