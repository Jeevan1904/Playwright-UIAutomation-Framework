import pytest
from playwright.sync_api import Playwright, expect, Page

from page_objects.login.login_page import LoginPage
from page_objects.login.login_page_redirect import LoginPageRedirect
from page_objects.home_page import HomePage

#from page_objects.login.login_page import LoginPage
#from page_objects.login import login_page

# uses setup_teardown fixture from conftest.py
# POM implementation in place
# custom marker 'sanity' defined in pytest.ini
@pytest.mark.sanity
def test_valid_login(setup_teardown):
    page = setup_teardown
    #page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    login_page_object = LoginPage(page)
    login_page_redirect_object = login_page_object.redirect_to_login_form() 
    cred = {'user_name':'wsc-dev@gridos.com', 'password':'0pusOne'}
    home_page=login_page_redirect_object.sign_in_action(cred)
    print(page.title())
    expect(page).to_have_title("GridOS TE")



@pytest.mark.sanity
def test_login(login):
    page = login
    expect(page).to_have_title("GridOS TE")

@pytest.mark.sanity
@pytest.mark.parametrize("cred", [{'user_name':'wsc-dev@gridos.com', 'password':'0pusOne'}, {'user_name':'wsc-dev1@gridos.com', 'password':'0pusOne'}])
def test_valid_login_2(page, cred):
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    login_page_object = LoginPage(page)
    login_page_redirect_object = login_page_object.redirect_to_login_form() 
    #cred = {'user_name':'wsc-dev@gridos.com', 'password':'0pusOne'}
    home_page=login_page_redirect_object.sign_in_action(cred)
    print(page.title())
    expect(page).to_have_title("GridOS TE")
    assert page.to

    
    
@pytest.mark.sanity
def test_invalid_login(setup_teardown) -> None:
    page = setup_teardown
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    login_page_object = LoginPage(page)
    page.screenshot(path="")
    login_page_redirect_object = login_page_object.redirect_to_login_form()
    credentials = {'user_name':'invalid-user@gridos.com', 'password':'0pusOne'}
    login_page_redirect_object.sign_in_action(credentials)
   
