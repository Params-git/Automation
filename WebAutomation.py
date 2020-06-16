from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = 'E:\chromedriver')
#driver = webdriver.Firefox(executable_path = 'E:\geckodriver.exe')

XPATH = "//*[@id='block_top_menu']/ul/li[3]/a"

driver.get('http://automationpractice.com/index.php')
driver.find_element_by_xpath(XPATH).click() #clicking the button

print(driver.title)
print(driver.current_url)

time.sleep(5)
#driver.close() #close only browser
driver.quit() #closing all tabs in a browser
