
from page_objects.home_page import HomePage


class LoginPageRedirect:
    def __init__(self, page) -> None:
        self.page = page
        self.user_name_inputbox = page.get_by_label("Email")
        self.password_inputbox = page.get_by_label("Password")
        self.remember_me_checkbox = page.get_by_label("Remember me")
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.input_error = page.get_by_text("Invalid username or password.")


    def enter_username(self, user_name):
        self.user_name_inputbox.clear()
        self.user_name_inputbox.fill(user_name)

    def enter_password(self, password):
        self.password_inputbox.clear()
        self.password_inputbox.fill(password)

    def sign_in_action(self, credentials):
        self.enter_username(user_name=credentials['user_name'])
        self.enter_password(password=credentials['password'])
        self.sign_in_button.click()
        return HomePage