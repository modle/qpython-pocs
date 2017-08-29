#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import sl4a
droid = sl4a.Android()
print("This is console module")
result = droid.notify('This is a notify test', 'You been notified!')
