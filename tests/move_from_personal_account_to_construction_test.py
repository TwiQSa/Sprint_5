from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestMoveFromPersonalAccountToConstruction:
    def test_personal_account_to_construction(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//p[text()='Личный Кабинет']"))))

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Сохранить']"))))

        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_from_personal_account_through_logo(self, login):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("semyonchshemelinin8125@yandex.ru")
        driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123abc")

        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//p[text()='Личный Кабинет']"))))

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Сохранить']"))))

        driver.find_element(By.XPATH, ("//div[@class='AppHeader_header__logo__2D0X2']/a")).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Оформить заказ']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()