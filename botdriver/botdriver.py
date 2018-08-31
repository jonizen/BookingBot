
from selenium import webdriver


class BotDriver:

    def __init__(self):
        WINDOW_SIZE = "1920,1080"
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("--window-size=%s" % WINDOW_SIZE)
        self.instance = webdriver.Chrome(executable_path='/Users/jonathan/Downloads/chromedriver', chrome_options=options)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL is not valid!")

    def make_screenshot(self, filename):
        self.instance.save_screenshot(filename)