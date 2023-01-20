
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep


class Sign_up_page(Base_page):
    SIGN_UP_BTN = (By.XPATH,"//a[@class='jss17 jss19']")
    FIELDS = (By.XPATH, "//input[@type='text']")
    PERSONAL_BTN = (By.CSS_SELECTOR, "input[value='personal']")
    SELECT_ACCOUNT_CONTINUE_BTN = (By.XPATH, '//button[@data-test-id="select-account-continue-btn"]')
    FIRST_NAME_CONTINUE_BTN = (By.XPATH, '//button[@data-test-id="first-name-continue-btn"]')
    LAST_NAME_CONTINUE_BTN = (By.XPATH, '//button[@data-test-id="last-name-continue-btn"]')
    WRONG_EMAIL_TEXT = (By.CSS_SELECTOR, ".MuiFormHelperText-root.MuiFormHelperText-contained.MuiFormHelperText-filled")



    def navigate_sign_up_page(self):
        self.driver.find_element(*self.SIGN_UP_BTN).click()

    def click_personal_button(self):
        self.driver.find_element(*self.PERSONAL_BTN).click()

    def click_continue_button(self):
        sleep(2)
        self.driver.find_element(*self.SELECT_ACCOUNT_CONTINUE_BTN).click()

    def input_first_name(self,name):
        self.driver.find_element(*self.FIELDS).send_keys(name)

    def click_continue_first_name_button(self):
        self.driver.find_element(*self.FIRST_NAME_CONTINUE_BTN).click()

    def input_last_name(self,last_name):
        self.driver.find_element(*self.FIELDS).send_keys(last_name)

    def click_last_name_continue_button(self):
        self.chrome.find_element(*self.LAST_NAME_CONTINUE_BTN).click()

    def input_email(self,email):
        self.driver.find_element(*self.FIELDS).send_keys(email)

    def check_error_message_email(self):
        expected = 'Please enter a valid email address'
        actual = self.driver.find_element(*self.WRONG_EMAIL_TEXT)
        self.assert expected == actual,'the error is different'

