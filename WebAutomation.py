from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import logindata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "E:\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
action = ActionChains(driver)
driver.maximize_window()
time.sleep(1)

driver.get('https://www.amazon.in')
time.sleep(1)


firstlevelmenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/div/span')
action.move_to_element(firstlevelmenu).perform() 
time.sleep(2)
secondlevelmenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondlevelmenu.click()
time.sleep(2)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.EMAIL)
time.sleep(2)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(2)

password = driver.find_element_by_xpath('//*[@id="ap_password"]')
password.send_keys(logindata.PASSWORD)
time.sleep(2)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(2)
    
searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbox.send_keys("laptop")
time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search.click()
time.sleep(4)

product = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[4]/div/span/div/div/div[2]/div[1]/div/div/span/a/div/img').click()

##addToCart = driver.find_element_by_name("submit.add-to-cart").click()
##action.move_to_element(addToCart).click().perform()
##time.sleep(2)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='buy-now-button']")))
element.click()
time.sleep(2)

Cart = driver.find_element_by_xpath('//*[@id="nav-cart"]').click()
time.sleep(4)
 
driver.quit()

