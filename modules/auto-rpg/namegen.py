#-*-coding:utf8;-*-
#qpy:3

import random
from fileutils import loadfile

weapons = loadfile('assets/weapons.txt')
prefixes = loadfile('assets/prefixes.txt')
suffixes = loadfile('assets/suffixes.txt')

for weapon in weapons:
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    print ("{} {} of {}"
    	 .format(prefix, weapon, suffix))
