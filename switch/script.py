import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def main():
	
	count = 1
	while 1:
		print "run browser..."
		device = MonkeyRunner.waitForConnection()
		package = "com.android.browser"
		activity = ".BrowserActivity"
		runComponent = package + '/' + activity
		device.startActivity(component=runComponent)
		time.sleep(1)
		result = device.takeSnapshot()
		result.writeToFile('shot.png','png')
			
		print "run 3D..."
		package = "org.linaro.glmark2"
		activity = "org.linaro.glmark2.Glmark2Activity"
		runComponent = package + "/" + activity
		device.startActivity(component = runComponent)
		time.sleep(1)
		result = device.takeSnapshot()
		result.writeToFile('shot.png','png')

if __name__ == "__main__":
	main()
