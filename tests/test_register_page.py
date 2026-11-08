from data.users import REGISTER_USER
from pages.register_page import RegisterPage


def test_successful_registration(driver):
    page = RegisterPage(driver)
    page.open()
    page.fill_all_data(REGISTER_USER)
    page.wait_page_changed(driver.current_url)
    assert "login" in driver.current_url


def test_first_name_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_first_name("")
    page.click_register()
    assert page.get_first_name_error() == "First name is required"


def test_last_name_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_last_name("")
    page.click_register()
    assert page.get_last_name_error() == "Last name is required"


def test_dob_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_dob("")
    page.click_register()
    assert page.get_dob_error() == "Date of Birth is required"


def test_dob_invalid_format_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_dob("123")
    page.click_register()
    assert page.get_dob_error() == "Please enter a valid date in YYYY-MM-DD format."


def test_country_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.click_register()
    assert page.get_country_error() == "Country is required"


def test_select_country_info_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.select_country("Palau")
    assert page.get_country_info_message() == (
        "Choose your country and enter the postal code and house number. "
        "Street, city and state will be filled in automatically."
    )


def test_postal_code_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_postal_code("")
    page.click_register()
    assert page.get_postal_code_error() == "Postcode is required"


def test_email_required_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_email("")
    page.click_register()
    assert page.get_email_error() == "Email is required"


def test_email_without_at_sign_message(driver):
    page = RegisterPage(driver)
    page.open()
    page.input_email("testmail.ru")
    page.click_register()
    assert page.get_email_error() == "Email format is invalid"

