# from playwright.sync_api import expect
#
# def test_create_Product(login, product):
#     login.goto(product)
#     login.get_by_role("button", name="Products").click()
#     login.get_by_role("link", name="Add Products").click()
#
#     # ---- Product name ----
#     product_name = "Jasmin"
#     login.get_by_placeholder("Enter name").fill(product_name)
#
#     # ---- Category select ----
#     login.locator("input[name='category']").locator("xpath=../..//input[@role='combobox']").click()
#     login.get_by_role("option").first.wait_for(state="visible")
#     login.get_by_role("option", name="Perfume", exact=True).first.click()
#
#     # ---- Brand select ----
#     login.locator("input[name='brand']").locator("xpath=../..//input[@role='combobox']").click()
#     login.get_by_role("option").first.wait_for(state="visible")
#     login.get_by_role("option", name="Dior", exact=True).first.click()
#
#     # ---- Purchase Price ----
#     login.locator('input[name="purchasePrice"]').fill("500")
#
#     # ---- Sale Price ----
#     login.locator('input[name="basePrice"]').fill("600")
#
#     # ---- Product Code ----
#     login.get_by_placeholder("Enter Product Code").fill("PRD-0001")
#
#     # ---- Description ----
#     login.get_by_placeholder("Enter Description").fill("This is a test product description")
#
#     # ---- Submit ----
#     login.get_by_role("button", name="Submit").click()
#     login.wait_for_timeout(3000)
#
#     # ---- Assert: Product List এ আছে কিনা দেখো ----
#     login.goto("https://dev.moinorrashid.com/products?limit=10&page=1")
#     login.wait_for_timeout(2000)
#
#     product_in_list = login.get_by_text(product_name, exact=True).first
#     expect(product_in_list).to_be_visible()
#     print(f"✅ Product '{product_name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")
# # FAKER
#
# # def test_create_Product(login, product, fake, created_brand, created_category):
# #     login.goto(product)
# #     login.get_by_role("button", name="Products").click()
# #     login.get_by_role("link", name="Add Products").click()
# #
# #     # ---- Product name ----
# #     product_name = fake.word()
# #     login.get_by_placeholder("Enter name").fill(product_name)
# #
# #     # ---- Category select ----
# #     login.locator("input[name='category']").locator("xpath=../..//input[@role='combobox']").click()
# #     login.get_by_role("option").first.wait_for(state="visible")
# #     login.get_by_role("option", name=created_category, exact=True).last.click()
# #
# #     # ---- Brand select ----
# #     login.locator("input[name='brand']").locator("xpath=../..//input[@role='combobox']").click()
# #     login.get_by_role("option").first.wait_for(state="visible")
# #     login.get_by_role("option", name=created_brand, exact=True).last.click()
# #
# #     # ---- Purchase Price ----
# #     price = fake.random_int(min=100, max=5000)
# #     login.locator('input[name="purchasePrice"]').fill(str(price))
# #
# #     # ---- Sale Price ----
# #     sale_price = fake.random_int(min=100, max=5000)
# #     login.locator('input[name="basePrice"]').fill(str(sale_price))
# #
# #     # ---- Product Code ----
# #     product_code = fake.bothify(text='PRD-####')
# #     login.get_by_placeholder("Enter Product Code").fill(product_code)
# #
# #     # ---- Description ----
# #     description = fake.sentence()
# #     login.get_by_placeholder("Enter Description").fill(description)
# #
# #     login.wait_for_timeout(5000)
# #----------------------------
#
#
#
#
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.add_product_page import AddProductPage


# ══════════════════════════════════════════════════════
# TC-001: Static data দিয়ে product create
# ══════════════════════════════════════════════════════
def test_create_Product(login: LoginPage, product: str):
    add_product = AddProductPage(login.page)

    product_name = "Moringa"

    add_product.create_product(
        name=product_name,
        category="Perfume",
        brand="Dior",
        purchase_price="500",
        sale_price="600",
        product_code="PRD-0001",
        description="This is a test product description",
    )

    login.page.wait_for_timeout(3000)
    add_product.assert_product_in_list(product_name)


# ══════════════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic product create
# (created_brand + created_category fixture use করে)
# ══════════════════════════════════════════════════════
# def test_create_Product_faker(
#     login: LoginPage,
#     product: str,
#     fake,
#     created_brand: str,
#     created_category: str,
# ):
#     add_product = AddProductPage(login.page)
#
#     product_name = fake.word()
#     purchase_price = str(fake.random_int(min=100, max=5000))
#     sale_price = str(fake.random_int(min=100, max=5000))
#     product_code = fake.bothify(text="PRD-####")
#     description = fake.sentence()
#
#     add_product.create_product(
#         name=product_name,
#         category=created_category,
#         brand=created_brand,
#         purchase_price=purchase_price,
#         sale_price=sale_price,
#         product_code=product_code,
#         description=description,
#         use_last=True,  # faker এ newly created option শেষে থাকে
#     )
#
#     login.page.wait_for_timeout(5000)
#     add_product.assert_product_in_list(product_name)
