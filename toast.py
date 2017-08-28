import sl4a
droid = sl4a.Android()
uname = droid.dialogGetInput("Enter your name") 
print (uname) 
droid.makeToast("Hello %s" %uname.result)