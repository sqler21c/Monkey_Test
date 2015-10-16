'''
Created on 2015. 10. 15.
Monkey Test script
@author: User
'''

import java
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection(300, 'dksldkfksl')

   
    
package = 'com.skt.prod.dialer'
activity = 'com.skt.prod.dialer.activities.main.MainActivity'

runComponent = package + "/" + activity
device.startActivity(component=runComponent)
device.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)
result=device.takeSnapshot()
result.writeToFile('myproject/shot1.png','png')


