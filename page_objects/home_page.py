from page_objects.header_page import HeaderPage


class HomePage:
    def __init__(self, page) -> None:
        self.page = page
        self.header_page = HeaderPage(page)

    def navigate_to_create_program(self):
        self.header_page.navigate_to_create_program_page()


