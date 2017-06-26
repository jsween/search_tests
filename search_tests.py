import unittest
from selenium import webdriver

class SearchTest (unittest.TestCase):
    def setUp(self):
        # create a new firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to application homepage
        self.driver.get("http://demo-store.seleniumacademy.com/")