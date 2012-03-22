import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def main():
	device = MonkeyRunner.waitForConnection()
	package = "com.android.quicksearchbox"
	acti = ".SearchActivity"
	comp = package + "/" + acti
	device.startActivity(component = comp)
	time.sleep(2)
	result=device.takeSnapshot()
	result.writeToFile("shot1.png","png")
	
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_W)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_H)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_E)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_R)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_E)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_T)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_O)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_E)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_A)
	device.press("KEYCODE_MENU",MonkeyDevice.KEYCODE_T)

	result = device.takeSnapshot()
	result.writeToFile("shot2.png","png")
	


if __name__ == '__main__':
	main()
