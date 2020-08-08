
## Script for scroll down in a youtube page in Chrome

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
chrome_path= r"E:\miscellaneous\__scripts\python\Web_automation\chromedriver.exe" # Path to driver
options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data") # Path to chrome user profile
driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.get("https://www.youtube.com/user/secureteam10/videos")

print(driver.title)
print(driver.current_url)
print(driver.window_handles)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);") ## Scroll down to bottom
    time.sleep(1) # Wait to load page
    print("Loading next page...")
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
       print()
       print("Scrolling session is done and the web page is ready to use.")
       break
    last_height = new_height
driver.switch_to_default_content()
##driver.close()