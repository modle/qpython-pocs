import sl4a
import time
droid = sl4a.Android()
title = 'Spinner'
message = 'This is simple spinner progress.'
droid.dialogCreateSpinnerProgress(title, message)
droid.dialogShow()
time.sleep(2)
droid.dialogDismiss()