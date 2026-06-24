from playwright.sync_api import Page, expect

BASE_URL = "https://dev.moinorrashid.com"


class AddProductPage:

    def __init__(self, page: Page):
        self.page = page

        # ── Navigation ──
        self.products_menu_button = page.get_by_role("button", name="Products")
        self.add_products_link = page.get_by_role("link", name="Add Products")

        # ── Form fields ──
        self.name_input = page.get_by_placeholder("Enter name")
        self.product_code_input = page.get_by_placeholder("Enter Product Code")
        self.description_input = page.get_by_placeholder("Enter Description")
        self.purchase_price_input = page.locator('input[name="purchasePrice"]')
        self.sale_price_input = page.locator('input[name="basePrice"]')

        # ── Dropdowns ──
        self.category_combobox = (
            page.locator("input[name='category']")
            .locator("xpath=../..//input[@role='combobox']")
        )
        self.brand_combobox = (
            page.locator("input[name='brand']")
            .locator("xpath=../..//input[@role='combobox']")
        )

        # ── Buttons ──
        self.submit_button = page.get_by_role("button", name="Submit")

    # ── Navigate ──────────────────────────────────────────
    def navigate(self):
        self.page.goto(BASE_URL)
        self.products_menu_button.click()
        self.add_products_link.click()

    # ── Fill fields ───────────────────────────────────────
    def fill_name(self, name: str):
        self.name_input.fill(name)

    def fill_product_code(self, code: str):
        self.product_code_input.fill(code)

    def fill_description(self, description: str):
        self.description_input.fill(description)

    def fill_purchase_price(self, price: str):
        self.purchase_price_input.fill(price)

    def fill_sale_price(self, price: str):
        self.sale_price_input.fill(price)

    def select_category(self, category_name: str, use_last: bool = False):
        self.category_combobox.click()
        self.page.get_by_role("option").first.wait_for(state="visible")
        option = self.page.get_by_role("option", name=category_name, exact=True)
        if use_last:
            option.last.click()
        else:
            option.first.click()

    def select_brand(self, brand_name: str, use_last: bool = False):
        self.brand_combobox.click()
        self.page.get_by_role("option").first.wait_for(state="visible")
        option = self.page.get_by_role("option", name=brand_name, exact=True)
        if use_last:
            option.last.click()
        else:
            option.first.click()

    def submit(self):
        self.submit_button.click()

    # ── Assert: Product list এ আছে কিনা ──────────────────
    def assert_product_in_list(self, product_name: str):
        self.page.goto(f"{BASE_URL}/products?limit=10&page=1")
        self.page.wait_for_timeout(2000)
        product_in_list = self.page.get_by_text(product_name, exact=True).first
        expect(product_in_list).to_be_visible()
        print(f"✅ Product '{product_name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")

    # ── Full flow: Static data ─────────────────────────────
    def create_product(
        self,
        name: str,
        category: str,
        brand: str,
        purchase_price: str,
        sale_price: str,
        product_code: str,
        description: str = "",
        use_last: bool = False,
    ):
        self.navigate()
        self.fill_name(name)
        self.select_category(category, use_last=use_last)
        self.select_brand(brand, use_last=use_last)
        self.fill_purchase_price(purchase_price)
        self.fill_sale_price(sale_price)
        self.fill_product_code(product_code)
        if description:
            self.fill_description(description)
        self.submit()
