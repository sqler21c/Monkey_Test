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
    result.writeToFile("%s/audio_%s.png" % (file_path, gen_png_no()), "png")


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

        # Wake up the screen and unlock
        device.shell("svc power stayon true;input keyevent 82")

        uri = ('http://samplemedia.linaro.org/Audio/'
               'big_buck_bunny_AAC_2Channel_44.1k_128K.AAC')
        device.startActivity(uri=uri,
                             component="com.android.browser/.BrowserActivity")

        print "wait 10 sec..."
        MonkeyRunner.sleep(10)
        take_snapshot(device)

        device.press('KEYCODE_BUTTON_SELECT', MonkeyDevice.DOWN_AND_UP)
        print "playing 30 sec..."
        MonkeyRunner.sleep(30)

        device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP)
        take_snapshot(device)

        MonkeyRunner.sleep(2)
        device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)
        take_snapshot(device)


if __name__ == '__main__':
    main()
