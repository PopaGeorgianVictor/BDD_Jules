
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep


class Sign_up_page(Base_page):
    SIGN_UP_BTN = (By.ID,'sign-up-link')
    PERSONAL_BTN = (By.CSS_SELECTOR, "input[value='personal']")
    CONTINUE_BTN = (By.XPATH, "//span[contains(text(),'CONTINUE')]")
    FIRST_NAME = (By.XPATH, "//input[@type='text']")
    FIRST_NAME_CONTINUE_BTN = (By.XPATH, '//button[@data-test-id="first-name-continue-btn"]')
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Type your answer here...']")
    LAST_NAME_CONTINUE_BTN = (By.CSS_SELECTOR,".jss49 > span:nth-child(1)")



    def navigate_sign_up_page(self):
        self.driver.find_element(*self.SIGN_UP_BTN).click()

    def click_personal_button(self):
        self.driver.find_element(*self.PERSONAL_BTN).click()

    def click_continue_button(self):
        sleep(2)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def input_first_name(self,name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(name)

    def click_continue_first_name_button(self):
        self.driver.find_element(*self.FIRST_NAME_CONTINUE_BTN).click()

    def input_last_name(self,last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def click_last_name_continue_button(self):
        self.chrome.find_element(*self.LAST_NAME_CONTINUE_BTN).click()

    def input_email(self,email):
        self.driver.find_element(*self.LAST_NAME).send_keys(email)

    def check_error_message_email(self):
        expected = 'Please enter a valid email address'
        actual = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')
        self.assertEqual(expected,actual,'the error is different')

    def click_sign_up_button(self):
        self.driver.find_element(*self.SIGN_UP).click()