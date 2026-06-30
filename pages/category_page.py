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
        self.page.goto(f"{BASE_URL}/products/category")
        self.page.wait_for_load_state("networkidle")

    # ── Actions ───────────────────────────────
    def fill_name(self, name: str):
        self.name_input.fill(name)

    def submit(self):
        # Category create API response actively capture করো
        with self.page.expect_response(
            lambda r: "/api/v1/cate" in r.url and r.request.method == "POST",
            timeout=20000,
        ) as resp_info:
            self.submit_button.click()

        resp = resp_info.value
        assert resp.status in (200, 201), (
            f"❌ Category create API failed! Status: {resp.status}, "
            f"Body: {resp.text()}"
        )
        self.page.wait_for_load_state("networkidle")

    # ── Full flow ─────────────────────────────
    def add_category(self, name: str):
        self.navigate()
        self.add_category_button.click()
        self.fill_name(name)
        self.submit()

    # ── Assert ────────────────────────────────
    def assert_category_in_list(self, name: str):
        self.page.wait_for_load_state("networkidle")

        # Search box দিয়ে filter করো — customer page এর মতো
        search_box = self.page.get_by_placeholder("Search here..")
        search_box.wait_for(state="visible", timeout=10000)
        search_box.click()
        search_box.press_sequentially(name, delay=80)

        # Search API response আসা পর্যন্ত wait করো
        self.page.wait_for_load_state("networkidle")

        # Table row এ matching name খোঁজো
        rows = self.page.locator("table tbody tr")
        matching_row = rows.filter(has_text=name)
        expect(matching_row.first).to_be_visible(timeout=15000)

        print(f"✅ Category '{name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")