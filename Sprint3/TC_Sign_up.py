import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Sign_Up(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://smoorthi.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/form/a[2]")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[1]/input")
        elem.send_keys("testuser1")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[2]/input")
        elem.send_keys("kavyaravi39@gmail.com")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[3]/input")
        elem.send_keys("Abcde@123")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[4]/input")
        elem.send_keys("Abcde@123")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[5]/input")
        elem.click()
        time.sleep(5)

        # Sucess_login
        driver.get("http://smoorthi.pythonanywhere.com/accounts/login/")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
