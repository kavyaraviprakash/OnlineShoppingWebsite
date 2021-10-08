import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class class_login(unittest.TestCase):
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
        time.sleep(3)
        elem = driver.find_element_by_id("userMenu")
        elem.click()
        time.sleep(3)
        try:
            # attempt to find the 'logout' - if found, logged in
            logout_link = driver.find_element_by_xpath("/html/body/nav/div/div/ul/li/div/a[2]").text
            if "Log Out" in logout_link:
                print("User Successfully logged in")
                assert True
            else:
                assert False

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        driver.quit()


@classmethod
def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
