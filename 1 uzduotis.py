"""Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next
grąžintų sekantį porinį skaičių. Pirmas sk. 2, toliau 4 ir taip be pabaigos."""
def poriniai():
    number = 2
    while True:
        yield number
        number += 2