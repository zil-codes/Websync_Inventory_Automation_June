import pytest
from playwright.sync_api import Page, expect
from faker import Faker


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def created_brand(login, fake):
    """Brand তৈরি করে নাম return করে"""
    login.goto("https://dev.moinorrashid.com/")
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Products Brands").click()
    login.get_by_role("button", name="Add Brand").click()

    brand_name = fake.company()
    login.get_by_placeholder("Enter name").fill(brand_name)
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(3000)

    return brand_name  # ← নামটা return করছে


@pytest.fixture
def created_category(login, fake):
    """Category তৈরি করে নাম return করে"""
    login.goto("https://dev.moinorrashid.com/")
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Products Category").click()
    login.get_by_role("button", name="Add Category").click()

    category_name = fake.word()
    login.get_by_placeholder("Enter name").fill(category_name)
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(3000)

    return category_name  # ← নামটা return করছে


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