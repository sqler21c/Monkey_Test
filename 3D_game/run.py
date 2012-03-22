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
			sys.exit()
		else:
			print "connect to the device: " + dev_id

		#clean the enviroment
		init()

		#install 3D Game apk
		print "install diversion.apk"
		device.installPackage("diversion.apk")

		pkg = "com.ezone.Diversion"
		acti = "com.unity3d.player.VideoPlayer"
		device.startActivity(component = pkg+"/"+acti)

		print "wait 10 sec..."
		MonkeyRunner.sleep(10)
		take_snapshot()

		#play the angrybird app
		print "touch"
		device.touch(500,500,'DOWN_AND_UP')



if __name__ == '__main__':
	main()
