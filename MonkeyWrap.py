
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
# from com.android.hierarchyviewerlib.device import ViewNode

#from com.android.monkeyrunner import MonkeyRunner as mr
#from com.android.monkrerunner import MonkeyDevice as md
#from com.android.monkeyrunner import MonkeyImage as mi

class MonkeyWrapImpl():
    def waitForConnection(self):
        self.device = MonkeyRunner.waitForConnection()
        self.initEasyDevice()
    def startActivity(self,runComponent):
        self.device.startActivity(component=runComponent)
        
    def initEasyDevice(self):
        self.easyDevice = EasyMonkeyDevice(self.device);
    def touchByViewId(self,viewId):
        self.easyDevice.touch(By.id(viewId),MonkeyDevice.DOWN_AND_UP)
    def visible(self,viewId):
        self.easyDevice.visible(By.id(viewId))
            
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
    def wakeup(self):
        self.device.wake()
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
class MonkeyViewNode():
    
    def __init__(self):
        '''
        Constructor
        '''
        
def getAbsInt(strValue,relValue):
    return int(float(strValue[0:len(strValue)-1]) * relValue / 100)

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
    monkey.press_power_down_and_up()
    monkey.sleep(0.3);
    toLeft = True;
    if (toLeft):
        ex = monkey.screenWidth() / 8
        log('will drag to left')
    else:
        ex = monkey.screenWidth() / 8 * 7
        log('will drag to right')
    ey = sy;
    duration = 1; 
    steps = 1;
    tuple = (sx, sy, ex, ey, duration, steps)
    log(tuple);
    monkey.wakeup()
    monkey.sleep(2);
    monkey.drag(sx, sy, ex, ey, duration, steps)
    isDownload = True;
    isShare = False;
    if(isDownload):
        log('download request')
        monkey.sleep(2);
        downViewId = 'id/btn_webview_download'
        btnLeft= monkey.screenWidth() / 3
        btnTop= monkey.screenHeight() * 9 / 10 + 40
        log((btnLeft,btnTop))
        compose_new = monkey.visible(downViewId)
        log('start load')
        monkey.touch_down_and_up(btnLeft, btnTop)
#         monkey.touchByViewId(downViewId)
        log('downloading')
        monkey.sleep(20);
        log('open apk in coohua') 
#         monkey.touchByViewId(downViewId)
        monkey.touch_down_and_up(btnLeft, btnTop)
        monkey.sleep(3);
        monkey.touch_down_and_up(monkey.screenWidth() / 8 * 7, ey)
        log('system installing')
        monkey.sleep(20);
        
        log('open try play')
        monkey.touch_down_and_up(monkey.screenWidth() / 8 * 7, ey)
        monkey.sleep(20);
    elif(isShare):
        log('share request')
        monkey.sleep(1);
#monkey.touch_down_and_up(180,120)
# Presses the Menu button
# device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

#monkey.takeAndSaveSnapshot(dir,'png')