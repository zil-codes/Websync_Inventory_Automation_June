from playwright.sync_api import Page, expect

BASE_URL = "https://dev.moinorrashid.com"


class CategoryPage:

    def __init__(self, page: Page):
        self.page = page

        # ── Navigation ──
        self.products_menu_button = page.get_by_role("button", name="Products")
        self.products_category_link = page.get_by_role("link", name="Products Category")
        self.add_category_button = page.get_by_role("button", name="Add Category")

        # ── Form ──
        self.name_input = page.get_by_placeholder("Enter name")
        self.submit_button = page.get_by_role("button", name="Submit")

    # ── Navigate ──────────────────────────────
    def navigate(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.products_menu_button.click()
        self.products_category_link.click()
        self.page.wait_for_load_state("networkidle")

    # ── Actions ───────────────────────────────
    def fill_name(self, name: str):
        self.name_input.fill(name)

    def submit(self):
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")

    # ── Full flow ─────────────────────────────
    def add_category(self, name: str):
        self.navigate()
        self.add_category_button.click()
        self.fill_name(name)
        self.submit()

    # ── Assert ────────────────────────────────
    def assert_category_in_list(self, name: str):
        # Submit এর পর backend response/list refresh সম্পূর্ণ হওয়া পর্যন্ত wait করো
        self.page.wait_for_load_state("networkidle")

        locator = self.page.get_by_text(name, exact=True).first
        expect(locator).to_be_visible(timeout=15000)
        print(f"✅ Category '{name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")