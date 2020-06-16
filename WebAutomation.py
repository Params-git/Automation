from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromedriver = "E:\chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.google.com/')

a = driver.find_element_by_name("q")
a.send_keys("harsh beniwal")
a.send_keys(Keys.ENTER)




# search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
# search.send_keys(Keys.ENTER)
