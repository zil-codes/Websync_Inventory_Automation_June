from playwright.sync_api import Page, expect

def test_login_valid_credential(login):
    # login fixture already logged in, just assert dashboard
    expect(login.get_by_role("heading", name="Dashboard")).to_be_visible()
    login.wait_for_timeout(10000)

def test_login_invalid_credential(page: Page):
    page.goto("https://dev.moinorrashid.com/login")
    page.locator("#email").fill("sm.trading.jess@gmail.com")
    page.locator("#password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Dashboard")).not_to_be_visible()
    expect(page.get_by_text("Invalid email or password")).to_be_visible()
    page.wait_for_timeout(10000)

def test_login_logout(login):
    login.locator("#user-menu-button-2").click()
    login.get_by_role("button", name="Logout").click()
    expect(login.get_by_role("heading", name="Sign In")).to_be_visible()
    login.wait_for_timeout(10000)


    # login fixture handles auth, so no page.goto(login) needed in valid credential and logout tests.
    # Only the invalid credential test uses page directly since it needs a fresh unauthenticated session.


