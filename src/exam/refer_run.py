import os
 import sys  3 from com.android.monkeyrunner import MonkeyRunner
   4 
   5 COUNT = 0
   6 
   7 file_path = os.path.realpath(os.path.dirname(__file__))
   8 
   9 
  10 def gen_png_no():
  11     global COUNT
  12     COUNT = COUNT + 1
  13     return str(COUNT)
  14 
  15 
  16 def take_snapshot(device):
  17     result = device.takeSnapshot()
  18     result.writeToFile('%s/0xbench_%s.png' % (file_path, gen_png_no()), "png")
  19 
  20 
  21 def init():
  22     os.system("rm %s/*.png 2> /dev/null" % file_path)
  23 
  24 
  25 def main():
  26     #connect the device
  27     timeout_val = 5
  28     for dev_id in sys.argv[1:]:
  29 
  30         device = MonkeyRunner.waitForConnection(timeout=timeout_val,
  31                                                 deviceId=dev_id)
  32 
  33         if not device:
  34             print "connect to the device timeout"
  35             sys.exit()
  36         else:
  37             print "connect to the device: " + dev_id
  38 
  39         # Wake up the screen and unlock
  40         device.shell("svc power stayon true;input keyevent 82")
  41  
  42         package = "org.zeroxlab.zeroxbenchmark"
  43         comp = package + "/" + "Benchmark"
  44         device.startActivity(component=comp)
  45         MonkeyRunner.sleep(4)
  46         activity = ["org.zeroxlab.graphics.DrawCircle",
  47                     "org.zeroxlab.zeroxbenchmark.TesterGC",
  48                     "org.zeroxlab.zeroxbenchmark.TesterArithmetic",
  49                     "org.zeroxlab.zeroxbenchmark.TesterJavascript",
  50                     "org.zeroxlab.zeroxbenchmark.TesterScimark2",
  51 #                    "org.zeroxlab.zeroxbenchmark.Report",
  52 #                    "org.zeroxlab.zeroxbenchmark.Upload",
  53                     "com.nea.nehe.lesson08.Run",
  54                     "com.nea.nehe.lesson16.Run",
  55                     "org.itri.teapot.TeapotES",
  56                     "org.opensolaris.hub.libmicro.NativeTesterMicro",
  57                     "org.zeroxlab.byteunix.NativeTesterUbench",
  58                     "org.zeroxlab.graphics.DrawRect",
  59                     "org.zeroxlab.graphics.DrawArc",
  60                     "org.zeroxlab.graphics.DrawText",
  61                     "org.zeroxlab.graphics.DrawCircle2",
  62                     "org.zeroxlab.graphics.DrawImage"]
  63 
  64         for acti in activity:
  65             print "begin to process ", acti
  66             comp = package + "/" + acti
  67             device.startActivity(component=comp)
  68             MonkeyRunner.sleep(10)
  69             take_snapshot(device)
  70 
  71 
  72 if __name__ == '__main__':
  73     main()