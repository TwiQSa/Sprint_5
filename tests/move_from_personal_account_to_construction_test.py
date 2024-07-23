from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import locators_for_tests


class TestMoveFromPersonalAccountToConstruction:
    def test_personal_account_to_construction(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(*locators_for_tests.sign_in_button_from_main).click()

        driver.find_element(*locators_for_tests.sign_in_email).send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(*locators_for_tests.sign_in_password).send_keys("123abc")

        driver.find_element(*locators_for_tests.sign_in_button_in_registration_form).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//p[text()='Личный Кабинет']"))))

        driver.find_element(*locators_for_tests.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Сохранить']"))))

        driver.find_element(*locators_for_tests.construction).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_from_personal_account_through_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(*locators_for_tests.sign_in_button_from_main).click()

        driver.find_element(*locators_for_tests.sign_in_email).send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(*locators_for_tests.sign_in_password).send_keys("123abc")

        driver.find_element(*locators_for_tests.sign_in_button_in_registration_form).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//p[text()='Личный Кабинет']"))))

        driver.find_element(*locators_for_tests.personal_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Сохранить']"))))

        driver.find_element(By.XPATH, ("//div[@class='AppHeader_header__logo__2D0X2']/a")).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()