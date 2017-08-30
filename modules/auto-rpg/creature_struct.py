#-*-coding:utf8;-*-
#qpy:3

import random
from fileutils import loadfile

creatures = loadfile('assets/creatures.txt')
prefixes = loadfile('assets/prefixes.txt')

def load_creature(level):
    creature = {}
    creature ['level'] = level
    creature ['name'] = '{} {}'.format(random.choice(prefixes), random.choice(creatures))
    creature ['hitpoints'] = 10 * level
    creature['damage'] = 2
    creature['defense'] = 1
    return creature
