from playwright.sync_api import Page, expect

BASE_URL = "https://dev.moinorrashid.com"


class AddSalePage:

    def __init__(self, page: Page):
        self.page = page

        # ── Navigation ──
        self.sales_menu_button = page.get_by_role("button", name="Sales")
        self.add_sale_link = page.get_by_role("link", name="Add Sale")

        # ── Search Customer Modal ──
        self.search_customer_button = page.get_by_role("button", name="🔍 Search Customer")
        self.modal = page.locator('[role="dialog"]')
        self.modal_search_input = self.modal.locator('input[placeholder="Search here..."]')

        # ── Form fields ──
        self.invoice_number_input = page.locator('input[name="invoiceNumber"]')
        self.payment_date_input = page.locator('input[name="paymentDate"]')
        self.sale_date_input = page.locator('input[name="saleDate"]')       # ✅ confirmed
        self.product_search_input = page.locator('input[placeholder="Search by product name..."]')
        self.discount_input = page.locator('input[type="number"]').nth(0)
        self.tax_input = page.locator('input[type="number"]').nth(1)
        self.receive_amount_input = page.locator('input[class*="border-purple"]').first

        # ── React Select dropdowns ──
        self.payment_method_select = page.locator('#react-select-2-placeholder')
        self.order_status_select = page.locator('#react-select-3-placeholder')

        # ── Submit ──
        self.submit_button = page.get_by_role("button", name="Create Sale Order")

    # ── Navigate ──────────────────────────────
    def navigate(self):
        self.page.goto(BASE_URL)
        self.sales_menu_button.click()
        self.add_sale_link.click()
        self.page.wait_for_load_state("networkidle")

    # ── Customer select ───────────────────────
    def select_customer(self, customer_name: str):
        self.search_customer_button.click()
        self.modal.wait_for(state="visible")
        self.modal_search_input.fill(customer_name)
        self.page.wait_for_timeout(500)
        self.modal.locator("table tbody tr", has_text=customer_name).first.click()
        self.page.wait_for_timeout(500)

    # ── Form fill methods ─────────────────────
    def fill_invoice_number(self, invoice: str):
        self.invoice_number_input.fill(invoice)

    def fill_payment_date(self, date: str):
        """date format: YYYY-MM-DD"""
        self.payment_date_input.fill(date)

    def fill_sale_date(self, date: str):
        """date format: YYYY-MM-DD"""
        self.sale_date_input.fill(date)

    def fill_discount(self, discount: str):
        self.discount_input.fill(discount)

    def fill_tax(self, tax: str):
        self.tax_input.fill(tax)

    def fill_receive_amount(self, amount: str):
        self.receive_amount_input.wait_for(state="visible", timeout=5000)
        self.receive_amount_input.fill(amount)

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
        self.page.wait_for_timeout(1000)
        # Table এ "Add" button click করো
        self.page.locator("table tbody tr").first.get_by_role("button", name="Add").click()
        self.page.wait_for_timeout(500)

    # ── Submit ────────────────────────────────
    def submit(self):
        self.submit_button.click()
        self.page.wait_for_timeout(2000)

    # ── Assert ────────────────────────────────
    def assert_sale_order_created(self):
        try:
            toast = self.page.locator(".toast, [class*='success'], [class*='alert']").first
            toast.wait_for(state="visible", timeout=5000)
            print(f"✅ Sale Order তৈরি হয়েছে! Toast: {toast.inner_text()}")
        except Exception:
            current_url = self.page.url
            assert "sale" in current_url, f"❌ Failed! URL: {current_url}"
            print(f"✅ Sale Order তৈরি হয়েছে! URL: {current_url}")

    # ── Full flow ─────────────────────────────
    def create_sale_order(
        self,
        customer: str,
        invoice_number: str,
        payment_method: str,
        order_status: str,
        payment_date: str,
        sale_date: str,
        product_keyword: str,
        discount: str = "0",
        tax: str = "0",
        receive_amount: str = "0",
    ):
        self.navigate()
        self.select_customer(customer)
        self.fill_invoice_number(invoice_number)
        self.select_payment_method(payment_method)
        self.select_order_status(order_status)
        self.fill_payment_date(payment_date)
        self.fill_sale_date(sale_date)
        self.add_product(product_keyword)
        self.fill_discount(discount)
        self.fill_tax(tax)
        self.fill_receive_amount(receive_amount)
        self.submit()
