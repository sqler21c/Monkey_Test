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
    result.writeToFile('%s/navigation_%s.png' % (file_path, gen_png_no()),
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

        #install the googlemap apk
        print "install the google apk"
        device.installPackage("%s/googlemap.apk" % file_path)

        #start the navigation app
        print "start navigation"
        pkg = "com.google.android.apps.maps"
        acti = "com.google.android.maps.driveabout.app.NavigationActivity"
        device.startActivity(component='%s/%s' % (pkg, acti))

        print "wait 5 sec..."
        MonkeyRunner.sleep(5)
        take_snapshot(device)
        device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)

        print "start search where to eat"
        acti = "com.google.android.maps.PlacesActivity"
        device.startActivity(component='%s/%s' % (pkg, acti))
        #search and navigation
        device.type("where to eat")
        take_snapshot(device)


if __name__ == '__main__':
    main()
