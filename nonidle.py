
# The script perform Alt + Tab command on an open window

import pygetwindow as gw
from datetime import datetime
import time

while True:
    win = gw.getWindowsWithTitle('TheNameOfTheWindow')[0]
    run_time = datetime.now().strftime("%H:%M:%S")
    if True:
        win.activate(); win.maximize(); time.sleep(1); win.minimize()
        print("Checked:", run_time); print()
        time.sleep(290)

        
