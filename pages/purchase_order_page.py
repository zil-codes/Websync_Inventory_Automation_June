from playwright.sync_api import Page, expect

BASE_URL = "https://dev.moinorrashid.com"


class PurchaseOrderPage:

    def __init__(self, page: Page):
        self.page = page

        # ── Navigation ──
        self.purchases_menu_button = page.get_by_role("button", name="Purchases")
        self.new_purchases_link = page.get_by_role("link", name="New Purchases")

        # ── Supplier Search Modal ──
        self.search_supplier_button = page.get_by_role("button", name="🔍 Search Supplier")
        self.modal = page.locator('[role="dialog"]')
        self.modal_search_input = self.modal.locator('input[placeholder="Search here..."]')

        # ── Form fields ──
        self.invoice_number_input = page.locator('input[name="invoiceNumber"]')
        self.payment_date_input = page.locator('input[name="paymentDate"]')
        self.purchase_date_input = page.locator('input[name="purchaseDate"]')
        self.product_search_input = page.locator('input[placeholder="Search by product name..."]')

        # ── React Select dropdowns ──
        self.payment_method_select = page.locator('#react-select-2-placeholder')
        self.order_status_select = page.locator('#react-select-3-placeholder')

        # ── Submit ──
        self.submit_button = page.get_by_role("button", name="Create Purchase Order")

    # ── Navigate ──────────────────────────────
    def navigate(self):
        self.page.goto(BASE_URL)
        self.purchases_menu_button.click()
        self.new_purchases_link.click()
        self.page.wait_for_load_state("networkidle")

    # ── Supplier ──────────────────────────────
    def select_supplier(self, supplier_name: str):
        self.search_supplier_button.click()
        self.modal.wait_for(state="visible")
        self.modal_search_input.fill(supplier_name)
        self.page.wait_for_timeout(500)
        self.modal.locator("table tbody tr", has_text=supplier_name).first.click()
        self.page.wait_for_timeout(500)

    # ── Form fields ───────────────────────────
    def fill_invoice_number(self, invoice: str):
        self.invoice_number_input.fill(invoice)

    def fill_payment_date(self, date: str):
        """date format: YYYY-MM-DD"""
        self.payment_date_input.fill(date)

    def fill_purchase_date(self, date: str):
        """date format: YYYY-MM-DD"""
        self.purchase_date_input.fill(date)

    # ── Dropdowns ─────────────────────────────
    def select_payment_method(self, method: str):
        self.payment_method_select.click(force=True)
        self.page.wait_for_timeout(300)
        self.page.get_by_role("option", name=method).click()

    def select_order_status(self, status: str):
        self.order_status_select.click(force=True)
        self.page.wait_for_timeout(300)
        self.page.get_by_role("option", name=status).click()

    # ── Product ───────────────────────────────
    def add_product(self, product_keyword: str):
        self.product_search_input.fill(product_keyword)
        self.page.wait_for_timeout(500)
        self.page.locator('[class*="suggestion"], [class*="result"], tbody tr').first.click()
        self.page.wait_for_timeout(300)

    # ── Submit ────────────────────────────────
    def submit(self):
        self.submit_button.click()
        self.page.wait_for_timeout(2000)

    # ── Assert ────────────────────────────────
    def assert_purchase_order_created(self):
        assert "purchase" in self.page.url, "Purchase Order creation failed!"
        print(f"✅ Purchase Order সফলভাবে তৈরি হয়েছে! URL: {self.page.url}")


    # ── Full flow ─────────────────────────────
    def create_purchase_order(
        self,
        supplier: str,
        invoice_number: str,
        payment_method: str,
        order_status: str,
        payment_date: str,
        purchase_date: str,
        product_keyword: str,
    ):
        self.navigate()
        self.select_supplier(supplier)
        self.fill_invoice_number(invoice_number)
        self.select_payment_method(payment_method)
        self.select_order_status(order_status)
        self.fill_payment_date(payment_date)
        self.fill_purchase_date(purchase_date)
        self.add_product(product_keyword)
        self.submit()
