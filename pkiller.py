
# Script to check tasklist and kill one or multiple procs

import os, subprocess, time

def check_tsklist():            # Function to parse the tasklist and return all current processes
    def getTasks(name):
        r = os.popen('tasklist /v').read().strip().split('\n')
        for i in range(len(r)):
            s = r[i]
            if name in r[i]:
                return r[i]
        return []
    if __name__ == '__main__':
        imgName = 'WatUX.exe'
        r = getTasks(imgName)
        if not r:  # targeted proc is not alive, so just print the info message (uncomment the other lines to kill another proc if needed)
            print('%s is not running' % (imgName))
            #os.system('taskkill /f /im mspaint.exe')
            #os.system('taskkill /f /im taskmgr.exe')
        else:      # targeted proc is alive, then kill it (uncomment the other lines to kill one or multiple procs at once if needed)
            os.system('taskkill /f /im WatUX.exe')
            #os.system('taskkill /f /im mspaint.exe')
            #os.system('taskkill /f /im taskmgr.exe')
while True:
    check_tsklist()
    time.sleep(2)
    
    
