import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = MonkeyRunner.waitForConnection()
package = "org.zeroxlab.zeroxbenchmark"
activity = "org.zeroxlab.graphics.DrawArc"
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
time.sleep(5)
result = device.takeSnapshot()
result.writeToFile('shot.png','png')
