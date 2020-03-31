
## Script to check tasklist and kill the WATUX proc

import os
import subprocess
import time

def check_tsklist():            ## Parse the tasklist and return all processes
    def getTasks(name):
        r = os.popen('tasklist /v').read().strip().split('\n')
        for i in range(len(r)):
            s = r[i]
            if name in r[i]:
                return r[i]
        return []
    if __name__ == '__main__': 	## if targeted proc is alive, then kill it
        imgName = 'WatUX.exe'
        r = getTasks(imgName)
        if not r:               ## if targeted proc is not alive, then kill another proc at choice
            print('%s is not running' % (imgName))
            #os.system('taskkill /f /im mspaint.exe')
            #os.system('taskkill /f /im taskmgr.exe')
        else:
            os.system('taskkill /f /im WatUX.exe')
while True:
    check_tsklist()
    time.sleep(2)