
## Update CV from Linkedin profile to Ejobs profile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, pyperclip

# *** Set main paths ***

options = webdriver.ChromeOptions()
chrome_path= r"E:\miscellaneous\__scripts\python\Web_automation\chromedriver.exe"             # Path to driver
options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data")  # Path to user profile
driver = webdriver.Chrome(chrome_path, chrome_options=options)

LkProfile = "https://www.linkedin.com/in/tataru-stefan-4a2805105/"
EjProfile = "https://www.ejobs.ro/user/cv.php?cv_lang=en"

# ------ Define common variables for About section ------ #
#_________________________________________________________#

LEdit    = '//*[@id="ember124"]'            # Lk Edit
LSummary = 'summary'                        # Lk Summary
JEdit    = '//*[@id="objective"]/div[1]/a'  # Ej Edit
JSummary = 'objective'                      # Ej Summary
JSave    = '//*[@id="edit-obiectiv"]/div/div[2]/form/button'  # Ej Save

# About section

driver.get(LkProfile); time.sleep(3)  # open Lk profile

driver.find_element_by_class_name(LEdit).click(); time.sleep(2)
driver.find_element_by_name(LSummary).send_keys(Keys.CONTROL + 'a' + 'c')
SummaryContent = pyperclip.paste()
print(); print(SummaryContent)
driver.switch_to_default_content(); time.sleep(2)

driver.get(EjProfile); time.sleep(2)  # open Ej profile

driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
driver.find_element_by_name(JSummary).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
driver.find_element_by_name(JSummary).send_keys(SummaryContent)
driver.find_element_by_xpath(JSave).click()
driver.switch_to_default_content(); print()
print(" *** About_me was updated successfully *** "); time.sleep(2)

# ------ Define common variables for Experience section ------ #
#______________________________________________________________#

LDescript = 'position-description'             # Lk description modal
JDescript = 'responsabilities'                 # Ej description modal
JSave     = '//*[@id="edit-experienta"]/div/div[2]/form/button'

# ------ Define dinamic variables for Software Tester ------ #
#____________________________________________________________#

LEdit = '//*[@id="ember143"]'
JEdit = '//*[@id="experience-8459512"]/a'

driver.get(LkProfile); time.sleep(3)

driver.find_element_by_xpath(LEdit).click(); time.sleep(2)
driver.find_element_by_id(LDescript).send_keys(Keys.CONTROL + 'a' + 'c')
DescriptContent = pyperclip.paste()
print(); print(DescriptContent)
driver.switch_to_default_content(); time.sleep(2)

driver.get(EjProfile); time.sleep(2)

driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
driver.find_element_by_name(JDescript).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
driver.find_element_by_name(JDescript).send_keys(DescriptContent)
driver.find_element_by_xpath(JSave).click()
driver.switch_to_default_content(); print()
print(" *** Software Tester was updated successfully *** "); time.sleep(2)

# ------ Define dinamic variables for Game Tester ------ #
#________________________________________________________#

LEdit = '//*[@id="ember148"]'
JEdit = '//*[@id="experience-7535610"]/a'

driver.get(LkProfile); time.sleep(3)

driver.find_element_by_xpath(LEdit).click(); time.sleep(2)
driver.find_element_by_id(LDescript).send_keys(Keys.CONTROL + 'a' + 'c')
DescriptContent = pyperclip.paste()
print(); print(DescriptContent)
driver.switch_to_default_content(); time.sleep(2)

driver.get(EjProfile); time.sleep(2)

driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
driver.find_element_by_name(JDescript).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
driver.find_element_by_name(JDescript).send_keys(DescriptContent)
driver.find_element_by_xpath(JSave).click()
driver.switch_to_default_content(); print()
print(" *** Game Tester was updated successfully *** "); time.sleep(2)

# ------ Define dinamic variables for FHW/SW Technician ------ #
#______________________________________________________________#

LEdit = '//*[@id="ember159"]'
JEdit = '//*[@id="experience-7442692"]/a'

driver.get(LkProfile); time.sleep(3)

driver.find_element_by_xpath(LEdit).click(); time.sleep(2)
driver.find_element_by_id(LDescript).send_keys(Keys.CONTROL + 'a' + 'c')
DescriptContent = pyperclip.paste()
print(); print(DescriptContent)
driver.switch_to_default_content(); time.sleep(2)

driver.get(EjProfile); time.sleep(2)

driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
driver.find_element_by_name(JDescript).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
driver.find_element_by_name(JDescript).send_keys(DescriptContent)
driver.find_element_by_xpath(JSave).click()
driver.switch_to_default_content(); print()
print(" *** FHW/SW Technician was updated successfully *** "); time.sleep(2)

# ------ Define dinamic variables for IHW/SW Technician ------ #
#______________________________________________________________#

LEdit = '//*[@id="ember170"]'
JEdit = '//*[@id="experience-1208566"]/a'

driver.get(LkProfile); time.sleep(3)

driver.find_element_by_xpath(LEdit).click(); time.sleep(2)
driver.find_element_by_id(LDescript).send_keys(Keys.CONTROL + 'a' + 'c')
DescriptContent = pyperclip.paste()
print(); print(DescriptContent)
driver.switch_to_default_content(); time.sleep(2)

driver.get(EjProfile); time.sleep(2)

driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
driver.find_element_by_name(JDescript).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
driver.find_element_by_name(JDescript).send_keys(DescriptContent)
driver.find_element_by_xpath(JSave).click()
driver.switch_to_default_content(); print()
print(" *** IHW/SW Technician was updated successfully *** "); time.sleep(2)

# ------ Define dinamic variables for IT Operator ------ #
#________________________________________________________#

LEdit = '//*[@id="ember181"]'
JEdit = '//*[@id="experience-530891"]/a'

driver.get(LkProfile); time.sleep(3)

driver.find_element_by_xpath(LEdit).click(); time.sleep(2)
driver.find_element_by_id(LDescript).send_keys(Keys.CONTROL + 'a' + 'c')
DescriptContent = pyperclip.paste()
print(); print(DescriptContent)
driver.switch_to_default_content(); time.sleep(2)

driver.get(EjProfile); time.sleep(2)

driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
driver.find_element_by_name(JDescript).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
driver.find_element_by_name(JDescript).send_keys(DescriptContent)
driver.find_element_by_xpath(JSave).click()
driver.switch_to_default_content(); print()
print(" *** IT Operator was updated successfully *** ")












