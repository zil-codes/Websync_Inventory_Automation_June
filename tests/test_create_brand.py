
def test_add_brand(login, product):
    login.goto(product)
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Products Brands").click()
    login.get_by_role("button", name="Add Brand").click()
    login.get_by_placeholder("Enter name").fill("Gucci")
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(10000)

# def test_add_brand(login, product, fake):
#     login.goto(product)
#     login.get_by_role("button", name="Products").click()
#     login.get_by_role("link", name="Products Brands").click()
#     login.get_by_role("button", name="Add Brand").click()
#
#     # ---- Brand name (Faker দিয়ে dynamic) ----
#     brand_name = fake.company()
#     login.get_by_placeholder("Enter name").fill(brand_name)
#
#     login.get_by_role("button", name="Submit").click()
#     login.wait_for_timeout(10000)
