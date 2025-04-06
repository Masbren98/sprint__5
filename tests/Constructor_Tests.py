from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators


class TestConstructor:
    def test_transitions_to_sections_buns(self, driver):  # Тест перехода к разделу «Булки»
        driver.get(TestLocators.main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).click()
        assert driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).text == driver.find_element(By.XPATH, TestLocators.ACTIVE_BUTTON).text
        driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.BUNS_TEXT_BUTTON)))
        assert driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_BUTTON).text == driver.find_element(By.XPATH, TestLocators.ACTIVE_BUTTON).text

    def test_transitions_to_sections_sauces(self, driver): # Тест перехода к разделу «Соусы»
        driver.get(TestLocators.main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.SAUCES_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).click()
        assert driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).text == driver.find_element(By.XPATH, TestLocators.ACTIVE_BUTTON).text

    def test_transitions_to_sections_fillings(self, driver): # Тест перехода к разделу «Начинки»
        driver.get(TestLocators.main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).click()
        assert driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).text == driver.find_element(By.XPATH, TestLocators.ACTIVE_BUTTON).text