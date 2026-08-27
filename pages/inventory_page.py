"""
InventoryPage Object representing the product catalog page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    PAGE_TITLE = (By.CSS_SELECTOR, "span.title")
    APP_LOGO = (By.CSS_SELECTOR, "div.app_logo")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, "div.inventory_item")

    # Add to cart dynamic helper locator
    @staticmethod
    def add_to_cart_button_by_name(product_name: str):
        # Convert product name e.g. "Sauce Labs Backpack" -> "add-to-cart-sauce-labs-backpack"
        slug = product_name.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{slug}")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Verify the inventory page is loaded with explicit wait."""
        try:
            self.wait.until(EC.url_contains("inventory.html"))
            return self.is_displayed(self.PAGE_TITLE)
        except TimeoutException:
            return False

    def get_title_text(self) -> str:
        """Get the inventory page heading title."""
        return self.get_text(self.PAGE_TITLE)

    def add_product_to_cart(self, product_name: str):
        """Add a specific product to the cart by its name."""
        locator = self.add_to_cart_button_by_name(product_name)
        self.click(locator)

    def get_cart_badge_count(self) -> int:
        """Return the current number of items displayed in cart badge."""
        if self.is_displayed(self.SHOPPING_CART_BADGE):
            text = self.get_text(self.SHOPPING_CART_BADGE)
            return int(text) if text.isdigit() else 0
        return 0

    def open_cart(self):
        """Click the shopping cart link to navigate to cart page."""
        self.click(self.SHOPPING_CART_LINK)
