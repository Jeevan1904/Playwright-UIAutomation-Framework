import pytest
from playwright.sync_api import Playwright, expect, Page

from page_objects.login.login_page import LoginPage
from page_objects.login.login_page_redirect import LoginPageRedirect

#from page_objects.login.login_page import LoginPage
#from page_objects.login import login_page

def test_valid_login(page: Page):
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    login_page_object = LoginPage(page)
    login_page_redirect_object = login_page_object.redirect_to_login_form() 
    cred = {'user_name':'wsc-dev@gridos.com', 'password':'0pusOne'}
    login_page_redirect_object.sign_in_action(cred)
    
    
@pytest.mark.sanity
def test_invalid_login(page: Page) -> None:
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    login_page_object = LoginPage(page)
    login_page_redirect_object = login_page_object.redirect_to_login_form()
    credentials = {'user_name':'invalid-user@gridos.com', 'password':'0pusOne'}
    login_page_redirect_object.sign_in_action(credentials)
   
