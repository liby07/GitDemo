import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class Baseclass:
    def VerifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, text)))

    def SelectByOption(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def Get_Logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile2.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
