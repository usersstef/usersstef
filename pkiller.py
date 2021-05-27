
# Script to check tasklist and kill a proc

import os
import subprocess
import time

def check_tsklist():            ## Parse the tasklist and return all processes
    def getTasks(name):
        r = os.popen('tasklist /v').read().strip().split('\n')
        #print ('Number of tasks is %s' % (len(r)))
        for i in range(len(r)):
            s = r[i]
            if name in r[i]:
                #print ('%s in r[i]' %(name))
                return r[i]
        return []
    if __name__ == '__main__': 	## if targeted proc is alive, then kill it
        imgName = 'WatUX.exe'
        r = getTasks(imgName)
        if not r:
            print('%s is not running' % (imgName)) 
        else:
            os.system('taskkill /f /im WatUX.exe')
while True:
    check_tsklist()
    time.sleep(2)
    
    
