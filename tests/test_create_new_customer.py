import time
from pages.login_page import LoginPage
from pages.create_new_customer_page import CustomerPage


def test_New_Customer(login: LoginPage):
    customer_page = CustomerPage(login.page)
    unique_suffix = int(time.time())
    customer_name = f"Xman {unique_suffix}"
    customer_page.create_supplier(
        name=customer_name,
        phone=f"017{str(unique_suffix)[-8:]}",
        email=f"man{unique_suffix}@gmail.com",
        address="National park 201",
        city="Nevada",
        postal_code="90006",
        customer_type="Regular",
    )
    customer_page.assert_supplier_in_list(customer_name)
    login.page.wait_for_timeout(3000)


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