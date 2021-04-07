
import pygetwindow as gw
import time

while True:
    win = gw.getWindowsWithTitle('ro-3106708.ad.ea.com')[0]
    if win == win:
        win.activate()
        win.maximize(); time.sleep(1)
        win.minimize(); print()
        print(" *** Checked *** "); print()
        time.sleep(5)