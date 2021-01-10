"""Parašykite generatoriaus funkciją, kuri atidarytų nurodytą failą, ir
grąžintų po vieną eilutę (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.).
Reikės prisiminti darbą su failais :)"""

def read_in_lines(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        line = 1
        while True:
            data = file.readlines(line)
            # Čia galima užsiimti text formatavimu, bet nebūtina.
            if not data:
                break
            yield data
            line += 1


generator = read_in_lines('os.py')