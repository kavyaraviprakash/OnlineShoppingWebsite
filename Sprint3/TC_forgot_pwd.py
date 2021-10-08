import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Class_forgot_pwd(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_onyx(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://smoorthi.pythonanywhere.com/login/")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/a")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("kavyaravi39@gmail.com")
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/form/fieldset/input")
        elem.click()
        time.sleep(5)

        try:

            elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/h1").text
            if (elem == "Password reset sent"):
                print("Password Reset Sent page Verified")
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
