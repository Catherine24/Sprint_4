import allure
import re
import pytest
from selenium import webdriver
from pom.orders_pom import HeaderOrderPom


class TestHeaderOrder:
    driver: webdriver

    @allure.title('Запускаем браузер и принимаем куки, закрываем браузер')
    @pytest.fixture
    def header_order_pom(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('https://qa-scooter.praktikum-services.ru/')
        header_order_pom = HeaderOrderPom(driver)
        header_order_pom.accept_cookie()
        yield header_order_pom
        driver.quit()

    @allure.title('Проверяем правильно оформленный заказ через кнопку "Заказать" в хедере')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_header_order(self, header_order_pom):
        order_text_pattern = (r"Заказ оформлен\n"
                              r"Номер заказа: \d+.  Запишите его:\n"
                              r"пригодится, чтобы отслеживать статус")
        header_order_pom.order_from_header_button()
        assert re.match(order_text_pattern, header_order_pom.order_get_text()) is not None

    @allure.title('Проверяем правильно оформленный заказ через кнопку "Заказать" в теле страницы')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_button_order(self, header_order_pom):
        order_text_pattern = (r"Заказ оформлен\n"
                              r"Номер заказа: \d+.  Запишите его:\n"
                              r"пригодится, чтобы отслеживать статус")
        header_order_pom.order_from_button()
        assert re.match(order_text_pattern, header_order_pom.order_get_text()) is not None

    @allure.title('Проверяем что при нажатии на логотип Яндекса открывается редирект')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Яндекса')
    def test_link_yandex_logo(self, header_order_pom):
        header_order_pom.url_from_logo_yandex()
        assert header_order_pom.current_url() == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверяем что при нажатии на логотип Самоката, открывается главная страница Самоката')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Самоката')
    def test_link_scooter_logo(self, header_order_pom):
        header_order_pom.url_from_logo_scooter()
        assert header_order_pom.current_url() == 'https://qa-scooter.praktikum-services.ru/'


