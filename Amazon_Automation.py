from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import logindata

class AmazonBot:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome("E:\drivers\chromedriver.exe")

    def closebrowser(self):
        self.driver.quit()

    def login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.amazon.com')
        time.sleep(2)

        firstlevelmenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/div/span')
        action = ActionChains(driver)
        action.move_to_element(firstlevelmenu).perform() 
        time.sleep(2)
        secondlevelmenu =driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span').click()
        time.sleep(3)
        signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(self.email)
        time.sleep(4)
        cont = driver.find_element_by_xpath('//*[@id="continue"]').click()
        time.sleep(3)
        password = driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(self.password)
        time.sleep(4)
        login = driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
        time.sleep(3)

    def searchItems(self,Item):
        driver = self.driver
        searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(Item)
        time.sleep(3)
        search = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
        time.sleep(3)
        product = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[1]/div/div/span/a/div/img').click()
        driver.implicitly_wait(5)

    def add_to_cart(self):
        driver = self.driver
        addToCart = driver.find_element_by_xpath('//*[@id="submit.add-to-cart"]').click()
        time.sleep(3)
        Cart = driver.find_element_by_xpath('//*[@id="nav-cart"]').click()
        time.sleep(5)


MyAmazonAccount = AmazonBot(logindata.EMAIL, logindata.PASSWORD)
MyAmazonAccount.login()
time.sleep(2)
MyAmazonAccount.searchItems("Redmi phone")
time.sleep(2)
MyAmazonAccount.add_to_cart()
time.sleep(5)
MyAmazonAccount.closebrowser()