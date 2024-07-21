#Регистрация
(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='name'][1]") #Поле ввода имени
(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input") #Поле ввода email
(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @name='Пароль']") #Поле ввода пароля
(By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка регистрации
(By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]") #Сообщение об ошибке

#Вход
(By.XPATH, ".//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт
(By.XPATH, ".//p[text()='Личный Кабинет']") #Личный кабинет
(By.XPATH, ".//button[text()='Войти']") #Кнопка входа в форме регистрации
(By.XPATH, "//button[text()='Восстановить пароль']") #Кнопка входа в форме восстановления пароля

#Переход в личный кабинет
(By.XPATH, ".//p[text()='Личный Кабинет']") #Личный кабинет

#Переход из личного кабинета в конструктор
(By.XPATH, ".//p[text()='Конструктор']") #Конструктор
(By.XPATH, ("//div[@class='AppHeader_header__logo__2D0X2']/a")) #Логотип

#Выход из аккаунта
(By.XPATH, ".//button[text()='Выход']")  #Кнопка выхода

#Раздел «Конструктор»
(By.XPATH, ".//span[text()='Булки']")  #Булки
(By.XPATH, ".//span[text()='Соусы']")  #Соусы
(By.XPATH, ".//span[text()='Начинки']")  #Начинки