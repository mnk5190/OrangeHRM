import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
#import HTMLTestRunner
#import HtmlTestRunner
#from HtmlTestRunner import HTMLTestRunner
from Pages.homePage import HomePage
from Pages.LoginPage import LoginPage

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/khan/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        """
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//a[@id='welcome']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        """

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
