
## Script for scroll down in a youtube page in Firefox

from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="E:\\miscellaneous\\__scripts\\python\\Web_automation\\Firefox\\geckodriver.exe")
driver.get("https://www.youtube.com/user/secureteam10/videos?disable_polymer=1")

print(driver.title)
print(driver.current_url)
print(driver.window_handles)

while True:
    try:
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);") # Scroll down to bottom
        time.sleep(1) # Wait to load page
        xpath1 = "/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div/div/div/div/ul/li[2]/button/span/span[2]"
        destination_page_link = driver.find_element_by_xpath(xpath1)
        destination_page_link.click()
        print("Loading next page...")
    except:
	    print()
	    print("Scrolling session is done and the web page is ready to use."); break
#driver.close()

''' Open & switch tabs, where "-3" is first tab and "-1" is last aka "...handles[2]":
driver.execute_script("window.open('');")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[2])

driver.switch_to_window(driver.window_handles[-3])
time.sleep(1)
driver.switch_to_window(driver.window_handles[-2])
time.sleep(1)
driver.switch_to_window(driver.window_handles[-1])
time.sleep(1)
driver.switch_to_window(driver.window_handles[-3])'''
