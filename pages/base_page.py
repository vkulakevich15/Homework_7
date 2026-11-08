from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait_clickable(locator)
        self.find(locator).click()

    def type(self, locator, text):
        self.wait_visible(locator)

        self.find(locator).clear()

        WebDriverWait(self.driver, 10).until(
            lambda d: self.find(locator).get_attribute("value") == ""
        )

        self.find(locator).send_keys(text)

        WebDriverWait(self.driver, 10).until(
            lambda d: self.find(locator).get_attribute("value") == text
        )

        # self.find(locator).send_keys(Keys.ENTER)

    def get_text(self, locator):
        return self.find(locator).text

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver,
                timeout).until(
                EC.element_to_be_clickable(
                locator)
                )

    def wait_page_changed(self, old, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda x: x.current_url != old
        )
