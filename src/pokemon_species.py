"""
POKETLAS
Retrieve Pokémon species from PokéAPI.
"""

import requests

API_URL = "https://pokeapi.co/api/v2/pokemon-species?limit=2000"


def get_species():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()["results"]


def main():
    species = get_species()

    print(f"Found {len(species)} Pokémon species.\n")

    print("First 10 Pokémon species:")
    for i, p in enumerate(species[:10], start=1):
        print(f"{i:>3}. {p['name']}")


if __name__ == "__main__":
    main()
