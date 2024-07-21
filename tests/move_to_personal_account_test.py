from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestMoveToPersonalAccount:
    def test_personal_account_page(self, login):
        driver = login

        login.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(((By.XPATH, ".//button[text()='Сохранить']"))))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.quit()