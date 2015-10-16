'''
Created on 2015. 10. 16.

@author: User
'''
import time

from com.android.monkeyrunner import MonkeyDevice, MonkeyRunner, MonkeyImage
 
device= MonkeyDevice
for i in range(5):
    device = MonkeyRunner.waitForConnection(8)
    if device != None:
        print "Device found..."
        break;
 
device.press("KEYCODE_NOTIFICATION", "DOWN_AND_UP")
time.sleep(1)
device.press("KEYCODE_BACK", "DOWN_AND_UP")