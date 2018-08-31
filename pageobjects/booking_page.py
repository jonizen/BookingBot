from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BookingPage:

    def __init__(self, driver):
        self.driver = driver
        self.book_page = WebDriverWait(self.driver.instance, 30).until(
                    EC.visibility_of_element_located((
                        By.CSS_SELECTOR, "div.price-example-main")))

    def validate_book_extras_loaded(self):
        assert self.book_page.is_displayed()

    def click_adjust_button(self):
        self.driver.instance.find_element_by_css_selector("a.btn.btn-sales.open-tui-modal").click()