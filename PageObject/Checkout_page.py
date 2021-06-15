from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self,driver):
        self.driver = driver

    product_group = (By.XPATH, "//h4[@class='card-title']/a")
    add_button = (By.XPATH, "//app-card-list[@class='row']/app-card[4]//div[2]")

    #checkout = self.driver.find_element_by_partial_link_text("Checkout ")

    check_out_btn = (By.PARTIAL_LINK_TEXT,"Checkout ")

    def product_group_ele(self):
        return self.driver.find_elements(*CheckOut.product_group)

    def add_button_click(self):
        return self.driver.find_element(*CheckOut.add_button)

    def check_out_btn_click(self):
        return self.driver.find_element(*CheckOut.check_out_btn)



