
import win32process
import subprocess
'''
win32process.CreateProcess('C:\\Program Files\\TS Support\\MultiCharts64\\MultiCharts64.exe', '',
None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,
win32process.STARTUPINFO(), shell=True)
'''
def call():
    subprocess.call(["C:\\Program Files\\TS Support\\MultiCharts64\\MultiCharts64.exe"], shell=True)

