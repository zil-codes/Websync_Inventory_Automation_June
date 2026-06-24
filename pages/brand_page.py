from playwright.sync_api import Page, expect

BASE_URL = "https://dev.moinorrashid.com"


class BrandPage:

    def __init__(self, page: Page):
        self.page = page

        # ── Navigation ──
        self.products_menu_button = page.get_by_role("button", name="Products")
        self.products_brands_link = page.get_by_role("link", name="Products Brands")
        self.add_brand_button = page.get_by_role("button", name="Add Brand")

        # ── Form ──
        self.name_input = page.get_by_placeholder("Enter name")
        self.submit_button = page.get_by_role("button", name="Submit")

    # ── Navigate ──────────────────────────────
    def navigate(self):
        self.page.goto(BASE_URL)
        self.products_menu_button.click()
        self.products_brands_link.click()

    # ── Actions ───────────────────────────────
    def fill_name(self, name: str):
        self.name_input.fill(name)

    def submit(self):
        self.submit_button.click()

    # ── Full flow ─────────────────────────────
    def add_brand(self, name: str):
        self.navigate()
        self.add_brand_button.click()
        self.fill_name(name)
        self.submit()

    # ── Assert ────────────────────────────────
    def assert_brand_in_list(self, name: str):
        expect(self.page.get_by_text(name, exact=True).first).to_be_visible()
        print(f"✅ Brand '{name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")
