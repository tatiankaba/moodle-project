import pytest
from selenium import webdriver
from .pages.register_page import *
from .pages.links import AllLinks
url = "http://demowebshop.tricentis.com"

@pytest.mark.parametrize('gender', [RegisterPageLocators.radio_btn_female, RegisterPageLocators.radio_btn_male])
def test_user_is_successfully_registered(browser,gender):
   link = AllLinks.register_url
   page = RegisterPage(browser,link)
   page.open()
   page.register_new_user(gender)
   page.register_msg_success()



