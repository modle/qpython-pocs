#-*-coding:utf8;-*-
#qpy:3

from creature_struct import load_creature
from player_struct import load_player
import time

def get_creature(seed):
    creature = load_creature(seed)
    print('{} has spawned'.format(creature['name']))
    return creature

player = load_player()
creature = get_creature(player['level'])
attack_string = '{} attacks {} for {} point(s) of damage!'

def calculate_player_damage():
    return player['damage'] - creature['defense']

def print_player_attack_round(damage):
    print (attack_string.format(player['name'], creature['name'], damage))

def update_creature_hitpoints(damage):
    creature['hitpoints'] = creature['hitpoints'] - damage

def print_creature_defeated():
    print ('{} has been defeated'.format(creature['name']))

def wait_a_second():
    time.sleep(1)

def recover_player_health():
    player['hitpoints'] = player['maxhitpoints']

def spawn_new_creature():
    return get_creature(player['level'])

def reset_battlefield():
    global creature
    print_creature_defeated()
    wait_a_second()
    recover_player_health()
    creature = spawn_new_creature()
    wait_a_second()

def calculate_creature_damage():
    return creature['damage'] - player['defense']

def print_creature_attack_round(damage):
    print (attack_string.format(creature['name'], player['name'], damage))

def update_player_hitpoints(damage):
    player['hitpoints'] = player['hitpoints'] - damage

def start_combat():
    while(1):
        player_damage = calculate_player_damage()
        print_player_attack_round(player_damage)
        update_creature_hitpoints(player_damage)
        if creature['hitpoints'] <= 0:
            reset_battlefield()
            continue
        wait_a_second()
        creature_damage = calculate_creature_damage()
        print_creature_attack_round(creature_damage)
        update_player_hitpoints(creature_damage)
        wait_a_second()

start_combat()
