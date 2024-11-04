from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
	def __init__(self):
		# Define driver, options, and service
		chrome_option = Options()
		chrome_option.add_argument("--disable-search-engine-choice-screen")
		# Define the download location.
		download_path = os.getcwd()
		prefs = {"download.default_directory":download_path}
		chrome_option.add_experimental_option("prefs":prefs)
		service = Service("./chromedriver-mac-arm64 2/chromedriver")
		self.driver = webdriver.Chrome(options=chrome_option, service=service)

	def login(self, username="duck0", password="Duck5910!!"):
		# Load the webpage.
		self.driver.get("https://demoqa.com/login")
		# Locate username, password, and login.
		username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
		password_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
		login_button = self.driver.find_element(By.ID, "login")
		# Fill in username, and password, and click the button.
		username_field.send_keys(username)
		password_filed.send_keys(password)
		self.driver.execute_script("arguments[0].click();", login_button)

	def fill_form(self, fullname, email, currentaddress, permanentaddress):
		# Locate the Elements dropdown and Text box.
		elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
																			 '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
		elements.click()
		text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
		text_box.click()

		# Locate the form fields and submit button.
		fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
		email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
		currentaddress_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
		permanentaddress_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
		submit_button = self.driver.find_element(By.ID, "submit")

		# Fill in the form fields. 
		fullname_field.send_keys(fullname)
		email_field.send_keys(email)
		currentaddress_field.send_keys(currentaddress)
		permanentaddress_field.send_keys(permanentaddress)
		self.driver.execute_script("arguments[0].click();", submit_button)

	def download(self):
		# Locate the Upload and Download section and the download button.
		upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,'item-7')))
		upload_download.click()
		download_button = self.driver.find_element(By.ID, "downloadButton")
		self.driver.execute_script("arguments[0].click();", download_button)

	def close(self):
		self.driver.quit()


if __name__ == "__main__":
	webautomation = WebAutomation()
	webautomation.login("duck0", "Duck5910!!")
	webautomation.fill_form("Andrew Lee", "duckk0249@gmail.com", "Street 1", "Street 2")
	webautomation.download()
	WebAutomation.close()
