from selenium.webdriver.common.by import By


class PetOptions:
    def __init__(self, driver):
        self.driver = driver

    petoptions = (By.XPATH, '//div[@id="Catalog"]/table/tbody/tr/td/a')

    def select_pet(self):
        return self.driver.find_elements(*PetOptions.petoptions)
