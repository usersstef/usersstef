
# Automated actions with loops & functions

from selenium import webdriver
import time

print();print("  Initializing test environment...")

driver = webdriver.Chrome(executable_path=r'D:\Scripts\Python\Web_automation\chromedriver.exe')
driver.maximize_window()

print();print("--- Testing process started ---")

# Generating draft contents

for draft_content, priority in zip(range(2), range(2)):
    print()
    print("DraftContent_%d" % draft_content, "Priority %d" % priority)
    driver.get('https://twitter.com/intent/follow?screen_name=seleniumeasy')
    time.sleep(1.5)
    driver.find_element_by_xpath(
        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/label/div/div["
        "2]/div/input").send_keys(
        'DraftContent_%d' % draft_content)
    time.sleep(1)  # user
    driver.find_element_by_xpath(
        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[2]/label/div/div["
        "2]/div/input").send_keys(
        priority)
    time.sleep(1)  # pass
    driver.find_element_by_xpath(
        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/span/span/span").click()
    time.sleep(1)  # no thanks button
print();print(" *** Test executed successfully :) *** ");print()
driver.close()

# Read & validate the text of an alert message and doing something after

""" class BootstrapAlert:

    driver = webdriver.Chrome(executable_path=r'D:\Scripts\Python\Web_automation\chromedriver.exe')
    driver.maximize_window()

    print();print("--- Testing process started ---")

    def check_context(self):
        self.driver.get('https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html')
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='normal-btn-success']").click()
        time.sleep(1)
        alert = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]")
        alert_content = alert.text

        if alert_content == alert.text:
            print()
            print("The message is: " + alert_content)
            time.sleep(1)
        else:
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/ html / body / div[2] / div / div[2] / div / div[2] / div[2] / button").click()
            time.sleep(1)

    def __init__(self):
        self.check_context()

    def exit(self):
        self.driver.close()

if __name__ == '__main__':
    WebSession = BootstrapAlert()
    WebSession.exit()
print();print(" *** Test executed successfully :) *** ");print() """


