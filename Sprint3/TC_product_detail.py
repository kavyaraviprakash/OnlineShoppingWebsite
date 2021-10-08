import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Class_Product_Detail(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "smoorthi"
        pwd = "swethacse"

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
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/img")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/a")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/button")
        elem.click
        #assert "Logged into product detail page"
        try:
            # attempt to find the details of the selected product and attempt to select 'Dresses' Navigation
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/h2[2]/a")
           time.sleep(5)
           elem.click()
           time.sleep(5)
           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        driver.quit()


@classmethod
def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()