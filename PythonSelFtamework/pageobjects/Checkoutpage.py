from selenium.webdriver.common.by import By

from pageobjects.Confirmpage import ConfirmPage


class CheckoutPage:

    items = (By.XPATH,"//div[@class='card h-100']")
    checkoutbox = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    blackberry_item = (By.XPATH,"//div/h4/a[contains(text(),Blackberry)]")
    checkoutbutton = (By.XPATH,"//button[@class='btn btn-success']")


    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    #self.driver.find_element_by_xpath("//div/h4/a[contains(text(),Blackberry)]")
    #self.driver.find_element_by_xpath("//button[@class='btn btn-success']")


    def getitems(self):
        return self.driver.find_elements(*CheckoutPage.items)
    def checkout(self):
        return self.driver.find_element(*CheckoutPage.checkoutbox)
    def blackberry_selection(self):
        return self.driver.find_element(*CheckoutPage.blackberry_item)
    def checkout_click(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton).click()
        Confirmpage = ConfirmPage(self.driver)
        return Confirmpage
    def checkout_click2(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton).click()
        Confirmpage = ConfirmPage(self.driver)
        return Confirmpage
    def checkout_click3(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton).click()
        Confirmpage = ConfirmPage(self.driver)
        return Confirmpage
