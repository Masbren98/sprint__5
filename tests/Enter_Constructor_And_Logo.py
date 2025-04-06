from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestEnterConstructor:
    def test_click_to_go_constructor(self, driver): # Переход по клику на «Конструктор» из личного кабинета
        driver.get(TestLocators.authorization_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(TestLocators.my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(TestLocators.my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.EXIT_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == TestLocators.main_page

    def test_transition_by_clicking_on_logo(self, driver): # Переход по клику на логотип Stellar Burgers из личного кабинета
        driver.get(TestLocators.authorization_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(TestLocators.my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(TestLocators.my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.EXIT_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.LOGO_STELLAR_BURGERS).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == TestLocators.main_page