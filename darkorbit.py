from darkorbitInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class Darkorbit:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()


    def logIn(self):
        self.browser.get("https://www.darkorbit.com/?originalURL=darkorbit.com&")
        time.sleep(3)
        btnAgree = self.browser.find_element(By.XPATH,"//*[@id='qc-cmp2-ui']/div[2]/div/button[2]")
        btnAgree.click()
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='bgcdw_login_form_username']")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='bgcdw_login_form_password']")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
        self.browser.get("https://it3.darkorbit.com/indexInternal.es?action=internalClan")
        membersBtn = self.browser.find_element(By.XPATH, "//*[@id='subNavTop']/ul/li[2]/a")
        membersBtn.click()


darkorbit = Darkorbit(username,password)
darkorbit.logIn()
