"""
CartPage Object representing the shopping cart page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    # Locators
    PAGE_TITLE = (By.CSS_SELECTOR, "span.title")
    CART_ITEMS = (By.CSS_SELECTOR, "div.cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, "div.inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Verify the cart page is loaded with explicit wait."""
        try:
            self.wait.until(EC.url_contains("cart.html"))
            return self.is_displayed(self.CHECKOUT_BUTTON)
        except TimeoutException:
            return False

    def get_cart_item_names(self) -> list[str]:
        """Return a list of all item names currently in the cart."""
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]

    def click_checkout(self):
        """Click the checkout button to proceed to Step One."""
        self.click(self.CHECKOUT_BUTTON)
