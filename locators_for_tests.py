from selenium.webdriver.common.by import By
from selenium import webdriver

#Регистрация
name_reg = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='name' and @type='text']") # Имя в форме регистрации
email_reg = (By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default' and @name='name']") # Почта в форме регистрации
password_reg = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль' and @type='password']") # Пароль в форме регистрации
registration_button = (By.XPATH, ".//button[text()='Зарегистрироваться']") #Кнопка регистрации
error_message = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]") #Сообщение об ошибке

#Email и пароль для входа
sign_in_email = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='name' and @type='text']") # Почта для входа
sign_in_password = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль' and @type='password']") # Пароль для входа

#Вход
sign_in_button_from_main = (By.XPATH, ".//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт
sign_in_button_in_registration_form = (By.XPATH, ".//button[text()='Войти']") #Кнопка входа в форме регистрации
forgot_password_button = (By.XPATH, ".//button[text()='Восстановить пароль']") #Кнопка входа в форме восстановления пароля
sign_in_registration_form = (By.XPATH, ".//a[text()='Войти']") #Надпись войти на странице регистрации
sign_in_forgot_password_form = (By.XPATH, ".//a[text()='Войти']") #Надпись войти на странице забыл пароль

#Переход в личный кабинет
personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']") #Личный кабинет

#Переход из личного кабинета в конструктор
construction = (By.XPATH, ".//p[text()='Конструктор']") #Конструктор
logo = (By.XPATH, (".//div[@class='AppHeader_header__logo__2D0X2']/a")) #Логотип

#Выход из аккаунта
exit_button = (By.XPATH, ".//button[text()='Выход']")  #Кнопка выхода

#Раздел «Конструктор»
buns = (By.XPATH, ".//span[text()='Булки']")  #Булки
sauces = (By.XPATH, ".//span[text()='Соусы']")  #Соусы
stuffings = (By.XPATH, ".//span[text()='Начинки']")  #Начинки