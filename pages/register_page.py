from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "https://practicesoftwaretesting.com/auth/register"
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    DOB = (By.ID, "dob")
    POSTAL_CODE = (By.ID, "postal_code")
    HOUSE_NUMBER = (By.ID, "house_number")
    STREET = (By.ID, "street")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    PHONE = (By.ID, "phone")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    COUNTRY = (By.ID, "country")
    REG_BUTTON = (By.CSS_SELECTOR, "[data-test='register-submit']")
    # REG_BUTTON = (By.CLASS_NAME, "btnSubmit.mb-3")

    def input_first_name(self, text):
        self.type(self.FIRST_NAME, text)

    def input_last_name(self, text):
        self.type(self.LAST_NAME, text)

    def input_dob(self, text):
        self.type(self.DOB, text)

    def input_postal_code(self, text):
        self.type(self.POSTAL_CODE, text)

    def input_house_number(self, text):
        self.type(self.HOUSE_NUMBER, text)

    def input_street(self, text):
        self.type(self.STREET, text)

    def input_city(self, text):
        self.type(self.CITY, text)

    def input_state(self, text):
        self.type(self.STATE, text)

    def input_phone(self, text):
        self.type(self.PHONE, text)

    def input_email(self, text):
        self.type(self.EMAIL, text)

    def input_password(self, text):
        self.type(self.PASSWORD, text)

    def select_country(self, country):
        dropdown = Select(self.find(self.COUNTRY))
        dropdown.select_by_visible_text(country)   

    def click_register(self):
        self.wait_clickable(self.REG_BUTTON)
        self.click(self.REG_BUTTON)

    def fill_all_data(self, user):
        self.input_first_name(user["first_name"])
        self.input_last_name(user["last_name"])
        self.input_dob(user["dob"])
        self.select_country(user["country"])
        self.input_postal_code(user["postal_code"])
        self.input_house_number(user["house_number"])
        # self.input_street(user["street"])
        # self.input_city(user["city"])
        # self.input_state(user["state"])        
        self.input_phone(user["phone"])
        self.input_email(user["email"])
        self.input_password(user["password"])
        self.click_register()
            