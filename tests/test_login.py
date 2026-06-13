from playwright.sync_api import Page, expect

def test_login_Valid_Crediental(page:Page,login):
    page.goto(login)
    page.locator("#email").fill("sm.trading.jess@gmail.com")
    page.locator("#password").fill("smtradding2024")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.wait_for_timeout(5000)

def test_login_invalid_credential(page: Page, login):
    page.goto(login)
    page.locator("#email").fill("sm.trading.jess@gmail.com")
    page.locator("#password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()

    # should stay on login page
    expect(page.get_by_role("heading", name="Dashboard")).not_to_be_visible()

    # and show an error message (adjust text to match actual UI)
    expect(page.get_by_text("Invalid email or password")).to_be_visible()

def test_login_logout(page: Page, login):
    page.goto(login)
    page.locator("#email").fill("sm.trading.jess@gmail.com")
    page.locator("#password").fill("smtradding2024")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    # open user menu
    page.locator("#user-menu-button-2").click()

    # click logout
    page.get_by_role("button", name="Logout").click()

    # assert back on login page
    expect(page.get_by_role("heading", name="Sign In")).to_be_visible()