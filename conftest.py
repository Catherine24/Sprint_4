import allure
import pytest
from selenium import webdriver


@allure.title('Запускаем браузер, закрываем браузер')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()


