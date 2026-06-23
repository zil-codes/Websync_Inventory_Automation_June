import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage  # underscore দিয়ে


# ──────────────────────────────────────────────
# TC-001: Valid credential login
# ──────────────────────────────────────────────
def test_login_valid_credential(login: LoginPage):
    # login fixture already logged in — just assert Dashboard
    login.assert_dashboard_visible()
    login.page.wait_for_timeout(10000)


# ──────────────────────────────────────────────
# TC-002: Invalid credential login
# ──────────────────────────────────────────────
def test_login_invalid_credential(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("sm.trading.jess@gmail.com", "wrongpassword")

    login_page.assert_dashboard_not_visible()
    login_page.assert_error_message_visible()
    page.wait_for_timeout(10000)


# ──────────────────────────────────────────────
# TC-003: Logout
# ──────────────────────────────────────────────
def test_login_logout(login: LoginPage):
    login.logout()
    login.assert_sign_in_visible()
    login.page.wait_for_timeout(10000)

