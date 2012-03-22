import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = MonkeyRunner.waitForConnection()
#droid = android.Android()
#3pkg = droid.getRunningPackages()
#pprint.pprint(pkg.result)
pkg = "com.rovio.angrybirdsseasons"
acti = "com.rovio.ka3d.App"
device.startActivity(component = pkg+"/"+acti)


