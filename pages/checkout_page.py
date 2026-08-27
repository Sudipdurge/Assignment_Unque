"""
CheckoutPage Object representing the multi-step checkout workflow.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Step One Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Step Two Locators
    SUBTOTAL_LABEL = (By.CSS_SELECTOR, "div.summary_subtotal_label")
    TAX_LABEL = (By.CSS_SELECTOR, "div.summary_tax_label")
    TOTAL_LABEL = (By.CSS_SELECTOR, "div.summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")

    # Step Complete Locators
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")
    COMPLETE_TEXT = (By.CSS_SELECTOR, "div.complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        """Fill customer details in Checkout Step One and continue."""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def is_overview_loaded(self) -> bool:
        """Verify checkout step two overview is displayed with explicit wait."""
        try:
            self.wait.until(EC.url_contains("checkout-step-two.html"))
            return self.is_displayed(self.FINISH_BUTTON)
        except TimeoutException:
            return False

    def get_summary_total(self) -> str:
        """Return total label text."""
        return self.get_text(self.TOTAL_LABEL)

    def click_finish(self):
        """Click finish button on overview step."""
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self) -> bool:
        """Verify order completion confirmation screen with explicit wait."""
        try:
            self.wait.until(EC.url_contains("checkout-complete.html"))
            return self.is_displayed(self.COMPLETE_HEADER)
        except TimeoutException:
            return False

    def get_completion_header(self) -> str:
        """Get the confirmation header text."""
        return self.get_text(self.COMPLETE_HEADER)
