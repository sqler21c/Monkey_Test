import os
import sys
from com.android.monkeyrunner import MonkeyRunner

COUNT = 0
file_path = os.path.realpath(os.path.dirname(__file__))


def gen_png_no():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def take_snapshot(device):
    result = device.takeSnapshot()
    result.writeToFile('%s/3D_Game_%s.png' % (file_path, gen_png_no()), "png")


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
            sys.exit()
        else:
            print "connect to the device: " + dev_id

        #clean the enviroment
        init()

        # Wake up the screen and unlock
        device.shell("svc power stayon true;input keyevent 82")

        #install 3D Game apk
        print "install diversion.apk"
        device.installPackage("%s/diversion.apk" % file_path)

        pkg = "com.ezone.Diversion"
        acti = "com.unity3d.player.UnityPlayerActivity"
        device.startActivity(component='%s/%s' % (pkg, acti))

        print "wait 10 sec..."
        MonkeyRunner.sleep(10)
        take_snapshot(device)

        #play the app
        print "touch"
        device.touch(500, 500, 'DOWN_AND_UP')
        take_snapshot(device)


if __name__ == '__main__':
    main()
