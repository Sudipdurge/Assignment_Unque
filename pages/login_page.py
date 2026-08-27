"""
LoginPage Object representing the SauceDemo authentication page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Navigate to the SauceDemo login page."""
        self.open(self.URL)

    def login(self, username: str, password: str):
        """Perform login action with given username and password."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Retrieve the error message text if login fails."""
        return self.get_text(self.ERROR_CONTAINER)

    def is_error_displayed(self) -> bool:
        """Check if error message container is visible."""
        return self.is_displayed(self.ERROR_CONTAINER)
