import json


with open('50.json', 'r', encoding='utf-8') as file:
    filmer = json.load(file)


def film_med_hoyest_karakter(filmer):
    max_karakter = 0
    film_med_hoyest_karakter = ''
    for film in filmer:
        if film['karakter'] > max_karakter:
            max_karakter = film['karakter']
            film_med_hoyest_karakter = film['navn']
    return film_med_hoyest_karakter, max_karakter


def gjennomsnittskarakter_alle(filmer):
    total_karakter = sum(film['karakter'] for film in filmer)
    return total_karakter / len(filmer)


def gjennomsnittskarakter_ti_første(filmer):
    total_karakter = sum(film['karakter'] for film in filmer[:10])
    return total_karakter / 10


def flest_filmer_av_en_regissør(filmer):
    regissør_teller = {}
    for film in filmer:
        for regissør in film['regissører']:
            regissør_teller[regissør] = regissør_teller.get(regissør, 0) + 1
    max_filmer = max(regissør_teller.values())
    flest_regissører = [regissør for regissør, filmer in regissør_teller.items() if filmer == max_filmer]
    return flest_regissører, max_filmer


def totalt_antall_regissører(filmer):
    regissør_liste = [regissør for film in filmer for regissør in film['regissører']]
    return len(set(regissør_liste))


film, karakter = film_med_hoyest_karakter(filmer)
print(f"Filmen med høyest karakter er '{film}' med en karakter på {karakter}.")

gjennomsnitt_alle = gjennomsnittskarakter_alle(filmer)
print(f"Gjennomsnittskarakteren til alle filmene er {gjennomsnitt_alle:.2f}.")

gjennomsnitt_ti_første = gjennomsnittskarakter_ti_første(filmer)
print(f"Gjennomsnittskarakteren til de ti første filmene er {gjennomsnitt_ti_første:.2f}.")

regissør, antall_filmer = flest_filmer_av_en_regissør(filmer)
print(f"Regissøren(e) som har regissert flest filmer er {', '.join(regissør)} med {antall_filmer} filmer.")

total_regissører = totalt_antall_regissører(filmer)
print(f"Totalt antall regissører på listen er {total_regissører}.")
