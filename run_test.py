
## Automated web navigation

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time, pyperclip

# *** Setting paths ***
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install()) # driver path
options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data") # user profile path
driver.maximize_window()

# Get URL & close modal
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html');time.sleep(1)
close_modal = '//*[@id="at-cv-lightbox-button-holder"]/a[2]'
driver.find_element_by_xpath(close_modal).click();time.sleep(1)

# Input single field
driver.find_element_by_xpath("//*[@id='user-message']").send_keys('The text message is inserted here successfully');time.sleep(1) # enter msg button
driver.find_element_by_xpath("//*[@id='get-input']/button").click();time.sleep(1) # show msg button

# Input two field
driver.find_element_by_xpath("//*[@id='sum1']").send_keys('1'); time.sleep(1) # enter a field
driver.find_element_by_xpath("//*[@id='sum2']").send_keys('2'); time.sleep(1) # enter b field
driver.find_element_by_xpath("//*[@id='gettotal']/button").click() # get total button
driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);");time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME);time.sleep(1)

# Dropdown list
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[1]/a").click();time.sleep(1)
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[1]/ul/li[4]/a").click();time.sleep(1) # droplist
Select(driver.find_element_by_xpath("//*[@id='select-demo']")).select_by_index(6);time.sleep(1) # selector
driver.find_element_by_xpath("//*[@id='multi-select']/option[6]").click(); time.sleep(1) # option
driver.find_element_by_xpath("//*[@id='printMe']").click(); time.sleep(1) # first selected button
driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);");time.sleep(1)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME);time.sleep(1)

# Range sliders
driver.get('https://www.seleniumeasy.com/test/drag-drop-range-sliders-demo.html');time.sleep(1)
slider = driver.find_element_by_xpath("//*[@id='slider1']/div/input")
ActionChains(driver).click_and_hold(slider).move_by_offset(90, 0).release().perform()
slider = driver.find_element_by_xpath("//*[@id='slider2']/div/input")
ActionChains(driver).click_and_hold(slider).move_by_offset(90, 0).release().perform()
slider = driver.find_element_by_xpath("//*[@id='slider3']/div/input")
ActionChains(driver).click_and_hold(slider).move_by_offset(90, 0).release().perform()
slider = driver.find_element_by_xpath("//*[@id='slider4']/div/input")
ActionChains(driver).click_and_hold(slider).move_by_offset(90, 0).release().perform()
slider = driver.find_element_by_xpath("//*[@id='slider5']/div/input")
ActionChains(driver).click_and_hold(slider).move_by_offset(90, 0).release().perform()
slider = driver.find_element_by_xpath("//*[@id='slider6']/div/input")
ActionChains(driver).click_and_hold(slider).move_by_offset(90, 0).release().perform();time.sleep(1)

# Copy paste
driver.get('https://www.seleniumeasy.com/test/input-form-demo.html');time.sleep(1)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[1]/div/div/input").send_keys('Text for copy paste' + Keys.CONTROL + 'a' + 'c');time.sleep(1)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[2]/div/div/input").send_keys(Keys.CONTROL + 'v');time.sleep(1)

# Drag and drop
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
print(); print(" *** Drag and drop action started... *** ")
source = driver.find_element_by_xpath("//*[@id='box2']") # Oslo
target = driver.find_element_by_xpath("//*[@id='box102']") # Norway
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box1']") # Stokkolm
target = driver.find_element_by_xpath("//*[@id='box101']") # Sweden
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box7']") # Madrid
target = driver.find_element_by_xpath("//*[@id='box107']") # Spain
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box6']") # Rome
target = driver.find_element_by_xpath("//*[@id='box106']") # Italy
ActionChains(driver).drag_and_drop(source,target).perform();

source = driver.find_element_by_xpath("//*[@id='box5']") # Seoul
target = driver.find_element_by_xpath("//*[@id='box105']") # South Corea
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box4']") # Copenhagen
target = driver.find_element_by_xpath("//*[@id='box104']") # Denmark
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box3']") # Washington
target = driver.find_element_by_xpath("//*[@id='box103']") # United States
ActionChains(driver).drag_and_drop(source,target).perform();time.sleep(1)
print(); print(" *** Script executed successfully :) *** ")
driver.refresh();time.sleep(1);driver.close()





