import unittest

import time

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("java_beforMethod")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("java_afterMethod")
        time.sleep(6)
        self.driver.quit()
