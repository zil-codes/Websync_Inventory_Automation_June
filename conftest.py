import pytest
from playwright.sync_api import Page,expect

@pytest.fixture
def login(page: Page):
    page.set_default_navigation_timeout(60000)
    page.goto("https://dev.moinorrashid.com/login", wait_until="commit")
    page.set_default_timeout(20000)
    page.locator("#email").fill("sm.trading.jess@gmail.com")
    page.locator("#password").fill("smtradding2024")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    return page



@pytest.fixture
def product():
    return "https://dev.moinorrashid.com/"
