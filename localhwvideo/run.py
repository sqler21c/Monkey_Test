import os,sys,time
from subprocess import call
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


COUNT = 0;

def gen_png_no():
	global COUNT
	COUNT = COUNT + 1
	return str(COUNT)

def take_snapshot(device):
	result = device.takeSnapshot()
	result.writeToFile(os.path.realpath(os.path.dirname(__file__))+"/localhwvideo_" + gen_png_no() +".png","png")

def init():
	os.system("rm" + os.path.realpath(os.path.dirname(__file__)) + "/*.png 2> /dev/null")

def main():

	if len(sys.argv) < 2:
		print "please input the device id"
		sys.exit(0)

	#connect the device
	timeout_val = 5
	for dev_id in sys.argv[1:]:
		device = MonkeyRunner.waitForConnection( timeout = timeout_val,deviceId = dev_id )

		if not device:
			print "connect to the device timeout"
			sys.exit(0)
		else:
			print "connect to the device: " + dev_id

		srcfile = os.path.realpath(os.path.dirname(__file__))+'/big_buck_bunny_1080p_H264_AAC_25fps_7200K_short.MP4'
		device.shell("mkdir /data/local/tests/")
		call(["adb", "-s", dev_id, "push", srcfile, "/data/local/tests/"])

		#clean the enviroment
		init()

                device.startActivity(uri='file:////data/local/tests/big_buck_bunny_1080p_H264_AAC_25fps_7200K_short.MP4',component='com.android.gallery3d/.app.MovieActivity')

		MonkeyRunner.sleep(2)
		take_snapshot(device)

		print "wiat for 10 sec..."
		MonkeyRunner.sleep(10)

		device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)
		take_snapshot(device)
		device.shell("rm -r /data/local/tests/")


if __name__ == '__main__':
	main()
