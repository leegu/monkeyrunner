
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
    def shell(self,cmd):
        return self.device.shell(cmd)
    def removePackage(self,pname):
        self.device.removePackage(pname)
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
#         return 480 
    def screenHeight(self):
#        h = self.device.getProperty('height')
#        return h;
        return 1280;
#         return 800
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
print 'monkey inited'
monkey.waitForConnection()
print 'conn device'
fo = open('F:/python_workspace/TestPython/autoRun/monkeyrunner.json')
text = fo.read();
#print text
configJson = eval(text)
print 'load json config'

print 'init test env'
# sets a variable with the package's internal name
package = configJson['package']

# sets a variable with the name of an Activity in the package
#activity = 'com.coohuaclient.ui.activity.SplashActivity'
activity = configJson['activity']
# sets the name of the component to start
runComponent = package + '/' + activity

#runComponent = 'io.dcloud.HBuilder' + '/' + 'com.example.runtime_sdk_test.ActivityEntry'
# Runs the component
monkey.startActivity(runComponent)


space_time = configJson['space_time']
monkey.sleep(space_time);
screenWidth = monkey.screenWidth()
screenHeight = monkey.screenHeight()
unlock_start_positon_x = getAbsInt(configJson['unlock_start_positon'][0],screenWidth)
unlock_start_positon_y = getAbsInt(configJson['unlock_start_positon'][1],screenHeight)

unlock_start_positon_to_left_x = getAbsInt(configJson['unlock_start_positon_to_left'][0],screenWidth)
unlock_start_positon_to_left_y = getAbsInt(configJson['unlock_start_positon_to_left'][1],screenHeight)

unlock_start_positon_to_right_x = getAbsInt(configJson['unlock_start_positon_to_right'][0],screenWidth)
unlock_start_positon_to_right_y = getAbsInt(configJson['unlock_start_positon_to_right'][1],screenHeight)

wake_up_wait_time = configJson['wake_up_wait_time']

unlock_drag_wait_time = configJson['unlock_drag_wait_time']

share_event = configJson['share_event']
scan_event = configJson['scan_event']
download_event = configJson['download_event']


def handleEvent(events):
    for d in events['actions']:
        if(d['type'] == 'touch'):
            touch_x = getAbsInt(d['touch_x'],screenWidth)
            touch_y = getAbsInt(d['touch_y'],screenHeight)
            print 'touch',touch_x,touch_y
#             loop = d['loop'];
#             for i in range(0,loop):
#                 monkey.touch_down_and_up(touch_x, touch_y)
#                 monkey.sleep(space_time)
#                 i += 1;
            monkey.touch_down_and_up(touch_x, touch_y)
        elif(d['type'] == 'sleep'):
            time = d['time']
            print 'sleep ' ,time
            monkey.sleep(time)
        elif(d['type'] == 'print'):
            msg = d['message']
            print 'print ' , msg
        elif(d['type'] == 'drag'):
            touch_s_x = getAbsInt(d['touch_s_x'],screenWidth)
            touch_s_y = getAbsInt(d['touch_s_y'],screenHeight)
            touch_e_x = getAbsInt(d['touch_e_x'],screenWidth)
            touch_e_y = getAbsInt(d['touch_e_y'],screenHeight)
#             loop = d['loop'];
#             for i in range(0,loop):
#                 monkey.drag(touch_s_x, touch_s_y, touch_e_x, touch_e_y, 0.1, 1)
#                 monkey.sleep(space_time)
#                 i += 1;
            monkey.drag(touch_s_x, touch_s_y, touch_e_x, touch_e_y, 0.1, 1)
            print 'drag ' , touch_s_x,touch_s_y,touch_e_x,touch_e_y
            
def handle_download_event():
    print 'execute handle_download_event'
    handleEvent(download_event)
    print 'execute handle_download_event_end'
    
def handle_share_event():
    print 'execute handle_share_event'
    handleEvent(share_event)
    print 'execute handle_share_event end'
    
def handle_scan_event():
    print 'execute handle_scan_event'
    handleEvent(scan_event)
    print 'execute handle_scan_event end'

def handle_del_apk():
    print 'execute handle_del_apk'
    monkey.shell('adb pull /sdcard/t/new_apk_list.t F:/python_workspace/TestPython/autoRun/t/new_apk_list.t')
    apk_list_file = open('F:/python_workspace/TestPython/autoRun/t/new_apk_list.t')
    apkPName = apk_list_file.read()
    print 'will remove apk pname=' , apkPName
    monkey.removePackage(apkPName)
    monkey.sleep(5)
    print 'execute handle_del_apk end'
    
print 'will execute'
loop = configJson['loop']
print 'loop=' ,loop
loop_index = 0 #| loop_index < loop
while(loop == -1 ):
    print 'executing'
    loop_index += 1
    monkey.press_power_down_and_up()
    monkey.sleep(space_time);
    toLeft = True;
    if (toLeft):
        ex = unlock_start_positon_to_left_x
        ey = unlock_start_positon_to_left_y
        log('will drag to left')
    else:
        ex = unlock_start_positon_to_right_x
        ey = unlock_start_positon_to_right_y
        log('will drag to right')
    duration = 0.1; 
    steps = 1;
    tuple = (unlock_start_positon_x, unlock_start_positon_to_left_y, ex, ey, duration, steps)
    log(tuple);
    monkey.wakeup()
    monkey.sleep(wake_up_wait_time);
    monkey.drag(unlock_start_positon_x, unlock_start_positon_to_left_y, ex, ey, duration, steps)
    
    # if hasnt btn_webview_download ,we think isnt download button
    downViewId = 'id/btn_webview_download'
    isDownload = monkey.visible(downViewId)
    print 'isDownload ',isDownload
    isDownload = True
    if(isDownload):
        handle_download_event()
        handle_del_apk()
    else:
        handle_scan_event()
        handle_share_event()






