#-*-coding:utf8;-*-
#qpy:3

from creature_struct import loadCreature
from player_struct import loadPlayer
import time

def get_creature(seed):
    creature = loadCreature(seed)
    print('{} has spawned'.format(creature['name']))
    return creature

player = loadPlayer()
creature = get_creature(player['level'])
attack_string = '{} attacks {} for {} point(s) of damage!'

while(1):
    # player attacks
    print (attack_string.format('player', creature['name'], player['damage']))
    creature['hitpoints'] = creature['hitpoints'] - player['damage']
    if creature ['hitpoints'] <= 0:
        print ('{} defeated'.format(creature['name']))
        creature = get_creature(player['level'])
    time.sleep(1)
