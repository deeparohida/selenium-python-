import pytest
from selenium.webdriver.common.by import By

from PageObjects.registerpage import Registration
from utilities.Baseclass import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginbutton = (By.NAME, "signon")
    registernow = (By.LINK_TEXT, 'Register Now!')


    #def loginasvaliduser(self, username, password):
        #self.send_keys(self.username, username)
        #self.send_keys(self.password, password)
        #self.click(self.loginbutton)


    def getusername(self):
        return self.driver.find_element(*LoginPage.username)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickbutton(self):
        return self.driver.find_element(*LoginPage.loginbutton)

    def registeruser(self):
        return self.driver.find_element(*LoginPage.registernow)
        #registerpage = Registration(self.driver)
        #return registerpage