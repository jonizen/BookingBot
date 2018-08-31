from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class FindFlightPage:

    def __init__(self, driver):
        self.driver = driver

        self.driver.instance.save_screenshot('flightpage.png')
        self.load_flight_page = WebDriverWait(self.driver.instance, 30).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "button.btn.btn-lg.btn-block.btn-primary.forward-navigation.ng-binding")))


    def forward_button(self):
        assert self.load_flight_page.is_displayed()

    def click_forward_button(self):
        self.driver.instance.find_element_by_css_selector(
            "button.btn.btn-lg.btn-block.btn-primary.forward-navigation.ng-binding").click()

