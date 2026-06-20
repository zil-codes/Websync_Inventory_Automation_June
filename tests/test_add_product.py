
def test_add_brand(login, product):
    login.goto(product)
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Products Brands").click()
    login.get_by_role("button", name="Add Brand").click()
    login.get_by_placeholder("Enter name").fill("Test Brand")
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(10000)


def test_add_category(login, product):
    login.goto(product)
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Products Category").click()
    login.get_by_role("button", name="Add Category").click()
    login.get_by_placeholder("Enter name").fill("Test Category")
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(10000)

def test_create_Product(login, product):
    login.goto(product)
    login.get_by_role("button", name="Products").click()
    login.get_by_role("link", name="Add Products").click()

    # Product name
    login.get_by_placeholder("Enter name").fill("Testbc")

    # ---- Category select ----
    login.locator("input[name='category']").locator("xpath=../..//input[@role='combobox']" ).click()
    login.wait_for_timeout(500)
    print("Category options:", login.get_by_role("option").all_text_contents())
    login.get_by_role("option", name="Test Category", exact=True).click()

    # ---- Brand select ----
    login.locator("input[name='brand']").locator("xpath=../..//input[@role='combobox']" ).click()
    login.wait_for_timeout(500)
    print("Brand options:", login.get_by_role("option").all_text_contents())
    login.get_by_role("option", name="Test Brand", exact=True).click()

    login.wait_for_timeout(5000)