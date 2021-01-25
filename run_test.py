
## Automated tests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time

print();print("  Initializing test environment...")

driver = webdriver.Chrome(executable_path=r'D:\Scripts\Python\Web_automation\chromedriver.exe')
driver.maximize_window()

# Get URL & close modal
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html');time.sleep(1)
close_modal = '//*[@id="at-cv-lightbox-button-holder"]/a[2]'
driver.find_element_by_xpath(close_modal).click();time.sleep(1)

print();print("--- Testing process started ---")

# Input single field
driver.find_element_by_xpath("//*[@id='user-message']").send_keys('The text message is inserted here successfully');time.sleep(1)  # enter msg
driver.find_element_by_xpath("//*[@id='get-input']/button").click();time.sleep(0.5)  # show msg button

# Input two field
driver.find_element_by_tag_name('body').send_keys(Keys.END);time.sleep(1)
driver.find_element_by_xpath("//*[@id='sum1']").send_keys('1'); time.sleep(1)  # enter a field
driver.find_element_by_xpath("//*[@id='sum2']").send_keys('2'); time.sleep(1)  # enter b field
driver.find_element_by_xpath("//*[@id='gettotal']/button").click(); time.sleep(1)  # get total
driver.find_element_by_tag_name('body').send_keys(Keys.HOME);time.sleep(1)
print();print(" *** Input test finished successfully *** ")

# Checkboxes
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[1]/a").click();time.sleep(1)  # Input form
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[1]/ul/li[2]/a").click();time.sleep(1)  # checkbox
driver.find_element_by_xpath("//*[@id='isAgeSelected']").click();time.sleep(1)
driver.find_element_by_xpath("//*[@id='check1']").click();time.sleep(1)  # check all
print();print(" *** Checkboxes test finished successfully *** ")

# Modals
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[5]/a").click();time.sleep(1)  # Alert & modals
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[5]/ul/li[2]/a").click();time.sleep(1)  # Bootstrap modal
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a").click();time.sleep(1)  # multiple modals
driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[3]/a").click();time.sleep(1)
driver.find_element_by_xpath("//*[@id='myModal2']/div/div/div[6]/a[1]").click();time.sleep(1)  # close
driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[4]/a[1]").click();time.sleep(1)
print();print(" *** Modals test finished successfully *** ")

# Dropdown list
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[1]/a").click();time.sleep(1)  # main tree
driver.find_element_by_xpath("//*[@id='treemenu']/li/ul/li[1]/ul/li[4]/a").click();time.sleep(1)  # dropdown list
Select(driver.find_element_by_xpath("//*[@id='select-demo']")).select_by_index(6);time.sleep(1)  # selector
driver.find_element_by_tag_name('body').send_keys(Keys.END);time.sleep(1)
driver.find_element_by_xpath("//*[@id='multi-select']/option[6]").click(); time.sleep(1)  # option
driver.find_element_by_xpath("//*[@id='printMe']").click(); time.sleep(1) # first selected
driver.find_element_by_tag_name('body').send_keys(Keys.HOME);time.sleep(1)
print();print(" *** Dropdown test finished successfully *** ")

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
print();print(" *** Range slider test finished successfully *** ")

# Copy paste & submit form
driver.get('https://www.seleniumeasy.com/test/input-form-demo.html');time.sleep(1)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[1]/div/div/input").send_keys('First name' + Keys.CONTROL + 'a' + 'c');time.sleep(1)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[2]/div/div/input").send_keys(Keys.CONTROL + 'v');time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[3]/div/div/input").send_keys('address@example.com');time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[4]/div/div/input").send_keys('0723685712');time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[5]/div/div/input").send_keys('Str. No. 8');time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[6]/div/div/input").send_keys('Las Vegas');time.sleep(1)
Select(driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[7]/div/div/select")).select_by_index(29);time.sleep(0.5)
postal_code = 123456
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[8]/div/div/input").send_keys(postal_code);time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[9]/div/div/input").send_keys('www.website.com');time.sleep(0.5)
driver.find_element_by_tag_name('body').send_keys(Keys.END);time.sleep(1)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[10]/div/div[2]/label/input").click();time.sleep(1)  # radio button
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[11]/div/div/textarea").send_keys('Web Automation Project');time.sleep(1)
driver.find_element_by_xpath("//*[@id='contact_form']/fieldset/div[13]/div/button").click(); time.sleep(1)  # submit button
driver.find_element_by_tag_name('body').send_keys(Keys.HOME);time.sleep(1)
print();print(" *** Submit form test finished successfully *** ")

# Drag and drop
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element_by_xpath("//*[@id='box1']")  # Stokkolm
target = driver.find_element_by_xpath("//*[@id='box101']")  # Sweden
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box2']")  # Oslo
target = driver.find_element_by_xpath("//*[@id='box102']")  # Norway
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box3']")  # Washington
target = driver.find_element_by_xpath("//*[@id='box103']")  # United States
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box4']")  # Copenhagen
target = driver.find_element_by_xpath("//*[@id='box104']")  # Denmark
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box5']")  # Seoul
target = driver.find_element_by_xpath("//*[@id='box105']")  # South Corea
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box6']")  # Rome
target = driver.find_element_by_xpath("//*[@id='box106']")  # Italy
ActionChains(driver).drag_and_drop(source,target).perform()

source = driver.find_element_by_xpath("//*[@id='box7']")  # Madrid
target = driver.find_element_by_xpath("//*[@id='box107']")  # Spain
ActionChains(driver).drag_and_drop(source,target).perform();time.sleep(1)
print();print(" *** Drag & drop test finished successfully *** ")
print();print(" *** All tests executed successfully :) *** ");print()
driver.refresh();time.sleep(1)
driver.close()


