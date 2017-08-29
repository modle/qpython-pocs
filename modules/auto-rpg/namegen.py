import random
from fileutils import loadfile

weapons = loadfile('weapons.txt')
prefixes = loadfile('prefixes.txt')
suffixes = loadfile('suffixes.txt')

for weapon in weapons:
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    print ("{} {} of {}"
    	 .format(prefix, weapon, suffix))
