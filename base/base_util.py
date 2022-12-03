import unittest

from selenium import webdriver


class BaseUtil(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        self.driver = webdriver.Firefox()
        driver = self.driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")

    def tearDown(self) -> None:
        pass


