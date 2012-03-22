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
	global device
	timeout_val = 5
		
	for dev_id in sys.argv[1:]:
		device = MonkeyRunner.waitForConnection( timeout = timeout_val,deviceId = dev_id )
		
		#install app
		print "install app"
		device.installPackage("../angrybird/AngryBirds_1.3.2_rio.apk")
		device.installPackage("../3D_game/diversion.apk")
		device.installPackage("../navigation/googlemap.apk")
	
 		if not device:
			print "connect to the device timeout"
			sys.exit()
		else:
			print "connect to the device: " + dev_id

		#clean the enviroment
		init()
	
		while 1:
			print "run browser..."
			package = "com.android.browser"
			activity = ".BrowserActivity"
			runComponent = package + '/' + activity
			device.startActivity(component=runComponent)
			time.sleep(2)
			take_snapshot()		
			device.press("KEYCODE_HOME",MonkeyDevice.DOWN_AND_UP)
	
			print "run googlemap..."
			pkg = "com.google.android.apps.maps"
			acti = "com.google.android.maps.MapsActivity"
			device.startActivity(component = pkg+"/"+acti)
			time.sleep(2)
			take_snapshot()		
			device.press("KEYCODE_HOME",MonkeyDevice.DOWN_AND_UP)

			print "run 3D game..."
			package = "com.ezone.Diversion"
			activity = "com.unity3d.player.VideoPlayer"
			runComponent = package + "/" + activity
			device.startActivity(component = runComponent)
			time.sleep(2)
			take_snapshot()
			device.press("KEYCODE_HOME",MonkeyDevice.DOWN_AND_UP)
			
			print "run angrybird..."
			package = "com.rovio.angrybirdsrio"
			activity = "com.rovio.ka3d.App"
			runComponent = package + "/" + activity
			device.startActivity(component = runComponent)
			time.sleep(2)
			take_snapshot()
			device.press("KEYCODE_HOME",MonkeyDevice.DOWN_AND_UP)



if __name__ == "__main__":
	main()




