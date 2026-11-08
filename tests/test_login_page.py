from pages.login_page import LoginPage
from data.users import VALID_USER, INVALID_USER


def test_login_page_open(driver):
    page = LoginPage(driver)
    page.open()
    assert "login" in driver.current_url

def test_email_field_visible(driver):
    page = LoginPage(driver)
    page.open()
    assert page.find(page.EMAIL).is_displayed()

def test_password_field_visible(driver):
    page = LoginPage(driver)

    page.open()

    assert page.find(page.PASSWORD).is_displayed()

def test_login_button_visible(driver):
    page = LoginPage(driver)
    page.open()
    assert page.find(page.LOGIN_BUTTON).is_displayed()

def test_login(driver):
    page=LoginPage(driver)
    page.open()
    page.login(VALID_USER['email'], VALID_USER['password'])
    page.wait_page_changed(driver.current_url)
    assert "account" in driver.current_url

def test_login_invalid_credentials(driver):
    page = LoginPage(driver)
    page.open()

    page.login(
        INVALID_USER["email"],
        INVALID_USER["password"]
    )

    page.wait_visible(page.ERROR_MESSAGE)
    assert page.get_text(page.ERROR_MESSAGE) == "Invalid email or password"

def test_login_empty_email(driver):
    page = LoginPage(driver)

    page.open()
    page.login("", "123456")

    page.wait_visible(page.EMAIL_REQUIRED_ERROR)

    assert page.get_text(page.EMAIL_REQUIRED_ERROR) == "Email is required"

def test_password_visibility_toggle(driver):
    page = LoginPage(driver)

    page.open()

    page.type(page.PASSWORD, "ABCDEFG")

    password_field = page.find(page.PASSWORD)

    assert password_field.get_attribute("type") == "password"

    page.click(page.PASSWORD_TOGGLE)

    assert password_field.get_attribute("type") == "text"

    page.click(page.PASSWORD_TOGGLE)

    assert password_field.get_attribute("type") == "password"
