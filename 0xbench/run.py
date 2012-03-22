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
	#connect the device
	global device
	timeout_val = 5
	for dev_id in sys.argv[1:]:
	
		device = MonkeyRunner.waitForConnection(timeout = timeout_val, deviceId = dev_id)

		if not device:
			print "connect to the device timeout"
			sys.exit()
		else:
			print "connect to the device: " + dev_id
		
		package = "org.zeroxlab.zeroxbenchmark"
		comp = package + "/" + "Benchmark"
		device.startActivity(component = comp)
		MonkeyRunner.sleep(4)
		activity = ["org.zeroxlab.graphics.DrawCircle","org.zeroxlab.zeroxbenchmark.TesterGC",
		"org.zeroxlab.zeroxbenchmark.TesterArithmetic","org.zeroxlab.zeroxbenchmark.TesterJavascript",
		"org.zeroxlab.zeroxbenchmark.TesterScimark2","org.zeroxlab.zeroxbenchmark.Report",
		"org.zeroxlab.zeroxbenchmark.Upload","com.nea.nehe.lesson08.Run",
		"com.nea.nehe.lesson16.Run","org.itri.teapot.TeapotES",
		"org.opensolaris.hub.libmicro.NativeTesterMicro","org.zeroxlab.byteunix.NativeTesterUbench",
		"org.zeroxlab.graphics.DrawRect","org.zeroxlab.graphics.DrawArc",
		"org.zeroxlab.graphics.DrawText","org.zeroxlab.graphics.DrawCircle2",
		"org.zeroxlab.graphics.DrawImage"]

		for acti in activity:
			print "begin to process ", acti
			comp = package + "/" + acti
			device.startActivity(component=comp)
			MonkeyRunner.sleep(10)
			take_snapshot()
			

if __name__ == '__main__':
	main()


