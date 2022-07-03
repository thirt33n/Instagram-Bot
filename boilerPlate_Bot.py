

#This is the base boiler-plate code for loggin in alone

# importing module
from datetime import date
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import sys
  
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# The XPaths of some of these buttons may change over time please ensure that these are up-to date
# when running the program
  
  
class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
  
    def login(self):
        self.bot.get(self.base_url)
  
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
  
        # first pop-up uncomment the next 2 lines if error encountered
        # self.bot.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        time.sleep(3)
  
        # 2nd pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
        time.sleep(4)
        
        #post button
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()  

        #self.bot.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()
        
        
        
        upload_btn = self.bot.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
        time.sleep(2)
        

def init():
    bot('Your_Username', 'Your_Password') #Enter your Username and password here.
  
    # when our program ends it will show "done".
    input("DONE")
  

# calling the function
init()