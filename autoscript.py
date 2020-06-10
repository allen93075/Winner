import os
import time
import subprocess
import pyautogui
import pynput
from threading import Thread
import win32com.client
import win32api
import win32con
import win32gui


def wait():
    time.sleep(50.0)
    print("這是等待函數")


def callMC2(): #LSTM
    commend = '"C:\Program Files\TS Support\MultiCharts64\MultiCharts64.exe"'
    p = subprocess.Popen(commend, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(p.pid)
    wait()
    # p.communicate(input='\n')
    pyautogui.hotkey('alt', 'f')
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(4):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey('alt','i')
    time.sleep(2)
    pyautogui.press('l')
    time.sleep(2)
    pyautogui.press('r')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    p.kill()

def callMC(): #RF
    commend = '"C:\Program Files\TS Support\MultiCharts64\MultiCharts64.exe"'
    p = subprocess.Popen(commend, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(p.pid)
    wait()
    # p.communicate(input='\n')
    pyautogui.hotkey('alt', 'f')
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(2):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press('p')
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey('alt','i')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(1)
    pyautogui.press('r')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    p.kill()







    # p.communicate(pyautogui.hotkey('alt', 'f'))
    # # pyautogui.hotkey('alt', 'f')
    # p.communicate(time.sleep(1))
    # p.communicate(pyautogui.press("tab"))
    # p.communicate(pyautogui.press("enter"))

    print("等待結束")

def callMC3():
    commend = '"C:\Program Files\TS Support\MultiCharts64\MultiCharts64.exe"'
    p = subprocess.Popen(commend, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # shell = win32com.client.Dispatch("WScript.Shell")
    wait()

def callQM():
    commend = '"C:\Program Files\TS Support\MultiCharts64\QuoteManager.exe"'
    p = subprocess.Popen(commend, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(7)
    pyautogui.hotkey('ctrl','m')
    time.sleep(2)
    for i in range(6):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(0.5)
    p.kill()







# callQM()
# callMC()
# subprocess.Popen(["start", "notepad.exe"], shell=True)
# callMC3()
# pyautogui.hotkey('a   lt', 'f')
#
