import sl4a
import time
droid = sl4a.Android()


title = "Progress" 
str = "Loading..."
droid.dialogCreateHorizontalProgress(title,str,100) 
droid.showDialog() 
	
for x in range(0,99):
    time.sleep(0.1) 
    droid.dialogSetCurrentProgress(x) 

droid.dialogDismiss()