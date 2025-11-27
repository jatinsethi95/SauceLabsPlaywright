from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Step 1 - Navigate
        page.goto("https://www.saucedemo.com/")

        # Step 2 - Login
        login = LoginPage(page)
        login.login()

        # Step 3 - Select 3 random items
        inventory = InventoryPage(page)
        selected_items = inventory.add_random_items(3)

        # Navigate to cart
        inventory.go_to_cart()

        # Step 4 - Verify cart items
        cart = CartPage(page)
        cart_items = cart.get_cart_items()

        assert set(selected_items) == set(cart_items), \
            "Selected items do not match items in cart"

        # Continue to checkout
        cart.checkout()

        # Step 5 - Fill checkout details
        checkout = CheckoutPage(page)
        checkout.fill_information()

        # Finish checkout
        checkout.finish_checkout()

        # Step 6 - Assert success
        success_msg = checkout.get_success_message()

        assert success_msg == "Thank you for your order!", \
            "Order success message mismatch"

        browser.close()
