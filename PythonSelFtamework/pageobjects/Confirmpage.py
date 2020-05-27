from selenium.webdriver.common.by import By


class ConfirmPage:
    checkbox = (By.CSS_SELECTOR,"input#country")
    checkbox_content = (By.LINK_TEXT,"India")
    confirm = (By.XPATH,"//div[@class = 'checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR,"[type='submit']")
    sucess_msg = (By.CSS_SELECTOR,"div[class*='alert-success']")
    #self.driver.find_element_by_css_selector("input#country")
    # self.driver.find_element_by_link_text("India")
    #self.driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']")
    #self.driver.find_element_by_css_selector("[type='submit']")
    #self.driver.find_element_by_css_selector("div[class*='alert-success']")

    def __init__(self,driver):
        self.driver = driver


    def check_box_click(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def checkbox_text(self):
        return self.driver.find_element(*ConfirmPage.checkbox_content)

    def confirm_click(self):
        return self.driver.find_element(*ConfirmPage.confirm)

    def submit_click(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def success_text2(self):
        return self.driver.find_element(*ConfirmPage.sucess_msg)

    def success_text3(self):
        return self.driver.find_element(*ConfirmPage.sucess_msg)

    def success_text4(self):
        return self.driver.find_element(*ConfirmPage.sucess_msg)

    def success_text5(self):
        return self.driver.find_element(*ConfirmPage.sucess_msg)