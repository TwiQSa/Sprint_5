from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators_for_tests

class TestRegistration:
    def test_registration_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*locators_for_tests.name_reg).send_keys("Semyon")
        driver.find_element(*locators_for_tests.email_reg).send_keys("semyonchshemelinin8162@yandex.ru")
        driver.find_element(*locators_for_tests.password_reg).send_keys("123abc")

        driver.find_element(*locators_for_tests.registration_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Войти']"))))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()

    def test_registration_error_for_incorrect_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*locators_for_tests.name_reg).send_keys("Semyon")
        driver.find_element(*locators_for_tests.email_reg).send_keys("semyonchshemelinin8002@yandex.ru")
        driver.find_element(*locators_for_tests.password_reg).send_keys("123ab")

        driver.find_element(*locators_for_tests.registration_button).click()

        error = driver.find_element(*locators_for_tests.error_message)

        assert 'Некорректный пароль' in error.text

        driver.quit()
