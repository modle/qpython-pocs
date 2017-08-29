def loadfile(filename):
    root_path = '/storage/emulated/0/qpython/scripts3/modules/auto-rpg/assets/'
    file_path = '{}{}'.format(root_path, filename)
    loaded_file = open (file_path, 'r')
    return loaded_file.read().split('\n')
