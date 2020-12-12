
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'D:\Scripts\Python\Web_automation\chromedriver.exe')  # driver path
driver.maximize_window()


def check_context():
    driver.get('https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html')
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='normal-btn-success']").click()
    time.sleep(1)
    alert = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]")
    alert_content = alert.text

    if alert_content == alert.text:
        print()
        print("The message is: " + alert_content)
        time.sleep(1)
    else:
        time.sleep(1)
        driver.find_element_by_xpath(
            "/ html / body / div[2] / div / div[2] / div / div[2] / div[2] / button").click()
        time.sleep(1)


check_context()
driver.close()

