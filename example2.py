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
        followersLink = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a")
        followersLink.click()
instgrm = Instagram(email, password)
instgrm.signIn()
instgrm.getFollowers()