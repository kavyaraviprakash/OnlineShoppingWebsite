import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Class_product_category(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_onyx(self):
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
        # Navigation to 'ALL' home page of Onyx
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[1]/a")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on 'ALL'
        driver.get("http://smoorthi.pythonanywhere.com/")
        # Navigation to 'Bottoms' Category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[2]/a")
        elem.click()
        time.sleep(3)
        #Open the below link when clicked on 'Bottoms':
        driver.get("http://smoorthi.pythonanywhere.com/bottoms/")
        # Navigation to 'Coats & Jackets' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[3]/a")
        elem.click()
        time.sleep(3)
        #Open the below link when clicked on Coats and Jackets category:
        driver.get("http://smoorthi.pythonanywhere.com/coats-jackets/")
        # Navigation to 'Dresses' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[4]/a")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on Dresses category:
        driver.get("http://smoorthi.pythonanywhere.com/dresses/")
        # Navigation to 'Jumpsuits and Rompers' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[5]/a")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on Jumpsuits and Rompers category:
        driver.get("http://smoorthi.pythonanywhere.com/jumpsuits-rompers/")
        # Navigation to 'Sarees and blouse ' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[7]/a")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on Sarees and blouse  category:
        driver.get("http://smoorthi.pythonanywhere.com/sarees/")
        # Navigation to ' Shirts,Tops and Tees' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[8]")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on Shirts,Tops and Tee category:
        driver.get("http://smoorthi.pythonanywhere.com/tops/")
        # Navigation to 'Sweaters & Cardigans' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[9]/a")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on Sweaters & Cardigans category:
        driver.get("http://smoorthi.pythonanywhere.com/sweaters/")
        # Navigation to 'Sweatshirts & Hoodies' category of Onyx
        driver.execute_script("window.scrollTo(0,200)")
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[10]/a")
        elem.click()
        time.sleep(3)
        # Open the below link when clicked on Sweatshirts & Hoodies category:
        driver.get("http://smoorthi.pythonanywhere.com/sweatshirts-hoodies/")

    @classmethod
    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
