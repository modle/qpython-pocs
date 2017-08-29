import os
import sys

print (os.name)
print (sys.platform)

path = os.path.dirname(os.path.abspath(__file__))
print (path)