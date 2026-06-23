from playwright.sync_api import expect

def test_New_Supplier(login, purchase):
    login.goto(purchase)
    login.get_by_role("button", name="Purchases").click()
    login.get_by_role("link", name="New Purchases").click()


    # # ---- ➕Create Supplier ----
    supplier_name = "Mojnu"

    login.get_by_role("button", name="Create Supplier").click()
    # Supplier Name
    login.get_by_placeholder("Enter name").fill("Mojnu")

    # Supplier Phone
    login.get_by_placeholder("Enter phone").fill("9090997675")

    # Supplier Email
    login.get_by_placeholder("Enter email").fill("mojnu@gmail.com")

    # Supplier Address
    login.get_by_placeholder("Enter address").fill("National park 201")

    # Supplier City
    login.get_by_placeholder("Enter city").fill("Nevada")

    # Supplier Postal Code
    login.get_by_placeholder("Enter postal code").fill("90006")

    # Supplier Type
    login.get_by_placeholder("Enter customer type").fill("Regular")

    # ---- Submit ----
    login.get_by_role("button", name="Submit").click()
    login.wait_for_timeout(3000)

    # ---- Assert: Supplier List এ আছে কিনা দেখো ----
    login.goto("https://dev.moinorrashid.com/customer/list")
    login.wait_for_timeout(2000)

    supplier_in_list = login.get_by_text(supplier_name, exact=True).first
    expect(supplier_in_list).to_be_visible()
    print(f"✅ Supplier '{supplier_name}' সফলভাবে তৈরি হয়েছে এবং list এ দেখা যাচ্ছে!")

