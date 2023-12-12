from PageObjects.homepage import HomePage
from PageObjects.loginpage import LoginPage
from utilities.Baseclass import BaseClass
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver


class TestLogin(BaseClass):

    def test_signin(self):
        homePage = HomePage(self.driver)
        homePage.login_page().click()

    @pytest.mark.skip
    def test_loginvaliduser(self):
        loginsuccessful = LoginPage(self.driver)
        loginsuccessful.getusername().send_keys("004")
        loginsuccessful.getpassword().clear()
        loginsuccessful.getpassword().send_keys("ppppkk44")
        loginsuccessful.clickbutton().click()
