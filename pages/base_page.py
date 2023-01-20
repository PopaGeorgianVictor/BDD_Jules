from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class Base_page(Browser, unittest.TestCase):
    def wait_for_elem(self,by,selector):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((by,selector)))