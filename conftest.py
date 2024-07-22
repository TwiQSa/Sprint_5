import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators_for_tests

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locators_for_tests.sign_in_button_from_main)).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators_for_tests.sign_in_email)).send_keys("semyonchshemelinin8125@yandex.ru")
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators_for_tests.sign_in_password)).send_keys("123abc")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locators_for_tests.sign_in_button_in_registration_form)).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Личный Кабинет']")))
    return driver