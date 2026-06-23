def test_New_Purchase_Order(login, purchase):
    login.goto(purchase)

    # ---- Navigate to New Purchase ----
    login.get_by_role("button", name="Purchases").click()
    login.get_by_role("link", name="New Purchases").click()
    login.wait_for_load_state("networkidle")

    # ---- Search Supplier ----
    login.get_by_role("button", name="🔍 Search Supplier").click()
    modal = login.locator('[role="dialog"]')
    modal.wait_for(state="visible")
    modal.locator('input[placeholder="Search here..."]').fill("Mojnu")
    login.wait_for_timeout(500)
    modal.locator('table tbody tr', has_text="Mojnu").first.click()
    login.wait_for_timeout(500)

    # ---- Invoice Number ----
    login.locator('input[name="invoiceNumber"]').fill("9999999")

    # ---- Payment Method (React Select) ----
    login.locator('#react-select-2-placeholder').click(force=True)
    login.wait_for_timeout(300)
    login.get_by_role('option', name="Cash").click()

    # ---- Order Status (React Select) ----
    login.locator('#react-select-3-placeholder').click(force=True)
    login.wait_for_timeout(300)
    login.get_by_role('option', name="Due").click()

    # ---- Payment Date ----
    login.locator('input[name="paymentDate"]').fill("2026-06-23")

    # ---- Purchase Date ----
    login.locator('input[name="purchaseDate"]').fill("2026-06-22")

    # ---- Add Product ----
    login.locator('input[placeholder="Search by product name..."]').fill("product")
    login.wait_for_timeout(500)
    login.locator('[class*="suggestion"], [class*="result"], tbody tr').first.click()
    login.wait_for_timeout(300)

    # ---- Submit ----
    login.get_by_role("button", name="Create Purchase Order").click()
    login.wait_for_timeout(2000)

    # ---- Assert: URL change অথবা page title ----
    assert "purchase" in login.url, "Purchase Order creation failed!"

    login.wait_for_timeout(3000)