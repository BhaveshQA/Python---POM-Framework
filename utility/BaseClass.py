import inspect
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    testURL = "https://rahulshettyacademy.com/angularpractice/"

    def element_presence(self,xpath):
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath )))


    def drop_down_select_by_index(self,locator,index):
        dropwonw = Select(locator)
        dropwonw.select_by_index(index)

    def getLogger(self):

        loggername = inspect.stack()[1][3]

        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler("result.log")

        formatter = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger
