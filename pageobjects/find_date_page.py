from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import base64
import json

def parse_data(data):
    try:
        base64_decoded = base64.b64decode(data)
        utf8_string = base64_decoded.decode("utf-8")
        json_string = utf8_string.replace("diff-com.tui.common.search.SearchRequestData-", "")
        return json.loads(json_string)
    except Exception as e:
        print(e)
        pass

class FindDatePage:
    def __init__(self, driver):
        self.driver = driver
        self.find_date_popup = WebDriverWait(self.driver.instance, 30).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "section.matrix.matrix-responsive-table")))

        self.options = WebDriverWait(self.driver.instance, 30).until(
            EC.visibility_of_any_elements_located((
                By.CSS_SELECTOR, "div.visible-offer")))

        self.forward_button = WebDriverWait(self.driver.instance, 30).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "button.btn.btn-lg.btn-block.btn-primary.forward-navigation.ng-binding")))
        self.driver.instance.save_screenshot('available_trips.png')

        self.available_dates = self.driver.instance.find_elements_by_css_selector("[data-selector]")
        print("Found: " + str(len(self.available_dates)))

    def find_date_popup_visible(self):
        assert self.find_date_popup.is_displayed()

    def forward_button(self):
        assert self.forward_button().is_displayed()

    def options_visible(self):
        assert self.options().is_displayed()

    def select_available_dates(self, date_to_book, duration):
        assert len(self.available_dates) > 0
        if len(self.available_dates) > 0:
            print("Available rooms = " + str(len(self.available_dates)))
            for option in self.available_dates:
                data_value = parse_data(option.get_attribute('data-selector'))
                if data_value is not None and data_value["EarliestStart"] == date_to_book and duration in data_value[
                    "Durations"]:
                    option.click()

    def click_forward_button(self):
        self.driver.instance.find_element_by_css_selector(
            "button.btn.btn-lg.btn-block.btn-primary.forward-navigation.ng-binding").click()


