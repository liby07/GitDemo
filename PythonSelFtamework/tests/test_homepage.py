from selenium import webdriver
from selenium.webdriver.support.select import Select
import pytest

from TestData.HomepageData import Testhomepagedata
from pageobjects.Homepage import HomePage
from utilities.BaseClass import Baseclass


class TestHomePage(Baseclass):

    def test_homepage(self,getData):
        log = self.Get_Logger()
        homepage = HomePage(self.driver)
        log.info("Name is"+getData["Name"])
        homepage.getName().send_keys(getData["Name"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys(getData["Password"])
        homepage.getCheck().click()
        self.SelectByOption(homepage.getControl(),getData["Gender"])
        self.driver.implicitly_wait(5)
        homepage.getSubmit().click()
        message = homepage.getSucessMsg().text  # using Xpath
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=Testhomepagedata.get_data('Testcase2'))
    def getData(self,request):
        return request.param