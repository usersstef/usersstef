
# Automated test
# Block comment: Shift + Alt + A (only in VS code editor)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Initializing test environment

print();print("  Initializing test environment...")

driver = webdriver.Chrome(
    executable_path=r"D:\Scripts\Python\Web_automation\chromedriver.exe"
)
driver.maximize_window()
print();print("--- Test started ---")

# Web links

Hangfire      = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
BatchExplorer = 'https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html'

# Trigger commands in Hangfire and Sync icon localization in Batch Explorer

def checkbox():
    driver.find_element_by_xpath("//*[@id='isAgeSelected']").click(); time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='check1']").click(); time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='isAgeSelected']").click(); time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='check1']").click(); time.sleep(0.5)

while True:
    driver.get(Hangfire);time.sleep(1)
    for i in range(2):
        checkbox()
    driver.refresh();time.sleep(1)
    driver.get(BatchExplorer);time.sleep(1)
    driver.find_element_by_xpath("//*[@id='normal-btn-success']").click();time.sleep(1) # Refresh button in BE
    SyncIcon = "/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a"    # Sync icon is not present in BE
    #SyncIcon = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]"          # Sync icon is present in BE

    try:
        driver.find_element_by_xpath(SyncIcon)
        print();print(
            "The button is located");time.sleep(1)
        break
    except NoSuchElementException:
        print("The button is not located")
        pass
print("--- Test finished ---")
driver.close(); print()


