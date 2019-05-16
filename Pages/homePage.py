class HomePage():
    def __init__(self, driver):
        self.driver = driver

        # These are the three locators on this page
        self.welcome_link_xpath = "//a[@id='welcome']"
        self.logout_button_xpath = "//input[@id='txtUsername']"


    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.self.welcome_link_xpath).click()


    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
