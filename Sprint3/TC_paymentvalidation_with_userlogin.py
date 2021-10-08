import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Class_Payment_validation(unittest.TestCase):

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
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/img")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/button")
        time.sleep(3)
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/a/img")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/a/img")
        elem.click()
        time.sleep(3)
        #Checkout
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/table/tbody/tr/th[3]/a")
        elem.click()
        time.sleep(3)
        #passing the values by locating the particular field in shipping information
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/form/div[2]/div[1]/input")
        elem.send_keys("4155N_145th_Plaza, Apt 308")
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/form/div[2]/div[2]/input")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/form/div[2]/div[3]/input")
        elem.send_keys("NE")
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/form/div[2]/div[4]/input")
        elem.send_keys(68116)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/form/div[2]/div[5]/input")
        elem.send_keys("USA")
        time.sleep(3)
        elem = driver.find_element_by_id("form-button")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]")
        elem.click()
        time.sleep(5)
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        paypal_window_handle = None
        while not paypal_window_handle:
            for handle in driver.window_handles:
                if handle != main_window_handle:
                    paypal_window_handle = handle
                    break
        driver.switch_to.window(paypal_window_handle)
        time.sleep(3)
        elem = driver.find_element_by_id("email")
        elem.send_keys("swetha.moorthi@gmail.com")
        time.sleep(3)
        elem = driver.find_element_by_id("btnNext")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_id("password")
        elem.send_keys("SwetMs@21")
        elem = driver.find_element_by_id("btnLogin")
        elem.click()
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_id("acceptAllButton")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_id("paywith-tab-now")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_id("payment-submit-btn")
        elem.click()
        time.sleep(5)
        driver.switch_to.window(main_window_handle)
        alerts = driver.switch_to.alert.text
        if alerts == "Transaction completed":
            print("Transaction completed Successfully and Verified")
            assert True
        else:
            print(alerts + "is not as as per expected")
            assert False

        driver.quit()


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
