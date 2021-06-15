from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self,driver):
        self.driver = driver
    # Define the page locators
    # name = driver.find_element_by_css_selector("input[name='name']")
    name_reg =(By.CSS_SELECTOR,"input[name='name']")

    # email = driver.find_element_by_name("email")
    email_reg =(By.NAME, "email")

    # password = driver.find_element_by_id("exampleInputPassword1")
    password_reg =(By.ID,"exampleInputPassword1")

    # chkbox = driver.find_element_by_class_name("form-check-input")
    chkbox_reg =(By.CLASS_NAME, "form-check-input")

    # gender = driver.find_element_by_xpath("//*[@id='exampleFormControlSelect1']")
    gender_drop_reg = (By.XPATH, "//*[@id='exampleFormControlSelect1']")

    # submit_btn = driver.find_element_by_xpath("//*[@value='Submit']")
    submit_btn_reg =(By.XPATH, "//*[@value='Submit']")


    # create method for all the locators

    def get_name(self):
        return self.driver.find_element(*RegistrationPage.name_reg)

    def get_email(self):
        return self.driver.find_element(*RegistrationPage.email_reg)

    def set_password(self):
        return self.driver.find_element(*RegistrationPage.password_reg)

    def check_box_select(self):
        self.driver.find_element(*RegistrationPage.chkbox_reg).click()

    def gender_select(self):
        return self.driver.find_element(*RegistrationPage.gender_drop_reg)

    def submit_btn_click(self):
        self.driver.find_element(*RegistrationPage.submit_btn_reg).click()
