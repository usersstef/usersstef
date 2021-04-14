
import pygetwindow as gw
from datetime import datetime
import time

while True:
    win = gw.getWindowsWithTitle('ro-3106708.ad.ea.com')[0]
    now = datetime.now()
    run_time = now.strftime("%H:%M:%S")
    if True:
        win.activate()
        win.maximize(); time.sleep(1)
        win.minimize()
        print("Checked:", run_time); print()
        time.sleep(290)