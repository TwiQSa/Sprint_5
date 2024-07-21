from selenium.webdriver.common.by import By
from selenium import webdriver

class TestFromConstructionToVariousSections:
    def test_from_construction_to_buns(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()

        driver.find_element(By.XPATH, ".//span[text()='Булки']").click()

        bun = driver.find_element(By.XPATH, ".//p[contains(text(), 'Флюоресцентная булка R2-D3')]")

        assert 'Флюоресцентная булка R2-D3' in bun.text

        driver.quit()

    def test_from_construction_to_sauces(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()

        sauce = driver.find_element(By.XPATH, ".//p[contains(text(), 'Соус фирменный Space Sauce')]")

        assert 'Соус фирменный Space Sauce' in sauce.text

        driver.quit()

    def test_from_construction_to_stuffing(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()

        stuffing = driver.find_element(By.XPATH, ".//p[contains(text(), 'Биокотлета из марсианской Магнолии')]")

        assert 'Биокотлета из марсианской Магнолии' in stuffing.text

        driver.quit()

