from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ExtrasPage:

    def __init__(self, driver):
        self.driver = driver


        self.load_extras_page = WebDriverWait(self.driver.instance, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "fieldset.form-section.address-section")))
        self.load_insurance_section = WebDriverWait(self.driver.instance, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.col-md-12.ancillary-group")))
        self.driver.instance.save_screenshot('extras.png')

    def validate_extras_loaded(self):
        assert self.load_extras_page.is_displayed()

    def validate_insurance_section_loaded(self):
        assert self.load_insurance_section.is_displayed()

    def fill_passanger(self):
        self.driver.instance.find_element_by_name('passengers.0.firstName').send_keys("John")
        self.driver.instance.find_element_by_name('passengers.0.lastName').send_keys("Doe")
        self.driver.instance.find_element_by_css_selector("input.form-control.birth-date").send_keys("19900101")
        self.driver.instance.save_screenshot('passengers.png')

    def fill_address(self):
        self.driver.instance.find_element_by_css_selector("input[type='radio'][value='MALE']").click()
        self.driver.instance.find_element_by_name('bookerDetails.0.streetAddress').send_keys("testgatan 1")
        self.driver.instance.find_element_by_name('bookerDetails.0.zipCode').send_keys("12345")
        self.driver.instance.find_element_by_name('bookerDetails.0.city').send_keys("stockholm")
        self.driver.instance.find_element_by_name('bookerDetails.0.phoneNumber').send_keys("0733123456")
        self.driver.instance.find_element_by_name('bookerDetails.0.emailAddress').send_keys("some@email.com")
        self.driver.instance.find_element_by_name('bookerDetails.0.emailAddress2').send_keys("some@email.com")
        self.driver.instance.save_screenshot('address.png')

    def select_cancellation_insurance(self):
        self.driver.instance.find_element_by_css_selector(
            "input[type='radio'][value='variantProductCode=fake_no_thanks_option_code,sysInfo=']").click()
        self.driver.instance.save_screenshot('cancellation_insurance.png')

    def select_transfer(self):
        self.driver.instance.find_element_by_css_selector(
            "input[type='radio'][value='variantProductCode=PC-000119876,sysInfo=D122 PLPATINDGD190228 01202604249']").click()
        self.driver.instance.save_screenshot('transfer.png')

    def select_travel_insurance(self):
        self.driver.instance.find_element_by_css_selector(
            "input[type='radio'][value='variantProductCode=fake_no_thanks_option_code,sysInfo=']").click()
        self.driver.instance.save_screenshot('travel_insurance.png')

    def click_summer_dropdown_button(self):
        self.driver.instance.find_element_by_id("price-summary-container").click()
        self.driver.instance.save_screenshot('finished.png')

