import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser):

    if browser == "chrome":
        return webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            )
        )

    if browser == "firefox":
        return webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install()
            )
        )

    if browser == "edge":
        return webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()
            )
        )


# @pytest.fixture(params=["chrome", "firefox", "edge"])
@pytest.fixture(params=["chrome"])
def driver(request):
    driver = get_driver(request.param)
    driver.set_window_position(0, -1080)
    driver.maximize_window()
    # driver.minimize_window()
    driver.implicitly_wait(3)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            filename = f"screenshots/{item.name}.png"

            driver.save_screenshot(filename)

            allure.attach.file(
                filename,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )