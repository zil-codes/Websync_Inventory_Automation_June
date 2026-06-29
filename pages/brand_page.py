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
        self.page.wait_for_load_state("networkidle")

    # ── Actions ───────────────────────────────
    def fill_name(self, name: str):
        self.name_input.fill(name)

    def submit(self):
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    # ── Full flow ─────────────────────────────
    def add_brand(self, name: str):
        self.navigate()
        self.add_brand_button.click()
        self.fill_name(name)
        self.submit()

    # ── Assert ────────────────────────────────
    def assert_brand_in_list(self, name: str):
        # Brand list এ navigate করো
        self.navigate()
        self.page.wait_for_timeout(2000)

        # Search করো
        search_box = self.page.get_by_placeholder("Search here..")
        search_box.wait_for(state="visible", timeout=10000)
        search_box.fill(name)
        self.page.wait_for_timeout(2000)

        # Table এ নাম খোঁজো — exact=True সরানো হয়েছে
        rows = self.page.locator("table tbody tr")
        row_count = rows.count()

        assert row_count > 0, f"কোনো row নেই! '{name}' পাওয়া যায়নি।"

        found = False
        for i in range(row_count):
            if name in rows.nth(i).inner_text():
                found = True
                break

        assert found, f"❌ '{name}' brand list এ নেই!"
        print(f"✅ Brand '{name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")