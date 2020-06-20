from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logindata

chromedriver = "E:\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
action = ActionChains(driver)
driver.maximize_window()
time.sleep(1)

driver.get('https://www.amazon.com')
time.sleep(1)

def XPATH(selector):
	path = driver.find_element_by_xpath(selector)
	return path

firstlevelmenu = XPATH('//*[@id="nav-link-accountList"]/div/span')
action.move_to_element(firstlevelmenu).perform() 
time.sleep(2)
secondlevelmenu = XPATH('//*[@id="nav-flyout-ya-signin"]/a/span')
secondlevelmenu.click()
time.sleep(3)

signinelement = XPATH('//*[@id="ap_email"]')
signinelement.send_keys(logindata.EMAIL)
time.sleep(4)

cont = XPATH('//*[@id="continue"]')
cont.click()
time.sleep(3)

password = XPATH('//*[@id="ap_password"]')
password.send_keys(logindata.PASSWORD)
time.sleep(4)

login = XPATH('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)
    
searchbox = XPATH('//*[@id="twotabsearchtextbox"]')
searchbox.send_keys("redmi phone")
time.sleep(3)

search = XPATH('//*[@id="nav-search"]/form/div[2]/div/input')
search.click()
time.sleep(3)

product = XPATH('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[1]/div/div/span/a/div/img').click()
driver.implicitly_wait(5)

addToCart = XPATH('//*[@id="submit.add-to-cart"]').click()
time.sleep(3)

##driver.implicitly_wait(5)
##byNow = driver.find_element_by_xpath('//*[@id="submit.buy-now"]').click()
##time.sleep(2)

Cart = XPATH('//*[@id="nav-cart"]').click()
time.sleep(5)
 
driver.quit()
