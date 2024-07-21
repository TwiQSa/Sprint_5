from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration:
    def test_registration_successful(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='name'][1]").send_keys("Semyon")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("semyonchshemelinin8149@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Войти']"))))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.quit()

    def test_registration_error_for_incorrect_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH,".//input[@class='text input__textfield text_type_main-default' and @name='name'][1]").send_keys("Semyon")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("semyonchshemelinin8002@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123ab")

        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

        error = driver.find_element(By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")

        assert 'Некорректный пароль' in error.text

        driver.quit()
