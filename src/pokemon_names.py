"""
POKETLAS
Retrieve official Pokémon data from PokéAPI.
"""

import requests


POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=2000"


def get_pokemon_list():
    """Return a list of all Pokémon."""
    response = requests.get(POKEAPI_URL, timeout=30)
    response.raise_for_status()
    return response.json()["results"]


def main():
    pokemon = get_pokemon_list()

    print(f"Found {len(pokemon)} Pokémon.")

    print("\nFirst 10 Pokémon:")
    for p in pokemon[:10]:
        print("-", p["name"])


if __name__ == "__main__":
    main()
