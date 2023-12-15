from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    items = (By.XPATH, '//div[@id="Catalog"]/table/tbody/tr/td')
    addtocartbutton = (By.CSS_SELECTOR, '.Button')

    def addtocart(self):
        return self.driver.find_elements(*CartPage.items)

    def additemsbutton(self):
        return self.driver.find_elements(*CartPage.addtocartbutton)

