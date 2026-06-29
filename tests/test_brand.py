from pages.login_page import LoginPage
from pages.brand_page import BrandPage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে brand create
# ══════════════════════════════════════════════
def test_add_brand(login: LoginPage):
    brand_page = BrandPage(login.page)

    brand_name = "Nike"

    brand_page.add_brand(brand_name)
    login.page.wait_for_timeout(3000)
    brand_page.assert_brand_in_list(brand_name)


# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic brand create
# ══════════════════════════════════════════════
def test_add_brand_faker(login: LoginPage, fake):
    brand_page = BrandPage(login.page)

    brand_name = fake.company()

    brand_page.add_brand(brand_name)
    login.page.wait_for_timeout(3000)
    brand_page.assert_brand_in_list(brand_name)