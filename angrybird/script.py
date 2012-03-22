import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def main():
	device = MonkeyRunner.waitForConnection()
	
	pkg = "com.rovio.angrybirdsseasons"
	acti = "com.rovio.ka3d.App"
	device.startActivity(component = pkg+"/"+acti)
	result=device.takeSnapshot()
	result.writeToFile("shot.png","png")
	


if __name__ == '__main__':
	main()
