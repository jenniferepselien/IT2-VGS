import json

with open('pokemon.json', 'r', encoding='utf-8') as file:
    pokemon_data = json.load(file)

print(pokemon_data)

class Pokemon:
    def __init__(self, id, name, types, base_stats):
        self._id = id
        self._name = name
        self._types = types
        self._base_stats = base_stats

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_types(self):
        return self._types

    def get_base_stats(self):
        return self._base_stats

    def __str__(self):
        return f"{self._name} - HP: {self._base_stats['HP']}"

class Trener:
    def __init__(self, navn):
        self._navn = navn
        self._pokemonliste = []

    def legg_til_pokemon(self, pokemon):
        self._pokemonliste.append(pokemon)

    def fjern_pokemon(self, pokemon):
        self._pokemonliste.remove(pokemon)

    def get_navn(self):
        return self._navn

    def get_antall_pokemon(self):
        return len(self._pokemonliste)

    def __str__(self):
        return f"{self._navn} - Antall Pokémon: {self.get_antall_pokemon()}"

def vis_pokemon_oversikt():
    print("Pokemonoversikt:")
    for pokemon in pokemon_liste:
        print(f"- {pokemon.get_name()} - Typer: {', '.join(pokemon.get_types())}")

def legg_til_trener():
    navn = input("Skriv inn navnet på treneren: ")
    ny_trener = Trener(navn)
    trenere.append(ny_trener)
    print(f"Treneren '{navn}' ble lagt til.")

def vis_trener_oversikt():
    print("Treneroversikt:")
    for trener in trenere:
        print(f"- {trener}")

with open('pokemon.json', 'r', encoding='utf-8') as file:
    pokemon_data = json.load(file)

pokemon_liste = []

bulbasaur = Pokemon(pokemon_data['id'], pokemon_data['name']['english'], pokemon_data['type'], pokemon_data['base'])
charmander = Pokemon(pokemon_data['id'], pokemon_data['name']['english'], pokemon_data['type'], pokemon_data['base'])

trenere = []

while True:
    print("\nVelg en handling:")
    print("1. Se pokemonoversikt")
    print("2. Se treneroversikt")
    print("3. Legg til trener")
    print("4. Avslutt")

    valg = input("Skriv inn valget ditt: ")

    if valg == "1":
        vis_pokemon_oversikt()
    elif valg == "2":
        vis_trener_oversikt()
    elif valg == "3":
        legg_til_trener()
    elif valg == "4":
        print("Avslutter programmet.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")


