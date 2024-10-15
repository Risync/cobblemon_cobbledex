import webbrowser
import keyboard
from system.lib import minescript as mc
import time

def open_pokedex():
    pokemon_nbt = mc.player_get_targeted_entity(nbt=True)
    
    if pokemon_nbt == None:
        mc.echo('Not Looking At Pokemon')

    else:
        pokemon = pokemon_nbt.name.lower()
        cobblemon_pokedex = "https://pokemondb.net/pokedex/"
        search = cobblemon_pokedex + pokemon
        webbrowser.open_new_tab(search)

def main():
    while True:
        if keyboard.is_pressed('left ctrl'):
            open_pokedex()
        time.sleep(0.1)

if __name__ == "__main__":
    main()

