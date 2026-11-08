from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.register_page import RegisterPage

class LoginPage(BasePage):
    URL='https://practicesoftwaretesting.com/auth/login'
    EMAIL=(By.ID,'email')
    PASSWORD=(By.ID,'password')
    LOGIN_BUTTON=(By.CSS_SELECTOR,"[data-test='login-submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    EMAIL_REQUIRED_ERROR = (By.XPATH, "//*[contains(text(),'Email is required')]")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, ".input-group-append button")

    # def open(self):
    #     self.driver.get(self.URL)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.wait_clickable(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def click_register(self):
        self.click(self.REGISTER_LINK)
        return RegisterPage(self.driver)
