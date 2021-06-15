from selenium.webdriver.common.by import By

from PageObject.Checkout_page import CheckOut


class Homepage:

    # create variable to store
    shop = (By.LINK_TEXT,"Shop")

    # create constructor
    def __init__(self,driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkout = CheckOut(self.driver)
        return checkout
