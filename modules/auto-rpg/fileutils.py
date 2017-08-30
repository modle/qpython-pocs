#-*-coding:utf8;-*-
#qpy:3

import os

def loadfile(file_path):
    abs_path = os.path.dirname(os.path.abspath(__file__))
    file_path = '{}/{}'.format(abs_path, file_path)
    loaded_file = open (file_path, 'r')
    return loaded_file.read().split('\n')
