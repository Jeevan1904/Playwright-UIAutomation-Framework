import pytest
from page_objects.home_page import HomePage

@pytest.fixture()
def setup_teardown(page)->None:
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    #page.get_by_role("button", name="Login").click()
    #page.get_by_label("Email").click()
    #page.get_by_label("Email").fill("wsc-dev@gridos.com")
    #page.get_by_label("Email").press("Tab")
    #page.get_by_label("Password").fill("0pusOne")
    #page.get_by_label("Password").press("Enter")
    yield page
    


@pytest.fixture()
def login(page):
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("wsc-dev@gridos.com")
    page.get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("0pusOne")
    page.get_by_label("Password").press("Enter")
    yield page
    