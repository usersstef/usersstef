
## Update CV from Linkedin profile to Ejobs profile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, pyperclip

class WebSession:

# *** Set main paths ***

	options = webdriver.ChromeOptions()
	chrome_path= r"E:\miscellaneous\__scripts\python\Web_automation\chromedriver.exe"             # Path to driver
	options.add_argument(r"user-data-dir=C:\Users\Stefan\AppData\Local\Google\Chrome\User Data")  # Path to user profile
	driver = webdriver.Chrome(chrome_path, chrome_options=options)

	def __init__(self):
		self.Update()
	
	def Update(self):
	
# ------ Define common variables for Experience section ------ #
#______________________________________________________________#

		LkProfile = "https://www.linkedin.com/in/tataru-stefan-4a2805105/"
		EjProfile = "https://www.ejobs.ro/user/cv.php?cv_lang=en"

		LDescript = 'position-description'             # Lk description modal
		JDescript = 'responsabilities'                 # Ej description modal
		JSave     = '//*[@id="edit-experienta"]/div/div[2]/form/button'

# ------ Define dinamic variables for Software Tester ------ #
#____________________________________________________________#

		LEdit = '//*[@id="ember143"]'
		JEdit = '//*[@id="experience-8459512"]/a'
		
		self.driver.get(LkProfile); time.sleep(3)
		self.driver.find_element_by_xpath(LEdit).click(); time.sleep(2)
		self.driver.find_element_by_id(LDescript).send_keys(Keys.CONTROL + 'a' + 'c')
		DescriptContent = pyperclip.paste()
		print(); print(DescriptContent)
		self.driver.switch_to_default_content(); time.sleep(2)

		self.driver.get(EjProfile); time.sleep(2)

		self.driver.find_element_by_xpath(JEdit).click(); time.sleep(2)
		self.driver.find_element_by_name(JDescript).send_keys(Keys.CONTROL + 'a'); time.sleep(1)
		self.driver.find_element_by_name(JDescript).send_keys(DescriptContent)
		self.driver.find_element_by_xpath(JSave).click()
		self.driver.switch_to_default_content(); print()
		print(" *** Software Tester was updated successfully *** "); time.sleep(2)

StartSession = WebSession()
StartSession.driver



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	