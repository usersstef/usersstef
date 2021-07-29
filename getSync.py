
# Automated test
# Block comment: Shift + Alt + A

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

# Initializing test environment

print();print("  Initializing test environment...")

driver = webdriver.Chrome(
    executable_path=r"D:\Scripts\Python\Web_automation\chromedriver.exe"
)
driver.maximize_window()

# Common variables: web links, timestamps & page elements

Hangfire      = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
BatchExplorer = 'https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html'
Refresh       = '//*[@id="normal-btn-success"]'                            # Refresh button in BE
#SyncIcon      = " "                                                        # Sync icon not available in BE
SyncIcon      = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]"           # Sync icon available in BE

def run_time():
    print(datetime.now().strftime("%H:%M:%S"));print()
def checkbox():
    driver.find_element_by_xpath("//*[@id='isAgeSelected']").click(); time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='check1']").click(); time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='isAgeSelected']").click(); time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='check1']").click(); time.sleep(0.5)
print();print("--- Test started at:");run_time()

# Trigger commands in Hangfire and Sync icon localization in Batch Explorer

while True:
    driver.get(Hangfire);time.sleep(1)
    for i in range(2):
        checkbox()
    driver.refresh();time.sleep(1)
    driver.get(BatchExplorer);time.sleep(1)
    driver.find_element_by_xpath(Refresh).click();time.sleep(1)
    try:
        driver.find_element_by_xpath(SyncIcon)
        print(
            "The Sync button is available");time.sleep(1);print()
        print("--- Test finished at:");run_time()
        break
    except NoSuchElementException:
        print("The button is not available")
        pass
driver.close()




