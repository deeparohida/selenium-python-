import pytest
from selenium.webdriver.common.by import By

from utilities.Baseclass import BaseClass


class Registration(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    confirmpassword = (By.NAME, "repeatedPassword")
    firstname = (By.NAME, "account.firstName")
    lastname = (By.NAME, "account.lastName")
    email = (By.NAME, "account.email")
    phone = (By.NAME, "account.phone")
    address1 = (By.NAME, "account.address1")
    address2 = (By.NAME, "account.address2")
    city = (By.NAME, "account.city")
    state = (By.NAME, "account.state")
    zip = (By.NAME, "account.zip")
    country = (By.NAME, "account.country")
    language = (By.NAME, "account.languagePreference")
    category = (By.NAME, "account.favouriteCategoryId")
    listoption = (By.NAME, "account.listOption")
    banneroption = (By.NAME, "account.bannerOption")
    submibutton = (By.NAME, "newAccount")

    def getusername(self):
        return self.driver.find_element(*Registration.username)

    def getpassword(self):
        return self.driver.find_element(*Registration.password)

    def getconfirmpass(self):
        return self.driver.find_element(*Registration.confirmpassword)

    def getemail(self):
        return self.driver.find_element(*Registration.email)

    def getphone(self):
        return self.driver.find_element(*Registration.phone)

    def getaddress1(self):
        return self.driver.find_element(*Registration.address1)

    def getaddress2(self):
        return self.driver.find_element(*Registration.address2)

    def getcity(self):
        return self.driver.find_element(*Registration.city)

    def getstate(self):
        return self.driver.find_element(*Registration.state)

    def getcountry(self):
        return self.driver.find_element(*Registration.country)

    def getlanguage(self):
        return self.driver.find_element(*Registration.language)

    def getcategory(self):
        return self.driver.find_element(*Registration.category)

    def getlistoptions(self):
        return self.driver.find_element(*Registration.listoption)

    def getbanneroption(self):
        return self.driver.find_element(*Registration.banneroption)

    def saveaccount(self):
        return self.driver.find_element(*Registration.submibutton)
