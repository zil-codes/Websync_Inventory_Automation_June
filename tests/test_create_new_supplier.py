import time
from pages.login_page import LoginPage
from pages.create_new_supplier_page import SupplierPage


def test_New_Supplier(login: LoginPage):
    supplier_page = SupplierPage(login.page)
    unique_suffix = int(time.time())
    supplier_name = f"Bindon {unique_suffix}"
    supplier_page.create_supplier(
        name=supplier_name,
        phone=f"018{str(unique_suffix)[-8:]}",
        email=f"bin{unique_suffix}@gmail.com",
        address="National park 201",
        city="Nevada",
        postal_code="90006",
        customer_type="Regular",
    )
    supplier_page.assert_supplier_in_list(supplier_name)
    login.page.wait_for_timeout(3000)


def test_New_Supplier_faker(login: LoginPage, purchase: str, fake):
    supplier_page = SupplierPage(login.page)
    supplier_name = fake.name()
    supplier_page.create_supplier(
        name=supplier_name,
        phone=fake.numerify(text="##########"),
        email=fake.email(),
        address=fake.street_address(),
        city=fake.city(),
        postal_code=fake.postcode(),
        customer_type=fake.random_element(["Regular", "VIP", "Wholesale"]),
    )
    supplier_page.assert_supplier_in_list(supplier_name)
    login.page.wait_for_timeout(3000)