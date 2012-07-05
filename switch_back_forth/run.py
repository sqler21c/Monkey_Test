import os
import sys
import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

COUNT = 0
file_path = os.path.realpath(os.path.dirname(__file__))


def gen_png_no():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def take_snapshot(device):
    result = device.takeSnapshot()
    result.writeToFile('%s/switch_back_forth_%s.png' % (file_path,
                                                        gen_png_no()),
                                                        "png")


def init():
    os.system("rm %s/*.png 2> /dev/null" % file_path)


def main():
    if len(sys.argv) < 2:
        print "please input the device id"
        sys.exit(0)

    timeout_val = 5

    for dev_id in sys.argv[1:]:
        device = MonkeyRunner.waitForConnection(timeout=timeout_val,
                                                deviceId=dev_id)

        #install app
        print "install apps"
        device.installPackage("%s/../angrybird/AngryBirds_1.3.2_rio.apk" % (
                                                                    file_path))
        device.installPackage("%s/../3D_game/diversion.apk" % file_path)
        device.installPackage("%s/../navigation/googlemap.apk" % file_path)

        if not device:
            print "connect to the device timeout"
            sys.exit()
        else:
            print "connect to the device: " + dev_id

        #clean the enviroment
        init()

        for i in range(500):
            print "start %i/500 times test" % (i + 1)

            print "run browser..."
            package = "com.android.browser"
            activity = ".BrowserActivity"
            runComponent = package + '/' + activity
            device.startActivity(component=runComponent)
            time.sleep(2)
            take_snapshot(device)
            device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)

            print "run googlemap..."
            pkg = "com.google.android.apps.maps"
            acti = "com.google.android.maps.MapsActivity"
            device.startActivity(component='%s/%s' % (pkg, acti))
            time.sleep(2)
            take_snapshot(device)
            device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)

            print "run 3D game..."
            package = "com.ezone.Diversion"
            activity = "com.unity3d.player.VideoPlayer"
            runComponent = package + "/" + activity
            device.startActivity(component=runComponent)
            time.sleep(2)
            take_snapshot(device)
            device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)

            print "run angrybird..."
            package = "com.rovio.angrybirdsrio"
            activity = "com.rovio.ka3d.App"
            runComponent = package + "/" + activity
            device.startActivity(component=runComponent)
            time.sleep(2)
            take_snapshot(device)
            device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)


if __name__ == "__main__":
    main()
