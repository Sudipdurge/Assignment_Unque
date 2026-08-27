"""
Test Suite: End-to-End Shopping Cart & Checkout Flow
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
def test_add_item_to_cart_and_complete_checkout(driver):
    """
    Test Case: Verify adding an item to cart and completing the checkout journey.
    1. Login with valid credentials.
    2. Add 'Sauce Labs Backpack' to the cart.
    3. Verify cart badge counter updates to 1.
    4. Open the cart page and verify item presence.
    5. Proceed to checkout and submit customer info.
    6. Verify order summary overview.
    7. Finish order and verify order completion screen.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Login
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded(), "Failed to navigate to inventory page."

    # 2. Add product to cart
    product_name = "Sauce Labs Backpack"
    inventory_page.add_product_to_cart(product_name)

    # 3. Verify Cart Badge
    assert inventory_page.get_cart_badge_count() == 1, "Cart badge count did not update to 1."

    # 4. Open Cart & Verify item
    inventory_page.open_cart()
    assert cart_page.is_loaded(), "Failed to navigate to shopping cart page."
    cart_items = cart_page.get_cart_item_names()
    assert product_name in cart_items, f"Expected '{product_name}' to be in cart, found: {cart_items}"

    # 5. Proceed to Checkout Step One
    cart_page.click_checkout()
    checkout_page.fill_information(
        first_name="Jane",
        last_name="Doe",
        postal_code="90210"
    )

    # 6. Verify Checkout Step Two Overview
    assert checkout_page.is_overview_loaded(), "Failed to navigate to checkout step two overview."

    # 7. Complete Order
    checkout_page.click_finish()
    assert checkout_page.is_order_complete(), "Expected checkout complete screen to be displayed."
    assert "Thank you for your order!" in checkout_page.get_completion_header(), (
        f"Unexpected completion header: {checkout_page.get_completion_header()}"
    )
