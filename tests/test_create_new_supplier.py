from pages.login_page import LoginPage
from pages.create_new_supplier_page import SupplierPage


# ══════════════════════════════════════════════
# TC-001: Static data দিয়ে supplier create
# ══════════════════════════════════════════════
def test_New_Supplier(login: LoginPage):
    supplier_page = SupplierPage(login.page)

    supplier_name = "Monika"

    supplier_page.create_supplier(
        name=supplier_name,
        phone="01712145678",
        email="monika@gmail.com",
        address="National park 201",
        city="Nevada",
        postal_code="90006",
        customer_type="Regular",
    )

    supplier_page.assert_supplier_in_list(supplier_name)
    login.page.wait_for_timeout(3000)



# ══════════════════════════════════════════════
# TC-002: Faker দিয়ে dynamic supplier create
# ══════════════════════════════════════════════
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

    supplier_page.assert_supplier_in_list(supplier_name)  # ← fixed
    login.page.wait_for_timeout(3000)
