import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


COUNT = 0;

def gen_png_no():
	global COUNT
	COUNT = COUNT + 1
	return str(COUNT)

def take_snapshot():
	global device
	result = device.takeSnapshot()
	result.writeToFile("shot_" + gen_png_no() +".png","png")

def init():
	os.system("rm *.png 2> /dev/null")

def main():
	if len(sys.argv) < 2:
		print "please input the device id"
		sys.exit(0)
	#connect the device
	global device 
	timeout_val = 5
	for dev_id in sys.argv[1:]:
		device = MonkeyRunner.waitForConnection( timeout = timeout_val,deviceId = dev_id )
	
 		if not device:
			print "connect to the device timeout"
			sys.exit(0)
		else:
			print "connect to the device: " + dev_id

		#clean the enviroment
		init()
		
		#install the googlemap apk
		print "install the google apk"
		device.installPackage("googlemap.apk")

		#start the navigation app
		print "start navigation"
		pkg = "com.google.android.apps.maps"
		acti = "com.google.android.maps.driveabout.app.NavigationActivity"
		device.startActivity(component = pkg + "/" + acti)

		print "wait 5 sec..."
		MonkeyRunner.sleep(5)
		take_snapshot()	
		device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)	
	
		print "start search where to eat"
		acti = "com.google.android.maps.PlacesActivity"
		device.startActivity(component = pkg + "/" + acti)
		#search and navigation
		device.type("where to eat")
		take_snapshot()


if __name__ == '__main__':
	main()


