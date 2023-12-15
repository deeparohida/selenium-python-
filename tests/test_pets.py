import time

import pytest

from PageObjects.addcartpage import CartPage
from PageObjects.finalcart import MyCart
from PageObjects.homepage import HomePage
from PageObjects.petselectpage import PetOptions
from utilities.Baseclass import BaseClass


class TestPets(BaseClass):

    def test_pets(self):
        homePage = HomePage(self.driver)
        mypet = homePage.petselect()
        i = -1
        for pet in mypet:
            i = i + 1
            homePage.petselect()[1].click()

    def test_selectmypets(self):
        petselection = PetOptions(self.driver)
        selectpetfrom = petselection.select_pet()
        j = -1
        for select in selectpetfrom:
            j = j + 1
            selecttext = select.text
            if selecttext == "K9-BD-01":
                petselection.select_pet()[j].click()
                break
        time.sleep(3)

    def test_addtocart(self):
        cartitempage = CartPage(self.driver)
        cartitems = cartitempage.addtocart()
        k = -1
        for item in cartitems:
            k = k + 1
            itemtext = item.text
            if itemtext == "EST-6":
                cartitempage.additemsbutton()[k].click()
                break
        time.sleep(3)

    def test_updateqty(self):
        itemquantity = MyCart(self.driver)
        updateexistingqty = itemquantity.getqty()
        updateexistingqty.clear()
        total_cost = itemquantity.gettotalcost().text
        sub_total = itemquantity.getsubtotal().text
        newqty = updateexistingqty.send_keys("4")
        if updateexistingqty != newqty:
            itemquantity.updatecart().click()

        assert total_cost in sub_total



    @pytest.mark.skip
    def test_emptycart(self):
        removecartitem = MyCart(self.driver)
        removecartitem.emptycart().click()
        carttext = removecartitem.emptycarttext().text

        assert "Your cart is empty" in carttext
