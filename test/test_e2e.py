"""
Select product from the list of the product with product name and complete the checkout process
"""
import time

from PageObject.Checkout_page import CheckOut
from PageObject.Homepage import Homepage
from utility.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.usefixtures("setup")
class Testone(BaseClass):
    def test_e2e(self):
        # pagewise object creation
        homepage = Homepage(self.driver)
        #checkoutpage = CheckOut(self.driver)
        self.driver.implicitly_wait(5)
        # Launch the testURL
        self.driver.get(BaseClass.testURL)

        # Homepage class function
        # homepage.shopItems()

        checkoutpage = Homepage.shopItems(self)
        # keep all item in one product list

        time.sleep(2)
        product_group= checkoutpage.product_group_ele()
        # product_group = self.driver.find_elements_by_xpath("//h4[@class='card-title']/a")
        # count =len(product_group)
        # print(count)
        for product in product_group:
            print(product.text)
            # time.sleep(2)
            if product.text == 'Blackberry':
                #add_btn_ = self.driver.find_element_by_xpath("//app-card-list[@class='row']/app-card[4]//div[2]")
                add_btn = checkoutpage.add_button_click()
                add_btn.click()

        # click on the checkout button
        #checkout = self.driver.find_element_by_partial_link_text("Checkout ")
        #time.sleep(5)
        checkout = checkoutpage.check_out_btn_click()
        checkout.click()

        # click on checkout button from cart page
        checkout_cart_list = self.driver.find_element_by_xpath("//button[@class='btn btn-success']")
        checkout_cart_list.click()

        # Enter country name for delivery location
        country = self.driver.find_element_by_xpath("//input[@id='country']")
        country.send_keys('ind')

        # explicit wait

        #wait = WebDriverWait(self.driver, 6)
        #wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul")))

        # created function for explicit wait in base class and access it in test-class
        self.element_presence("//div[@class='suggestions']/ul")

        # select the country name from the auto suggest dropdown
        country_name = self.driver.find_elements_by_xpath("//div[@class='suggestions']/ul")
        count = len(country_name)
        print(count)

        # select 'india' from the dropdown
        for county_select in country_name:
            print(county_select.text)
            if county_select.text == 'India':
                time.sleep(2)
                county_select.click()
                break

        # click on the I Agree checkbox
        time.sleep(1)
        agree_checkbox = self.driver.find_element_by_xpath("//input[@id='checkbox2']")
        agree_checkbox_text = self.driver.find_element_by_xpath("//label[@for='checkbox2']")

        if agree_checkbox.is_selected():
            print("selected")
        else:
            agree_checkbox_text.click()

        print(agree_checkbox.is_selected())

        time.sleep(1)
        # click on the purchase button
        purchase_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
        purchase_btn.click()

        # check the success message after click on the purchase
        success_msg = "Success! Thank you! Your order will be delivered in next few weeks :-)."

        get_message = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]")
        print(get_message.text)

        # take screenshot
        self.driver.get_screenshot_as_file("Test.png")

        # verify the success message
        assert success_msg in get_message.text
