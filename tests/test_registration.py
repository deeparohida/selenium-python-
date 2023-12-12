import pytest
from selenium.webdriver.common.by import By

from PageObjects.homepage import HomePage
from PageObjects.loginpage import LoginPage
from PageObjects.registerpage import Registration
from utilities.Baseclass import BaseClass


class TestRegistration(BaseClass):



    def test_registrationpage(self):
        homepage = HomePage(self.driver)
        homepage.login_page().click()
        loginPage = LoginPage(self.driver)
        loginPage.registeruser().click()

    def test_newuserregistration(self):
        registerpage = Registration(self.driver)
        registerpage.getusername().send_keys("pinks22wwe2")
        registerpage.getpassword().send_keys("eeuuajj199")
        registerpage.getconfirmpass().send_keys("eeuuajj199")
        registerpage.getemail().send_keys("pinks33@gmail.com")
        registerpage.getphone().send_keys("8191919199")
        registerpage.getaddress1().send_keys("check1")
        registerpage.getaddress2().send_keys("check2")
        registerpage.getcity().send_keys("check3")
        registerpage.getstate().send_keys("check4")
        registerpage.getcountry().send_keys("check5")
        self.selectOptionByText(registerpage.getlanguage(), "english")
        self.selectOptionByText(registerpage.getcategory(), "FISH")
        registerpage.getlistoptions().click()
        registerpage.getbanneroption().click()
        registerpage.saveaccount().click()

    #def test_existinguser(self):
        #registerpage = Registration(self.driver)
        #registerpage.getemail().send_keys()
