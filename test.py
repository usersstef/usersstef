
# Generate n number of Draft Contents

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
import time
import ctypes

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())                                    # driver path
options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data")  # user profile path
driver.maximize_window()

# Generating as many draft contents are needed

for draft_content, priority in zip(range(51), range(51)):
    print()
    print("DraftContent_%d" %draft_content, "Priority %d" %priority)
    driver.get('https://twitter.com/intent/follow?screen_name=seleniumeasy')
    time.sleep(1.5)
    driver.find_element_by_xpath(
        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/label/div/div[2]/div/input").send_keys(
        'DraftContent_%d' %draft_content)
    time.sleep(1)  # user
    driver.find_element_by_xpath(
        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[2]/label/div/div[2]/div/input").send_keys(
        priority)
    time.sleep(1)  # pass
    driver.find_element_by_xpath(
        "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/span/span/span").click()
    time.sleep(1)  # no thanks button
driver.close()

# after above code is run, there will be to execute 4 ore 5 lines more to bulk publish the 50 or 100 draft contents :)
#ctypes.windll.user32.MessageBoxW(0, "Draft Contents generated & published", "Info", 1)

# Checking the text inside an alert message and doing something after

class BootstrapAlert:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data")
    driver.maximize_window()

    def __init__(self):
        self.check_context()

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
                "/ html / body / div[2] / div / div[2] / div / div[2] / div[2] / button").click();time.sleep(1)

    def exit(self):
        self.driver.close()


if __name__ == '__main__':
    WebSession = BootstrapAlert()
    WebSession.exit()
