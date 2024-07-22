from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import locators_for_tests

class TestLogout:
    def test_logout_from_personal_account(self, login):
        driver = login
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*locators_for_tests.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Выход']"))))

        driver.find_element(*locators_for_tests.exit_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Войти']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()


