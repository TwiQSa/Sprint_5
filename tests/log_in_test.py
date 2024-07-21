from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogInFromVariosPages:
    def test_log_in_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_log_in_from_main_page_through_personal_account(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_log_in_from_registration_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()

        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_log_in_from_forgot_password_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()

        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

