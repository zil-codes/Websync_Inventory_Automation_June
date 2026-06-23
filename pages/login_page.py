from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://dev.moinorrashid.com/login"

    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.sign_in_heading = page.get_by_role("heading", name="Sign In")
        self.error_message = page.get_by_text("Invalid email or password")
        self.user_menu_button = page.locator("#user-menu-button-2")
        self.logout_button = page.get_by_role("button", name="Logout")

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_dashboard_visible(self):
        expect(self.dashboard_heading).to_be_visible()

    def assert_dashboard_not_visible(self):
        expect(self.dashboard_heading).not_to_be_visible()

    def assert_error_message_visible(self):
        expect(self.error_message).to_be_visible()

    def assert_sign_in_visible(self):
        expect(self.sign_in_heading).to_be_visible()

    def logout(self):
        self.user_menu_button.click()
        self.logout_button.click()
