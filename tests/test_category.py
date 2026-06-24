from pages.login_page import LoginPage
from pages.category_page import CategoryPage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে category create
# ══════════════════════════════════════════════
def test_add_category(login: LoginPage, product: str):
    category_page = CategoryPage(login.page)

    category_name = "BananaRepublic"
    category_page.add_category(category_name)

    login.page.wait_for_timeout(10000)
    category_page.assert_category_in_list(category_name)


# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic category create
# ══════════════════════════════════════════════
def test_add_category_faker(login: LoginPage, product: str, fake):
    category_page = CategoryPage(login.page)

    category_name = fake.word()
    category_page.add_category(category_name)

    login.page.wait_for_timeout(10000)
    category_page.assert_category_in_list(category_name)
