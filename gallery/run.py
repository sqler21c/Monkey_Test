import os
import sys
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

COUNT = 0
file_path = os.path.realpath(os.path.dirname(__file__))
module_name = os.path.basename(file_path)

def gen_png_no():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def take_snapshot(device):
    result = device.takeSnapshot()
    result.writeToFile('%s/%s_%s.png' % (file_path, module_name,
                                         gen_png_no()),
                       "png")
    MonkeyRunner.sleep(20)


def init(device):
    os.system("rm %s/*.png 2> /dev/null" % file_path)
    device.shell("am kill-all")


def main():
    if len(sys. argv) < 2:
        print "please input the device id"
        sys.exit(0)

    timeout_val = 5

    for dev_id in sys.argv[1:]:
        device = MonkeyRunner.waitForConnection(timeout=timeout_val,
                                                deviceId=dev_id)

        if not device:
            print "connect to the device timeout"
            sys.exit()
        else:
            print "connect to the device: " + dev_id

        #clean the enviroment
        init(device)

        # Wake up the screen and unlock
        device.shell("svc power stayon true;input keyevent 82")

        print "run %s..." % module_name
        package = "com.android.gallery3d"
        activity = ".app.Gallery"
        runComponent = package + '/' + activity
        device.startActivity(component=runComponent)
        MonkeyRunner.sleep(5)
        take_snapshot(device)
        device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)
        take_snapshot(device)


if __name__ == "__main__":
    main()
