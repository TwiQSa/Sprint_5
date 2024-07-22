from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import locators_for_tests

class TestMoveToPersonalAccount:
    def test_personal_account_page(self, login):
        driver = login
        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*locators_for_tests.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Сохранить']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()