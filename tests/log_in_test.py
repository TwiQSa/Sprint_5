from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import locators_for_tests


class TestLogInFromVariosPages:
    def test_log_in_from_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(*locators_for_tests.sign_in_button_from_main).click()

        driver.find_element(*locators_for_tests.sign_in_email).send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(*locators_for_tests.sign_in_password).send_keys("123abc")

        driver.find_element(*locators_for_tests.sign_in_button_in_registration_form).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_log_in_from_main_page_through_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(*locators_for_tests.personal_account).click()

        driver.find_element(*locators_for_tests.sign_in_email).send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(*locators_for_tests.sign_in_password).send_keys("123abc")

        driver.find_element(*locators_for_tests.sign_in_button_in_registration_form).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_log_in_from_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*locators_for_tests.sign_in_registration_form).click()

        driver.find_element(*locators_for_tests.sign_in_email).send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(*locators_for_tests.sign_in_password).send_keys("123abc")

        driver.find_element(*locators_for_tests.sign_in_button_in_registration_form).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_log_in_from_forgot_password_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(*locators_for_tests.sign_in_forgot_password_form).click()

        driver.find_element(*locators_for_tests.sign_in_email).send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(*locators_for_tests.sign_in_password).send_keys("123abc")

        driver.find_element(*locators_for_tests.sign_in_button_in_registration_form).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

