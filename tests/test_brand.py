#
# def test_add_brand(login, product):
#     login.goto(product)
#     login.get_by_role("button", name="Products").click()
#     login.get_by_role("link", name="Products Brands").click()
#     login.get_by_role("button", name="Add Brand").click()
#     login.get_by_placeholder("Enter name").fill("Gucci")
#     login.get_by_role("button", name="Submit").click()
#     login.wait_for_timeout(10000)

# def test_add_brand(login, product, fake):
#     login.goto(product)
#     login.get_by_role("button", name="Products").click()
#     login.get_by_role("link", name="Products Brands").click()
#     login.get_by_role("button", name="Add Brand").click()
#
#     # ---- Brand name (Faker দিয়ে dynamic) ----
#     brand_name = fake.company()
#     login.get_by_placeholder("Enter name").fill(brand_name)
#
#     login.get_by_role("button", name="Submit").click()
#     login.wait_for_timeout(10000)

from pages.login_page import LoginPage
from pages.brand_page import BrandPage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে brand create
# ══════════════════════════════════════════════
def test_add_brand(login: LoginPage, product: str):
    brand_page = BrandPage(login.page)

    brand_name = "polo"
    brand_page.add_brand(brand_name)

    login.page.wait_for_timeout(10000)
    brand_page.assert_brand_in_list(brand_name)


# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic brand create
# ══════════════════════════════════════════════
def test_add_brand_faker(login: LoginPage, product: str, fake):
    brand_page = BrandPage(login.page)

    brand_name = fake.company()
    brand_page.add_brand(brand_name)

    login.page.wait_for_timeout(10000)
    brand_page.assert_brand_in_list(brand_name)
