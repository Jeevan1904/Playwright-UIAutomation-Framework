from page_objects.create_program import CreateProgram


class HeaderPage:
    def __init__(self, page) -> None:
        self.page = page
        self.hamburger_open_button = page.locator(".button")
        self.hamburger_close_button = page.locator(".navigation__scroll-container > button")
        self.program_specifics_text = page.get_by_role("heading", name="Program specifics")
        self.dashboard_button = page.get_by_role("link", name="Dashboard") 
        self.map_link = page.get_by_role("link", name="Map")
        self.auction_management_text = page.get_by_text("Auction management")
        self.requests_and_responses_link = page.get_by_role("link", name="Requests and Responses")
        self.contracts_link = page.get_by_role("link", name="Contracts")
        self.market_schedules_link = page.get_by_role("link", name="Market schedules")
        self.settlements_link = page.get_by_role("link", name="Settlements")
        self.reports_link = page.get_by_role("link", name="Reports")
        self.feeders_link = page.get_by_role("link", name="Feeders")
        self.settings_link = page.get_by_role("link", name="Settings")
        self.utilization_settings_link = page.get_by_role("link", name="Utilisation Settings")
        self.measurements_link = page.get_by_role("link", name="Measurements")
        self.create_program_link = page.get_by_role("link", name="Create Program")
        self.admin_panel_link = page.get_by_role("link", name="Admin Panel")
        self.account_settings_link = page.get_by_text("Account settings")
        self.user_manual_link = page.get_by_role("link", name="User manual")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")
        self.report_an_issue_link = page.get_by_role("link", name="Report an issue")
        self.version_text = page.get_by_text("master")
        self.logout_button = page.get_by_role("button", name="Logout")
        self.program_selection_dropdown = page.locator(".css-8mmkcg")

    
    def navigate_to_create_program_page(self):
        self.hamburger_open_button.first.click()
        self.create_program_link.click()
        return CreateProgram(self.page)


 
    