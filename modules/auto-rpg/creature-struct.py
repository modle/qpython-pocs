#-*-coding:utf8;-*-
#qpy:3

import random
from fileutils import loadfile

creatures = loadfile('creatures.txt')

def loadCreature(level):
    creature = {}
    creature ['level'] = level
    creature ['name'] = random.choice(creatures)
    creature ['hitpoints'] = 10 * level
    return creature
    
print (loadCreature(1))