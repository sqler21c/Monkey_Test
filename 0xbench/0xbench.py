import os,sys,time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def main():
	print "begin to run 0xbench"
	device = MonkeyRunner.waitForConnection()
	package = "org.zeroxlab.zeroxbenchmark"
	comp = package + "/" + "Benchmark"
	device.startActivity(component = comp)
	time.sleep(4)
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
		time.sleep(5)
		result=device.takeSnapshot()
		result.writeToFile(acti+".png","png")


if __name__ == '__main__':
	main()
