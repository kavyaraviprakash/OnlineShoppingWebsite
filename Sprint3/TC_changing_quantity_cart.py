import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Class_change_qty(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_onyx(self):
        user = "smoorthi"
        pwd = "swethacse"
        homepage = "http://smoorthi.pythonanywhere.com/"

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
        # adding product1 to the cart
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/button")
        elem.click()
        time.sleep(3)
        # adding product2 to the cart
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/button")
        elem.click()
        time.sleep(3)
        # Selecting cart icon from the navigation page
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/a/img")
        elem.click()
        time.sleep(3)
        # Collecting the initial count of products in the cart
        before_count = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/table/tbody/tr/th[1]/h5/strong").text
        # Selecting the quantity increase button of the items in the cart
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[4]/div/img[1]")
        elem.click()
        time.sleep(3)
        # Collecting the final count of products in the cart after increasing
        after_count = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/table/tbody/tr/th[1]/h5/strong").text
        # Verifying if the products increased
        if int(before_count)+1 == int(after_count):
            print("Item increased Verified")
            assert True
        else:
            print("Item is not increased")
            assert False
        # Now Decreasing the count of product by 2
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[4]/div/img[2]")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[4]/div/img[2]")
        elem.click()
        time.sleep(3)
        # Collecting the final count of products in the cart after decreasing
        after_count = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/table/tbody/tr/th[1]/h5/strong").text
        # Verifying if the products decreased
        if int(before_count)-1 == int(after_count):
            print("Item Decreased Verified")
            assert True
        else:
            print("Item is not Decreased")
            assert False
        # Navigation to continue shopping
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/a")
        elem.click()
        time.sleep(3)
        elem = driver.current_url
        if elem == homepage:
            print("Continue button on Cart page Navigated user back to Home Page Verified")
            assert True
        else:
            print("User is not navigated to HomePage as expected.Instead navigated to" + elem)
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
