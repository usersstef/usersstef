

import os
import subprocess
import pygetwindow as gw
import time

def check_tsklist():
    def getTasks(name):
        r = os.popen('tasklist /v').read().strip().split('\n')
        for i in range(len(r)):
            s = r[i]
            if name in r[i]:
                return r[i]
        return []
    if __name__ == '__main__':
        imgName = 'mstsc.exe'
        r = getTasks(imgName)
        if r:
            win = gw.getWindowsWithTitle('ro-3106708.ad.ea.com')[0]
            win.activate()
            win.maximize(); time.sleep(1)
            win.minimize()
while True:
    check_tsklist()
    time.sleep(290)
