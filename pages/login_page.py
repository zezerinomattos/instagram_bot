from selenium.webdriver.common.by import By
from config.settings import INSTAGRAM_URL, USERNAME, PASSWORD
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def go_to_login_page(self):
        self.driver.get(INSTAGRAM_URL)

    def login(self):
        self.input_text(self.USERNAME_FIELD, USERNAME)
        self.input_text(self.PASSWORD_FIELD, PASSWORD)
        self.click(self.LOGIN_BUTTON)
