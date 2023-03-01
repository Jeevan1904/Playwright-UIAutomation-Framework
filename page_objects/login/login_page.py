from page_objects.login.login_page_redirect import LoginPageRedirect

class LoginPage:
    
    def __init__(self, page) -> None:
        self.page = page
        self.login_button = page.get_by_role("button", name="Login")

    def redirect_to_login_form(self):
        self.login_button.click()
        return LoginPageRedirect(self.page)