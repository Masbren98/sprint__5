Sprint_5
    
В корне проекта:
Фикстуры - conftest.py
Локаторы - locators.py
Генератор рандомных значений (Имя, Логин, пароль (валидный/невалидный)) -random_gen.py
Папка с тестами - tests

Тесты:

Регистрация - Registration_Tests.py
1) test_registration - Успешная регистрация с рандомными валидными значениями
2) test_error_incorrect_password - Ошибка регистрации с невалидным паролем

Вход в аккаунт - Enter_Tests.py
1) test_authorization_on_main_page - Вход по кнопке «Войти в аккаунт» на главной странице
2) test_authorization_in_personal_account_button - Вход через кнопку «Личный кабинет»
3) test_authorization_button_in_registration_form - Вход через кнопку в форме регистрации
4) test_authorization_button_in_password_recovery - Вход через кнопку в форме восстановления пароля

Переход в личный кабинет - Accounts_Tests.py 

Переход из личного кабинета в конструктор - Enter_Constructor_And_Logo.py 

Выход из аккаунта - Accounts_Out_Tests.py 

Проверка перехода к разделам в конструкторе - Constructor_Tests.py
