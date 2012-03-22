import sys,os 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

COUNT = 0;

def gen_png_no():
	global COUNT
	COUNT = COUNT + 1
	return str(COUNT)

def take_snapshot(d):
	result = d.takeSnapshot()
	result.writeToFile("shot_" + gen_png_no() +".png","png")

def init():
	os.system("rm *.png 2> /dev/null")

def call_video(d):   
    	d.startActivity(uri='http://samplemedia.linaro.org/H264/big_buck_bunny_480p_H264_AAC_25fps_1800K.MP4',component="com.android.browser/.BrowserActivity")
    	MonkeyRunner.sleep(5.0)
    	d.press('KEYCODE_BUTTON_SELECT', MonkeyDevice.DOWN_AND_UP)
	take_snapshot(d) 
   

def main():
	
	timeout_val = 5	
	if len(sys.argv) < 2:
		print "please input the device id"
		sys.exit(0)
	
    	print "Start"
	init()

	for dev_id in sys.argv[1:]:
		device = MonkeyRunner.waitForConnection( timeout = timeout_val,deviceId = dev_id )
        
    		if not device:
        		print "Couldn't get connection"
		        sys.exit(0)
		else:
			print "connect to the device: " + dev_id
   
    
    		call_video(device)


if __name__ == '__main__':
	main()


    
