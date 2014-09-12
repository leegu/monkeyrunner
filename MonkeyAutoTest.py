from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#from stu.lee.monkey.auto.run import Main
device = MonkeyRunner.waitForConnection()

fo = open('F:/python_workspace/TestPython/autoRun/monkeyrunner.json')
text = fo.read();
#print text
configJson = eval(text)
# print configJson['scan_event']['actions'][0].keys()
#device.shell('adb uninstall io.dcloud.HBuilder')
#device.removePackage('io.dcloud.HBuilder');
def getAbsInt(strValue,relValue):
    return int(float(strValue[0:len(strValue)-1]) * relValue / 100)

screenWidth = 720
screenHeight = 128
print getAbsInt('78%',screenWidth)
print device.getSystemProperty('display')


# print str(device.shell('adb devices'))
download_event = configJson['download_event']

def handleEvent(events):
    for d in events['actions']:
        if(d['type'] == 'touch'):
            touch_x = getAbsInt(d['touch_x'],screenWidth)
            touch_y = getAbsInt(d['touch_y'],screenHeight)
            print 'touch',touch_x,touch_y
        elif(d['type'] == 'sleep'):
            time = d['time']
            print 'sleep ' ,time
        elif(d['type'] == 'print'):
            msg = d['message']
            print 'print ' , msg
        elif(d['type'] == 'drag'):
            touch_s_x = getAbsInt(d['touch_s_x'],screenWidth)
            touch_s_y = getAbsInt(d['touch_s_y'],screenHeight)
            touch_e_x = getAbsInt(d['touch_e_x'],screenWidth)
            touch_e_y = getAbsInt(d['touch_e_y'],screenHeight)
            print 'drag ' , touch_s_x,touch_s_y,touch_e_x,touch_e_y
            
handleEvent(download_event)

def handle_del_apk():
    print 'execute handle_del_apk'
#     device.shell('adb pull /sdcard/t/new_apk_list.t F:/python_workspace/TestPython/autoRun/t/new_apk_list.t')
    apk_list_file = open('F:/python_workspace/TestPython/autoRun/t/new_apk_list.t')
    apkPName = apk_list_file.read()
    print 'will remove apk pname=' , apkPName
    device.removePackage(apkPName)
    MonkeyRunner.sleep(5)
    print 'execute handle_del_apk end'
    
handle_del_apk()