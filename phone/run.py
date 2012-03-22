import sys 
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

def browse(d):   
    	d.startActivity(uri='http://www.baidu.com',component="com.android.browser/.BrowserActivity")
    	MonkeyRunner.sleep(5.0)
    	d.press('KEYCODE_BUTTON_SELECT', MonkeyDevice.DOWN_AND_UP) 

   
def call(d):
	
    	d.startActivity(component="com.android.contacts/.TwelveKeyDialer")
    	print "Start Activity"
    	MonkeyRunner.sleep(10.0)
    	d.type("911")
	take_snapshot(d)
       
    	# Call number.
	print "Call"
    	d.touch(190, 800, 'DOWN_AND_UP');
	take_snapshot(d)
    
    	print "Wait 5 sec"
    	MonkeyRunner.sleep(5.0)
       
    	d.press('KEYCODE_CALL', MonkeyDevice.DOWN_AND_UP)
   
    	d.startActivity(component="com.android.phone/.InCallScreen")
   
    	MonkeyRunner.sleep(1.0)
    
    	print "Wait 5 sec"
    	MonkeyRunner.sleep(5.0)
	take_snapshot(d)
   
    	# HangUp Call
    	print "Hang Up"
    	d.press('KEYCODE_ENDCALL', MonkeyDevice.DOWN_AND_UP)
	take_snapshot(d)

def endcall(d):
    	d.touch(140, 760, 'DOWN_AND_UP')
	MonkeyRunner.sleep(3)
	take_snapshot(d)
   	
    	print "dialing..."
    	d.type('911')
    	MonkeyRunner.sleep(3)
    	d.touch(240, 740, 'DOWN_AND_UP')
    	MonkeyRunner.sleep(3)
	take_snapshot(d)
   
    	print "hanging up..."
    	d.touch(240, 600, 'DOWN_AND_UP')
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
   
    
    		call(device)
    		endcall(device)
    		browse(device)


if __name__ == '__main__':
	main()


    
