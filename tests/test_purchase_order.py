from pages.login_page import LoginPage
from pages.purchase_order_page import PurchaseOrderPage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে purchase order create
# ══════════════════════════════════════════════
def test_New_Purchase_Order(login: LoginPage):
    purchase_page = PurchaseOrderPage(login.page)

    purchase_page.create_purchase_order(
        supplier="Mojnu",
        invoice_number="9999999",
        payment_method="Cash",
        order_status="Due",
        payment_date="2026-06-23",
        purchase_date="2026-06-22",
        product_keyword="product",
    )

    login.page.wait_for_timeout(3000)
    purchase_page.assert_purchase_order_created()


# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic purchase order
# ══════════════════════════════════════════════
def test_New_Purchase_Order_faker(login: LoginPage, fake):
    purchase_page = PurchaseOrderPage(login.page)

    purchase_page.create_purchase_order(
        supplier="Mojnu",
        invoice_number=fake.numerify(text="INV-#####"),
        payment_method="Cash",
        order_status="Due",
        payment_date=fake.date_between(
            start_date="today", end_date="+30d"
        ).strftime("%Y-%m-%d"),
        purchase_date=fake.date_between(
            start_date="-30d", end_date="today"
        ).strftime("%Y-%m-%d"),
        product_keyword="product",
    )

    login.page.wait_for_timeout(3000)
    purchase_page.assert_purchase_order_created()