
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

#from com.android.monkeyrunner import MonkeyRunner as mr
#from com.android.monkrerunner import MonkeyDevice as md
#from com.android.monkeyrunner import MonkeyImage as mi

class MonkeyWrapImpl():
    def waitForConnection(self):
        self.device = MonkeyRunner.waitForConnection()
    def startActivity(self,runComponent):
        self.device.startActivity(component=runComponent)
        
    def touch_down(self,x,y):
        self.device.touch(x,y,MonkeyDevice.DOWN)
    def touch_up(self,x,y):
        self.device.touch(x,y,MonkeyDevice.UP)
    def touch_down_and_up(self,x,y):
        self.device.touch(x,y,MonkeyDevice.DOWN_AND_UP)
        
    def press_menu_down_and_up(self):
        self.device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    def press_power_down_and_up(self):
        self.device.press('KEYCODE_POWER', MonkeyDevice.DOWN_AND_UP)
        
    def drag(self,sx,sy,ex,ey,duration,steps):
        self.device.drag((sx,sy),(ex,ey),duration,steps);
    def sleep(self,sec):
        MonkeyRunner.sleep(sec);
    def takeAndSaveSnapshot(self,savaPath,type):
        img = self.device.takeSnapshot()
        img.writeToFile(savaPath,type)
    def screenWidth(self):
#        w = self.device.getProperty('width')
#        print('width=' + w)
#        return w;
        return 720; 
    def screenHeight(self):
#        h = self.device.getProperty('height')
#        return h;
        return 1280;
    def __init__(self):
        '''
        Constructor
        '''
        
def log(msg):
    print(msg)
    
# com.coohuaclient com.coohuaclient.ui.activity.SplashActivity

# main core

monkey = MonkeyWrapImpl()

monkey.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
# device.installPackage('myproject/bin/MyApplication.apk')

# sets a variable with the package's internal name
package = 'com.coohuaclient'

# sets a variable with the name of an Activity in the package
#activity = 'com.coohuaclient.ui.activity.SplashActivity'
activity = 'com.coohuaclient.ui.activity.LockScreenOneViewActivity'
# sets the name of the component to start
runComponent = package + '/' + activity

#runComponent = 'io.dcloud.HBuilder' + '/' + 'com.example.runtime_sdk_test.ActivityEntry'
# Runs the component
monkey.startActivity(runComponent)

monkey.sleep(0.5);
sx = monkey.screenWidth() / 2
sy = monkey.screenHeight() * 9 / 10
while(True):
    monkey.sleep(1);
    monkey.press_power_down_and_up()
    monkey.sleep(0.3);
    toLeft = True;
    if (toLeft):
        ex = monkey.screenWidth() / 8
    else:
        ex = monkey.screenWidth() / 8 * 7
        
    ey = sy;
    duration = 1; 
    steps = 3;
    tuple = (sx, sy, ex, ey, duration, steps)
    log(tuple);
    monkey.drag(sx, sy, ex, ey, duration, steps)


#monkey.touch_down_and_up(180,120)
# Presses the Menu button
# device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

#monkey.takeAndSaveSnapshot(dir,'png')