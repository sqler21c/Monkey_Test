'''
Created on 2015. 10. 15.
Monkey Test script
@author: User
'''

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

    
package = 'com.skt.prod.dialer'
activity = 'com.skt.prod.dialer.activities.main.MainActivity'
strDvicName='866b652b'
strTimeOtt =100

runComponent = package + "/" + activity

'''device = MonkeyRunner.waitForConnection(strTimeOtt, strDvicName)
'''
device=MonkeyDevice
device.startActivity(component=runComponent)
device.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)
result=device.takeSnapshot()
result.writeToFile('myproject/shot1.png','png')


