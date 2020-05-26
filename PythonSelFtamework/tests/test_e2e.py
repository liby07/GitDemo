import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import Baseclass
from pageobjects.Checkoutpage import CheckoutPage
from pageobjects.Confirmpage import ConfirmPage
from pageobjects.Homepage import HomePage


class Testone(Baseclass):
    def test_selpython(self):
        log = self.Get_Logger()
        homepage = HomePage(self.driver)
        log.info("getting all products name")
        checkoutpage = homepage.getshopicon()
        products =checkoutpage.getitems()
        log.info(products)
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            log.info(product_name)
            if product_name == 'Blackberry':
                product.find_element_by_xpath("div/button").click()
        checkoutpage.checkout().click()
        assert "Blackberry" == checkoutpage.blackberry_selection().text
        confirmpage = checkoutpage.checkout_click()
        log.info("entering the country name as india")
        confirmpage.check_box_click().send_keys('ind')
        self.VerifyLinkPresence("suggestions")
        confirmpage.checkbox_text().click()
        confirmpage.confirm_click().click()
        confirmpage.submit_click().click()
        Sucess_msg = confirmpage.success_text().text
        log.info("Success msg printed as"+Sucess_msg)
        assert "Success! False Text Thank you!" in Sucess_msg

        print("just to check changes in repository")
        print("demo testing")
