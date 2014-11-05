import unittest
import time
from selenium import webdriver

class GHomePage(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://www.google.com/"

    def g_homepage(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.logo = self.driver.find_element_by_xpath('//*[@id="hplogo"]').get_attribute("alt")
        self.current_url = self.driver.current_url

class LPTests(unittest.TestCase):

    def setUp(self):
        self.page = GHomePage()
        self.page.g_homepage()

    def test_page_address(self):
        self.assertEqual(self.page.url, str(self.page.current_url))

    def test_logo_alt(self):
        self.assertEqual(self.page.logo, "Google")

    def tearDown(self):
        self.page.driver.close()

def main():
    unittest.main()

if __name__ == '__main__':
    main()

