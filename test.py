
# Check the text alert

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())  # driver path
options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data")  # user profile path
driver.maximize_window()

for draft_content, priority in zip(range(2), range(2)):
    print()
    print("DraftContent_%d" %draft_content, "Priority %d" %priority)
    driver.get('https://twitter.com/intent/follow?screen_name=seleniumeasy')
    time.sleep(1)
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


class BootstrapAlert:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install())  # driver path
    options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data")  # user profile path
    driver.maximize_window()

    # Code to test
    def __init__(self):
        self.check_text()

    def check_text(self):
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
            self.driver.find_element_by_xpath(
                "/ html / body / div[2] / div / div[2] / div / div[2] / div[2] / button").click()

    def exit(self):
        self.driver.close()


if __name__ == '__main__':
    WebSession = BootstrapAlert()
    WebSession.exit()

    
    
    
    
    
    
    
    
