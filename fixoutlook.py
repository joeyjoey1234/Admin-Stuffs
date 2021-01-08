import datetime
import os
import psutil

now = datetime.datetime.now()
plus_10 = now + datetime.timedelta(minutes= 9)
number = 0


def sys_clean(x):
    if ans == "YES" or ans == "Y":
        os.system("sfc /scannow")
        os.system("dism /online /Cleanup-Image /RestoreHealth")
        print("if this fails its okay")
    elif ans == "NO" or ans == "N":
        pass



def clean_outlook():
    click_to_run = str('"C:\Program Files\Microsoft Office 15\ClientX64\OfficeClickToRun.exe"')
    os.system("net stop wsearch")
    os.system("Taskkill /IM wbxcOIEx.exe /F")
    os.system("powershell -command remove-item 'C:\Program Files (x86)\Microsoft Office\Root\Office16\EMSMDB32.DLL' -force")
    os.system("{} scenario=Repair platform=x86 culture=en-us forceappshutdown=True RepairType=FullRepair DisplayLevel=True".format(click_to_run))
    print("!!!!!Make sure to do a FULL ONLINE REAPAIR!!!! not a quick repair")

def pro_func():
    for x in range(1,4):
        number = 0
        for x in psutil.process_iter(attrs=['name']):
            x = str(x)
            if "name='OfficeClickToRun.exe'" in x:
                print("found it!")
                number += 1
            else:
                pass
    return number

def time_func():
    if now == plus_10:
        if pro_func() == 3:
            pass
        elif pro_func() == 2:
            pass
        elif pro_func() == 1:
            print("It should be done by now go ahead and close me and open outlook")
        else:
            pass


print(clean_outlook())
print(time_func())
















