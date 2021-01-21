from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logindata

class TwitterBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("E:\drivers\chromedriver.exe")

    def closebrowser(self):
        self.driver.quit()

    def login(self):
        driver = self.driver
        driver.get('https://www.twitter.com')
        time.sleep(2)
        signin = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
        user_Name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user_Name.send_keys(self.username)
        time.sleep(2)
        password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(self.password)
        Login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
    
    def tweet_post(self,tweet):
        driver = self.driver
        driver.get('https://www.twitter.com/home')
        Tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        Tweet.send_keys(tweet)

    def calculate_followings(self):
        driver = self.driver
        driver.get('https://www.twitter.com/home/following')
        # item = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[1]/div/a/div[2]').click()\

    def like_tweet(self,hashtag):
        driver = self.driver
        driver.get('https://www.twitter.com/search?q=' +hashtag+ '&src=typd')
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = driver.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(links)

            # for link in links:
            #     driver.get('https://twitter.com' + link)
            #     try:
            #         driver.find_element_by_class_name('HeartAnimation').click()
            #         time.sleep(10)

            #     except Exception as ex:
            #         time.sleep(10)

myAccount = TwitterBot(logindata.TWITTER_USER_NAME, logindata.PASSWORD)
myAccount.login()
time.sleep(2)
myAccount.like_tweet("electronic")
# time.sleep(2)
# myAccount.closebrowser()
