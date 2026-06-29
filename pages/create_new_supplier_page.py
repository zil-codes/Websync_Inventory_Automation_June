from playwright.sync_api import Page, expect

BASE_URL = "https://dev.moinorrashid.com"


class SupplierPage:

    def __init__(self, page: Page):
        self.page = page

    # ── /customer/add এ সরাসরি যাও ──────────
    def navigate_to_create(self):
        self.page.goto(f"{BASE_URL}/customer/add")
        self.page.wait_for_load_state("networkidle")

    # ── Supplier Create করো ───────────────────
    def create_supplier(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
        city: str,
        postal_code: str,
        customer_type: str,
    ):
        self.navigate_to_create()

        self.page.get_by_placeholder("Enter name").fill(name)
        self.page.get_by_placeholder("Enter phone").fill(phone)
        self.page.get_by_placeholder("Enter email").fill(email)
        self.page.get_by_placeholder("Enter address").fill(address)
        self.page.get_by_placeholder("Enter city").fill(city)
        self.page.get_by_placeholder("Enter postal code").fill(postal_code)
        self.page.get_by_placeholder("Enter customer type").fill(customer_type)

        self.page.get_by_role("button", name="Submit").click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    # ── /customer/list এ assert করো ──────────
    def assert_supplier_in_list(self, name: str):
        self.page.goto(f"{BASE_URL}/customer/list")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

        # Search করো
        search_box = self.page.get_by_placeholder("Search here..")
        search_box.wait_for(state="visible", timeout=10000)
        search_box.fill(name)
        self.page.wait_for_timeout(2000)

        # Table এ নাম খোঁজো
        rows = self.page.locator("table tbody tr")
        row_count = rows.count()

        assert row_count > 0, f"কোনো row নেই! '{name}' পাওয়া যায়নি।"

        found = False
        for i in range(row_count):
            if name in rows.nth(i).inner_text():
                found = True
                break

        assert found, f"❌ '{name}' customer list এ নেই!"
        print(f"✅ Customer '{name}' সফলভাবে list এ পাওয়া গেছে!")