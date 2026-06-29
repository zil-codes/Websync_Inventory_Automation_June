from pages.login_page import LoginPage
from pages.add_sale_page import AddSalePage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে sale order create
# ══════════════════════════════════════════════
def test_New_Sale_Order(login: LoginPage):
    sale_page = AddSalePage(login.page)

    sale_page.create_sale_order(
        customer="meanual",
        invoice_number="SAL-0001",
        payment_method="Cash",
        order_status="Due",
        payment_date="2026-06-28",
        sale_date="2026-06-28",
        product_keyword="Moringa",
        discount="0",
        tax="0",
        receive_amount="600",
    )

    login.page.wait_for_timeout(3000)
    sale_page.assert_sale_order_created()


# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic sale order
# ══════════════════════════════════════════════
def test_New_Sale_Order_faker(login: LoginPage, fake):
    sale_page = AddSalePage(login.page)

    sale_page.create_sale_order(
        customer="meanual",
        invoice_number=fake.numerify(text="SAL-#####"),
        payment_method="Cash",
        order_status="Due",
        payment_date=fake.date_between(
            start_date="today", end_date="+30d"
        ).strftime("%Y-%m-%d"),
        sale_date=fake.date_between(
            start_date="-30d", end_date="today"
        ).strftime("%Y-%m-%d"),
        product_keyword="Moringa",
        discount="0",
        tax="0",
        receive_amount=str(fake.random_int(min=100, max=10000)),
    )

    login.page.wait_for_timeout(3000)
    sale_page.assert_sale_order_created()
