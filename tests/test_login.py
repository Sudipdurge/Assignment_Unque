"""
Test Suite: Authentication Flows (Valid Login & Locked Out User)
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.auth
def test_valid_login(driver):
    """
    Test Case: Verify user can successfully log in with valid credentials.
    1. Open SauceDemo login page.
    2. Enter standard_user credentials.
    3. Verify successful landing on the inventory page.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded(), "Expected to be on the inventory page after valid login."
    assert inventory_page.get_title_text() == "Products", "Expected page title to be 'Products'."


@pytest.mark.auth
def test_locked_out_user_login(driver):
    """
    Test Case: Verify locked-out user receives appropriate error message and cannot log in.
    1. Open SauceDemo login page.
    2. Enter locked_out_user credentials.
    3. Verify error message appears with expected text.
    """
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_displayed(), "Expected error container to be visible for locked-out user."
    error_text = login_page.get_error_message()
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert expected_error in error_text, f"Expected error message '{expected_error}', but got '{error_text}'."
