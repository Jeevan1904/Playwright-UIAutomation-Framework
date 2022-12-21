
from page_objects.home_page import HomePage


class LoginPageRedirect:
    def __init__(self, page) -> None:
        self.page = page
        self.user_name_inputbox = page.get_by_label("Email")
        self.password_inputbox = page.get_by_label("Password")
        self.remember_me_checkbox = page.get_by_label("Remember me")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

    def sign_in_action(self, credentials):
        self.user_name_inputbox.fill(credentials['user_name'])
        self.password_inputbox.fill(credentials['password'])
        self.remember_me_checkbox.check()
        self.sign_in_button.click()
        return HomePage