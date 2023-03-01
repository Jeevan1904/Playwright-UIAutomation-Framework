from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/")
    page.goto("https://transition-wsc-dev.vpn.opusonesolutions.com/login")
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("wsc-dev.gridos.com")
    page.get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("0pusOne")
    page.get_by_role("button", name="Sign In").click()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
