from .base_page import BasePage
from .locators import AuthorisationPageLocators
from .locators import RegisterPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .user import User
from .register_page import *

class AuthorisationPage(RegisterPage):
    def new_user_registered(self):
        radio_btn = self.browser.find_element(*RegisterPageLocators.radio_btn_male)
        radio_btn.click()
        first_name_field = self.browser.find_element(*RegisterPageLocators.first_name_field)  
        first_name_field.send_keys(User.first_name)
        last_name_field = self.browser.find_element(*RegisterPageLocators.last_name_field)
        last_name_field.send_keys(User.last_name)
        email_field = self.browser.find_element(*RegisterPageLocators.email_field)
        email_field.send_keys(User.email)
        password_field =  self.browser.find_element(*RegisterPageLocators.password_field)
        password_field.send_keys(User.password)
        confirm_password_field = self.browser.find_element(*RegisterPageLocators.confirm_password_field)
        confirm_password_field.send_keys(User.password)
        register_btn = self.browser.find_element(*RegisterPageLocators.register_button)
        register_btn.click()

    def existed_user_logged_in_successfully(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(User.password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.account_information), "The user hasn't been authorised"
        
        
    def right_email_wrong_password_login_failed(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(User.wrong_password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_unsuccessfull_login), "The error message is absent"
        error_message_unsuccessfull_login = self.browser.find_element(*AuthorisationPageLocators.error_message_unsuccessfull_login)
        assert error_message_unsuccessfull_login.text == 'Login was unsuccessful. Please correct the errors and try again.', "The error message is not correct"
        assert self.is_element_present(*AuthorisationPageLocators.error_message_wrong_credentials), "The error message about the wrong credentials is absent"
        error_message_wrong_credentials = self.browser.find_element(*AuthorisationPageLocators.error_message_wrong_credentials)
        assert error_message_wrong_credentials.text == 'The credentials provided are incorrect', "The error message about the wrong credentials is not correct"

    def wrong_email_right_password_login_failed(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.wrong_email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(User.password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_unsuccessfull_login), "The error message is absent"
        error_message_unsuccessfull_login = self.browser.find_element(*AuthorisationPageLocators.error_message_unsuccessfull_login)
        assert error_message_unsuccessfull_login.text == 'Login was unsuccessful. Please correct the errors and try again.', "The error message is not correct"
        assert self.is_element_present(*AuthorisationPageLocators.error_message_wrong_credentials), "The error message about the wrong credentials is absent"
        error_message_wrong_credentials = self.browser.find_element(*AuthorisationPageLocators.error_message_wrong_credentials)
        assert error_message_wrong_credentials.text == 'No customer account found', "The error message about the wrong credentials is not correct"

    def wrong_email_wrong_password_login_failed(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.wrong_email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys(User.wrong_password)
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_unsuccessfull_login), "The error message is absent"
        error_message_unsuccessfull_login = self.browser.find_element(*AuthorisationPageLocators.error_message_unsuccessfull_login)
        assert error_message_unsuccessfull_login.text == 'Login was unsuccessful. Please correct the errors and try again.', "The error message is not correct"
        assert self.is_element_present(*AuthorisationPageLocators.error_message_wrong_credentials), "The error message about the wrong credentials is absent"
        error_message_wrong_credentials = self.browser.find_element(*AuthorisationPageLocators.error_message_wrong_credentials)
        assert error_message_wrong_credentials.text == 'No customer account found', "The error message about the wrong credentials is not correct"

    def empty_fields_login_failed(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys('')       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.send_keys('')
        login_btn = self.browser.find_element(*AuthorisationPageLocators.log_in_btn)
        login_btn.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_unsuccessfull_login), "The error message is absent"
        error_message_unsuccessfull_login = self.browser.find_element(*AuthorisationPageLocators.error_message_unsuccessfull_login)
        assert error_message_unsuccessfull_login.text == 'Login was unsuccessful. Please correct the errors and try again.', "The error message is not correct"
        assert self.is_element_present(*AuthorisationPageLocators.error_message_wrong_credentials), "The error message about the wrong credentials is absent"
        error_message_wrong_credentials = self.browser.find_element(*AuthorisationPageLocators.error_message_wrong_credentials)
        assert error_message_wrong_credentials.text == 'No customer account found', "The error message about the wrong credentials is not correct"

    def error_msg_invalid_email_appeared(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.invalid_email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_invalid_email), "The error message about invalid email is absent"
        error_message_invalid_email = self.browser.find_element(*AuthorisationPageLocators.error_message_invalid_email)
        assert error_message_invalid_email.text == 'Please enter a valid email address.', "The error message about invalid email is not correct"

    def error_msg_invalid_email_disappeared(self):
        email_field = self.browser.find_element(*AuthorisationPageLocators.email_field)  
        email_field.send_keys(User.invalid_email)       
        password_field =  self.browser.find_element(*AuthorisationPageLocators.password_field)
        password_field.click()
        assert self.is_element_present(*AuthorisationPageLocators.error_message_invalid_email), "The error message about invalid email is absent"
        error_message_invalid_email = self.browser.find_element(*AuthorisationPageLocators.error_message_invalid_email)
        assert error_message_invalid_email.text == 'Please enter a valid email address.', "The error message about invalid email is not correct"
        email_field.clear()
        email_field.send_keys(User.email) 
        assert self.is_not_element_present(*AuthorisationPageLocators.error_message_invalid_email), "The error message about invalid email hasn't diasppeared"
        