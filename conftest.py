import pytest
from playwright.sync_api import Page, expect
from faker import Faker
from pages.login_page import LoginPage

BASE_URL = "https://dev.moinorrashid.com"
VALID_EMAIL = "sm.trading.jess@gmail.com"
VALID_PASSWORD = "smtradding2024"


# ─────────────────────────────────────────────
# Faker
# ─────────────────────────────────────────────
@pytest.fixture
def fake():
    return Faker()


# ─────────────────────────────────────────────
# Login fixture — returns LoginPage object
# ─────────────────────────────────────────────
@pytest.fixture
def login(page: Page) -> LoginPage:
    page.set_default_navigation_timeout(60000)
    page.set_default_timeout(20000)

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    login_page.assert_dashboard_visible()

    return login_page  # ← LoginPage object return করছে


# ─────────────────────────────────────────────
# Brand fixture — LoginPage এর page attribute ব্যবহার করে
# ─────────────────────────────────────────────
@pytest.fixture
def created_brand(login: LoginPage, fake: Faker) -> str:
    page = login.page

    page.goto(BASE_URL)
    page.get_by_role("button", name="Products").click()
    page.get_by_role("link", name="Products Brands").click()
    page.get_by_role("button", name="Add Brand").click()

    brand_name = fake.company()
    page.get_by_placeholder("Enter name").fill(brand_name)
    page.get_by_role("button", name="Submit").click()
    page.wait_for_timeout(3000)

    return brand_name


# ─────────────────────────────────────────────
# Category fixture
# ─────────────────────────────────────────────
@pytest.fixture
def created_category(login: LoginPage, fake: Faker) -> str:
    page = login.page

    page.goto(BASE_URL)
    page.get_by_role("button", name="Products").click()
    page.get_by_role("link", name="Products Category").click()
    page.get_by_role("button", name="Add Category").click()

    category_name = fake.word()
    page.get_by_placeholder("Enter name").fill(category_name)
    page.get_by_role("button", name="Submit").click()
    page.wait_for_timeout(3000)

    return category_name


# ─────────────────────────────────────────────
# URL fixtures
# ─────────────────────────────────────────────
@pytest.fixture
def product():
    return BASE_URL


@pytest.fixture
def purchase():
    return BASE_URL
