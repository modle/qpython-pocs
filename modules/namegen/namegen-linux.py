import random

path = 'assets/'

weapons_file_path = '{}weapons.txt'.format(path)
weapons_file = open (weapons_file_path, 'r')
weapons = weapons_file.read().split('\n')

suffixes_file_path = '{}suffixes.txt'.format(path)
suffixes_file = open (suffixes_file_path, 'r')
suffixes = suffixes_file.read().split('\n')

prefixes_file_path = '{}prefixes.txt'.format(path)
prefixes_file = open (prefixes_file_path, 'r')
prefixes = prefixes_file.read().split('\n')

for weapon in weapons:
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    print ("{} {} of {}"
    	 .format(prefix, weapon, suffix))
