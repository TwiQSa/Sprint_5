import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Личный Кабинет']")))
    return driver