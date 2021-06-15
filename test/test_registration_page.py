import pytest

from PageObject.Registration_page import RegistrationPage
from testData.test_registration_data import Registation_Data
from utility.BaseClass import BaseClass


class Test_Registration(BaseClass):

    def test_registration(self, get_user_data):

        # call the logger function of the BaseClass
        log = self.getLogger()

        # create Registration_page class object
        registration_page = RegistrationPage(self.driver)
        log.info("Registration page object initiation done")

        self.driver.get(self.testURL)

        # implicit wait define
        self.driver.implicitly_wait(5)

        # Enter the name
        name = registration_page.get_name()

        # name.send_keys(get_user_data[0])
        log.info("Received firstname"+get_user_data["firstname"])
        name.send_keys(get_user_data["firstname"])

        # Enter Email
        email = registration_page.get_email()
        # email.send_keys(get_user_data[1])
        log.info("Received User email"+get_user_data["email"])
        email.send_keys(get_user_data["email"])


        # Enter password
        password = registration_page.set_password()
        password.send_keys("123456")

        # select checkbox
        registration_page.check_box_select()

        # gender selection
        self.drop_down_select_by_index(registration_page.gender_select(), 1)

        # click on the submit button
        registration_page.submit_btn_click()
        log.info("Form submitted successfully")

        # refresh the page, if we plan to run same testcase with multiple dataset
        self.driver.refresh()

    # pass this fixtures in the test_registration for the paramterized
    # @pytest.fixture(params=[("Bhavesh", "bhavesh@mailinator.com"), ("Hina", "hina@gamil.com")])

    # using the dictionary
    # here we can take data from the testData package
    @pytest.fixture(params=Registation_Data.get_registration_data_excel())
    def get_user_data(self, request):
        return request.param

