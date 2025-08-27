
# Block comment: Ctrl + / or Shift + Alt + A

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time

# Initializing test environment

ServiceObj = Service('D:\Python\chrome_driver\chromedriver.exe')
driver = webdriver.Chrome(service = ServiceObj)

driver.maximize_window()

# Common variables: web links, functions, page elements & timestamp
 
HangfireQA        = 'http://mad-cmsweb-qa:8081/Dashboard/recurring'
GetNotCompleted   = "//*[contains(text(), 'GetNotCompletedSyncBatchesStatusesRecurringCommand')]"
MonitorAdlibQueue = "//*[contains(text(), 'MonitorAdlibQueueCommand')]"
GetCompleted      = "//*[contains(text(), 'GetCompletedSyncBatchesStatusesRecurringCommand')]"
Trigger           = '//*[@id="wrap"]/div[2]/div/div/div/div[1]/button[1]'

def trigger():
    driver.find_element(By.XPATH, GetNotCompleted).click(); time.sleep(0.5)
    driver.find_element(By.XPATH, MonitorAdlibQueue).click(); time.sleep(0.5)
    driver.find_element(By.XPATH, GetCompleted).click(); time.sleep(0.5)
    driver.find_element(By.XPATH, Trigger).click(); time.sleep(0.5)

print();print("--- Started  at:", datetime.now().strftime("%H:%M:%S"));print()

# Trigger commands in Hangfire

driver.get(HangfireQA); time.sleep(2)
for i in range(3):
    trigger()
driver.refresh(); time.sleep(1); driver.close()
print(); print("--- Finished at:", datetime.now().strftime("%H:%M:%S")); print()


