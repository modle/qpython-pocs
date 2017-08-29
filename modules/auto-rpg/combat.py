#-*-coding:utf8;-*-
#qpy:3

from creature_struct import loadCreature
from player_struct import loadPlayer
import time

player = loadPlayer()
creature = loadCreature(player['level'])
attack_string = '{} attacks {} for {} point(s) of damage!'

while(1):
    # player attacks
    print (attack_string.format('player', 'creature', 1))
    time.sleep(1)
    # creature attacks
    print (attack_string.format('creature', 'player', 1))
    time.sleep(1)
