from selenium.webdriver.common.by import By

from pageobjects.Checkoutpage import CheckoutPage


class HomePage:
    def __init__(self,driver):#constructor to take driver
        self.driver = driver
    shop = (By.LINK_TEXT,"Shop")#class variable
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,"email")
    password = (By.ID,"exampleInputPassword1")
    check = (By.ID,"exampleCheck1")
    control = (By.ID,"exampleFormControlSelect1")
    submit =  (By.XPATH,"//input[@class='btn btn-success']")
    sucess_msg = (By.XPATH,"//*[contains(@class,'alert-success')]")

    #self.driver.find_element_by_link_text("Shop").click()
    #self.driver.find_element_by_css_selector("input[name='name']").send_keys("Liby")
    #driver.find_element_by_name("email").send_keys("libyelsa795@gmail.com")
    #driver.find_element_by_id("exampleInputPassword1").send_keys("mary@12")
    #driver.find_element_by_id("exampleCheck1").click()
    #driver.find_element_by_id("exampleFormControlSelect1"))
    #driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
    #driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
    def getshopicon(self):
        self.driver.find_element(*HomePage.shop).click()
        Checkoutpage = CheckoutPage(self.driver)
        return Checkoutpage
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def getCheck(self):
        return self.driver.find_element(*HomePage.check)
    def getControl(self):
        return self.driver.find_element(*HomePage.control)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def getSucessMsg(self):
        return self.driver.find_element(*HomePage.sucess_msg)
    def getSucessMsg2(self):
        return self.driver.find_element(*HomePage.sucess_msg)
    def getSucessMsg3(self):
        return self.driver.find_element(*HomePage.sucess_msg)