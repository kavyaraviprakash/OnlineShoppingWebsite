import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Class_Navbar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_onyx(self):
        user = "testuser"
        pwd = "Abcdef@123"
        # Login Page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://smoorthi.pythonanywhere.com/login/")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[1]/input")
        elem.send_keys(user)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[2]/input")
        elem.send_keys(pwd)
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[3]/input")
        elem.click()
        time.sleep(5)
        # Navigation to About Us page
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[2]/a")
        elem.click()
        time.sleep(3)
        driver.get("http://smoorthi.pythonanywhere.com/about/")
        # Navigation to Contact Page
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[3]/a")
        elem.click()
        time.sleep(3)
        driver.get("http://smoorthi.pythonanywhere.com/contact/")
        # Navigation to Store Page
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul/li[1]/a")
        elem.click()
        time.sleep(3)
        # Navigation to Change Password
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li/div/a[1]")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[1]/input")
        elem.send_keys("Abcdef@123")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[2]/input")
        elem.send_keys("Abcd@123")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/fieldset/div[3]/input")
        elem.send_keys("Abcd@123")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/form/div/div/input")
        elem.click()
        time.sleep(3)
        # Navigation to logout page
        driver.get("http://smoorthi.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li/div/a[2]")
        elem.click()
        time.sleep(3)
        # Redirect to homepage
        driver.get("http://smoorthi.pythonanywhere.com/")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
