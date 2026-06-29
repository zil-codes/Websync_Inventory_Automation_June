from pages.login_page import LoginPage
from pages.create_new_customer_page import CustomerPage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে customer create
# ══════════════════════════════════════════════
def test_New_Customer(login: LoginPage):
    customer_page = CustomerPage(login.page)

    customer_name = "Troy Moly"

    customer_page.create_supplier(
        name=customer_name,
        phone="01712345634",
        email="troy@gmail.com",
        address="National park 201",
        city="Nevada",
        postal_code="90006",
        customer_type="Regular",
    )

    customer_page.assert_supplier_in_list(customer_name)
    login.page.wait_for_timeout(3000)


# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic customer create
# ══════════════════════════════════════════════
def test_New_Customer_faker(login: LoginPage, fake):
    customer_page = CustomerPage(login.page)

    customer_name = fake.name()

    customer_page.create_supplier(
        name=customer_name,
        phone=fake.numerify(text="##########"),
        email=fake.email(),
        address=fake.street_address(),
        city=fake.city(),
        postal_code=fake.postcode(),
        customer_type=fake.random_element(["Regular", "VIP", "Wholesale"]),
    )

    customer_page.assert_supplier_in_list(customer_name)
    login.page.wait_for_timeout(3000)