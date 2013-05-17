import os
import sys
from subprocess import call
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

COUNT = 0


def gen_png_no():
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)


def take_snapshot(device):
    result = device.takeSnapshot()
    result.writeToFile('%s/localaudio_%s.png' % (
                                os.path.realpath(os.path.dirname(__file__)),
                                gen_png_no()), "png")


def init():
    os.system("rm %s/*.png 2> /dev/null" % (
                    os.path.realpath(os.path.dirname(__file__))))


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

        file_dir = os.path.realpath(os.path.dirname(__file__))
        srcfile = file_dir + '/big_buck_bunny_AAC_2Channel_44.1k_128K.AAC'
        device.shell("mkdir /data/local/tests/")
        call(["adb", "-s", dev_id, "push", srcfile, "/data/local/tests/"])

        #clean the enviroment
        init()

        # Wake up the screen and unlock
        device.shell("svc power stayon true;input keyevent 82")

        uri = ('file:////data/local/tests/'
               'big_buck_bunny_AAC_2Channel_44.1k_128K.AAC')
        component = 'com.android.music/.MediaPlaybackActivity'
        device.startActivity(uri=uri, component=component)

        take_snapshot(device)

        print "playing 30 sec..."
        MonkeyRunner.sleep(30)

        device.press("KEYCODE_DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.press("KEYCODE_DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.press("KEYCODE_DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.press("KEYCODE_DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.press("KEYCODE_DPAD_LEFT", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.press("KEYCODE_DPAD_CENTER", MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1)
        device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
        take_snapshot(device)

        MonkeyRunner.sleep(2)
        device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)
        take_snapshot(device)

        device.shell("rm -r /data/local/tests/")


if __name__ == '__main__':
    main()
