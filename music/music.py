import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = MonkeyRunner.waitForConnection()

pkg = "com.android.music"
acti = "com.android.music.MusicBrowserActivity"
comp = pkg + "/" + acti
device.startActivity(component = comp)
device.press("KEYCODE_9",MonkeyDevice.DOWN)
device.press("KEYCODE_1",MonkeyDevice.DOWN)
device.press("KEYCODE_1",MonkeyDevice.DOWN)
device.press("KEYCODE_ENTER",MonkeyDevice.DOWN)
result = device.takeSnapshot()
result.writeToFile('shot.png','png')


