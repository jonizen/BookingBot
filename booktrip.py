import unittest
import time
from pprint import pprint
from unittest import TextTestRunner
from botdriver.botdriver import BotDriver
from pageobjects.booking_page import BookingPage
from pageobjects.find_date_page import FindDatePage
from pageobjects.find_flight_page import FindFlightPage
from pageobjects.breakfast_page import BreakfastPage
from pageobjects.extras_page import ExtrasPage


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import sys

baseurl = "https://www.tui.se/resa/spanien/gran-canaria/san-agustin/don-gregory/?partysizes=1%3B&departureCode=ARN&departureDate=2019-02-28&duration=8&referer=searchresult"
date_to_book = "2019-02-28"
duration = 8




class BookTrip(unittest.TestCase):

    def setUp(self):
        self.driver = BotDriver()
        self.driver.navigate(baseurl)

    def test_book_available_room(self):
        try:

            print("Try to find and book trip!")

            booking_page = BookingPage(self.driver)
            booking_page.validate_book_extras_loaded()
            booking_page.click_adjust_button()


            find_date_page = FindDatePage(self.driver)
            find_date_page.select_available_dates(date_to_book, duration)
            find_date_page.click_forward_button()

            find_flight_page = FindFlightPage(self.driver)
            find_flight_page.forward_button()
            find_flight_page.click_forward_button()

            breakfast_page = BreakfastPage(self.driver)
            breakfast_page.forward_button()
            breakfast_page.click_forward_button()

            extras_page = ExtrasPage(self.driver)
            extras_page.validate_extras_loaded()
            extras_page.validate_insurance_section_loaded()
            extras_page.fill_passanger()
            extras_page.fill_address()
            extras_page.select_cancellation_insurance()
            extras_page.select_transfer()
            extras_page.select_travel_insurance()
            extras_page.click_summer_dropdown_button()

            return

        except TimeoutException:
            self.driver.instance.save_screenshot('Error_timeout.png')
            self.driver.instance.quit()
            self.fail("Timeout occurred..")
            print("No offers found...")

        except KeyboardInterrupt:
            self.driver.instance.quit()
            sys.exit()

        except Exception:
            self.driver.instance.save_screenshot('error.png')
            self.driver.instance.quit()
            self.fail("Failed with %s" % error)
            pass

    def tearDown(self):
        self.driver.instance.quit()


def main():
    try:
        while True:
            test = unittest.TestLoader().loadTestsFromName("test_book_available_room", module=BookTrip)
            book_result = TextTestRunner().run(test)
            if len(book_result.failures) is 0 and len(book_result.errors) is 0:
                print("Successful booking check mail!")
                break
            else:
                print("Will try again in 5 minutes...")
                time.sleep(300)

    except KeyboardInterrupt:
        sys.exit()

    except Exception:
        pass


if __name__ == '__main__':
    main()
