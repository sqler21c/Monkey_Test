import os
import sys
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

COUNT = 0
file_path = os.path.realpath(os.path.dirname(__file__))


def gen_png_no():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def take_snapshot(device):
    result = device.takeSnapshot()
    result.writeToFile('%s/angrybird_%s.png' % (file_path, gen_png_no()),
                       "png")


def init():
    os.system("rm %s/*.png 2> /dev/null" % file_path)


def main():

    if len(sys.argv) < 2:
        print "please input the device id"
        sys.exit(0)

    #connect the device
    timeout_val = 5
    for dev_id in sys.argv[1:]:
        device = MonkeyRunner.waitForConnection(timeout=timeout_val,
                                                deviceId=dev_id)

        if not device:
            print "connect to the device timeout"
            sys.exit(0)
        else:
            print "connect to the device: " + dev_id

        #clean the enviroment
        init()

        #install the angrybird.apk
        print "install angrybird.apk"
        device.installPackage("%s/AngryBirds_1.3.2_rio.apk" % file_path)

        #start the angrybird rio
        pkg = "com.rovio.angrybirdsrio"
        acti = "com.rovio.ka3d.App"
        device.startActivity(component='%s/%s' % (pkg, acti))

        print "wait 10 sec..."
        MonkeyRunner.sleep(10)
        take_snapshot(device)

        #play the angrybird app
        #print "touch"
        #device.touch(500,500,'DOWN_AND_UP')

        #close the app
        print "close"
        device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
        take_snapshot(device)

        MonkeyRunner.sleep(2)
        device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)
        take_snapshot(device)


if __name__ == '__main__':
    main()
