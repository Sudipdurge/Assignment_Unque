"""
BasePage class containing common helper methods and explicit waits
for all page objects in the SauceDemo automation framework.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        """Navigate to a specified URL."""
        self.driver.get(url)

    def find(self, locator):
        """Wait for an element to be present in the DOM and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        """Wait for an element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text: str):
        """Wait for an element to be visible, clear it, and type text."""
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        """Get the text content of a visible element."""
        element = self.find_visible(locator)
        return element.text

    def is_displayed(self, locator) -> bool:
        """Check if an element is visible on the page."""
        try:
            return self.find_visible(locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def get_current_url(self) -> str:
        """Return the current browser URL."""
        return self.driver.current_url

    def get_page_title(self) -> str:
        """Return the current page title."""
        return self.driver.title
