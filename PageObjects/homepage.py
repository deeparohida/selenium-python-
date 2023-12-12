import pytest
from selenium.webdriver.common.by import By

from PageObjects.loginpage import LoginPage
from utilities.Baseclass import BaseClass


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    login = (By.LINK_TEXT, 'Sign In')

    def login_page(self):
        return self.driver.find_element(*HomePage.login)
        #gotologin = LoginPage(self.driver)
        #return gotologin