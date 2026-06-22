
def test_add_category(login, product):
    login.goto(product)
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Products Category").click()
    login.get_by_role("button", name="Add Category").click()
    login.get_by_placeholder("Enter name").fill("Guccifemale")
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(10000)

# def test_add_category(login, product, fake):
#     login.goto(product)
#     login.get_by_role("button", name="Products").click()
#     login.get_by_role("link", name="Products Category").click()
#     login.get_by_role("button", name="Add Category").click()
#
#     # ---- Category name (Faker দিয়ে dynamic) ----
#     category_name = fake.word()
#     login.get_by_placeholder("Enter name").fill(category_name)
#
#     login.get_by_role("button", name="Submit").click()
#     login.wait_for_timeout(10000)