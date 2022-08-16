from instagramUserInfo import email, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(3)

        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)




    def getFollowers(self):
        self.browser.get(f"https://instagram.com/{self.username}")
        time.sleep(6)
        self.browser.get(f"https://instagram.com/{self.username}/followers")
        time.sleep(6)
        dialog = self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]")
        #still getting error to reach followers
        followers = self.browser.find_elements(By.CLASS_NAME,"_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm")
        followerCount = len(dialog.find_elements(By.CSS_SELECTOR,"a"))
        print(f"first count: {followers}")

        for user in followers:
            link = user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            print(link)
instgrm = Instagram(email, password)
instgrm.signIn()
instgrm.getFollowers()