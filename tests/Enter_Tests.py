from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestEnter:

    def test_authorization_on_main_page(self, driver):  # Вход по кнопке «Войти в аккаунт» на главной странице
        driver.get(TestLocators.main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(TestLocators.my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(TestLocators.my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == TestLocators.main_page

    def test_authorization_in_personal_account_button(self, driver):  # Вход через кнопку «Личный кабинет»
        driver.get(TestLocators.main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(TestLocators.my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(TestLocators.my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == TestLocators.main_page

    def test_authorization_button_in_registration_form(self, driver):  # Вход через кнопку в форме регистрации
        driver.get(TestLocators.register_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(TestLocators.my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(TestLocators.my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == TestLocators.main_page

    def test_authorization_button_in_password_recovery(self,driver):  # Вход через кнопку в форме восстановления пароля
        driver.get(TestLocators.recovery_pass_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(TestLocators.my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(TestLocators.my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == TestLocators.main_page
