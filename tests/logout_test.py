from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogout:
    def test_logout_from_personal_account(self, login):
        driver = login

        login.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Выход']"))))

        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Войти']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()


