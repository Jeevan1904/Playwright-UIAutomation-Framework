from playwright.sync_api import Playwright, expect

from page_objects.login.login_page import LoginPage

#from page_objects.login.login_page import LoginPage
#from page_objects.login import login_page

def test_login(page):
    browser = Playwright.chromium.launch(headless=False, slowmo = 1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    login_page_object = LoginPage(page)
    login_page_redirect_object = login_page_object.redirect_to_login_form() 
    credentials = {'user_name':'wsc-dev@gridos.com', 'password':'0pusOne'}
    login_page_redirect_object.sign_in_action(credentials)
    expect(page)