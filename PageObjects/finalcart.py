from selenium.webdriver.common.by import By


class MyCart:

    def __init__(self, driver):
        self.driver = driver

    Quantity = (By.XPATH, '//input[@name="EST-6"]')
    listprice = (By.XPATH, '//form/table/tbody/tr[2]/td[6]')
    totalcost = (By.XPATH, '//form/table/tbody/tr[2]/td[7]')
    subtotal = (By.XPATH, '//form/table/tbody/tr[3]/td[1]')
    updatecartbutton = (By.XPATH, '//input[@name="updateCartQuantities"]')
    removebutton = (By.XPATH, '//form/table/tbody/tr[2]/td[8]')
    message = (By.XPATH, '//form/table/tbody/tr[2]/td[1]')

    def getqty(self):
        return self.driver.find_element(*MyCart.Quantity)

    def getlistprice(self):
        return self.driver.find_element(*MyCart.listprice)

    def gettotalcost(self):
        return self.driver.find_element(*MyCart.totalcost)

    def getsubtotal(self):
        return self.driver.find_element(*MyCart.subtotal)

    def updatecart(self):
        return self.driver.find_element(*MyCart.updatecartbutton)

    def emptycart(self):
        return self.driver.find_element(*MyCart.removebutton)

    def emptycarttext(self):
        return self.driver.find_element(*MyCart.message)