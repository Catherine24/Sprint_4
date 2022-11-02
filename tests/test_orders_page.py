import allure
import re
from selenium import webdriver
from pages.orders_page import OrdersPage


class TestHeaderOrder:
    driver: webdriver

    @allure.title('Проверяем правильно оформленный заказ через кнопку "Заказать" в хедере')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_header_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        orders_page = OrdersPage(driver)
        orders_page.accept_cookie()
        orders_page.click_on_button_order()
        orders_page.find_element_and_click_input_name()
        orders_page.input_name_in()
        orders_page.find_element_and_click_input_surname()
        orders_page.input_surname_in()
        orders_page.find_element_and_click_input_address()
        orders_page.input_address_in()
        orders_page.find_and_click_metro_station()
        orders_page.wait_before_choose_station()
        orders_page.click_on_metro_station()
        orders_page.find_and_click_phone_number()
        orders_page.input_phone_number_in()
        orders_page.click_next_button()
        orders_page.find_and_click_when_to_bring_scooter()
        orders_page.choose_when_to_bring_scooter()
        orders_page.find_and_click_rental_period()
        orders_page.choose_rental_period()
        orders_page.choose_color_of_scooter()
        orders_page.click_order_button()
        orders_page.click_yes_button()
        orders_page.wait_to_proceed_banner()

        assert re.match(orders_page.order_text_pattern_1, orders_page.order_get_text()) is not None

    @allure.title('Проверяем правильно оформленный заказ через кнопку "Заказать" в теле страницы')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_button_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        orders_page = OrdersPage(driver)
        orders_page.accept_cookie()
        orders_page.click_on_button_order()
        orders_page.find_element_and_click_input_name()
        orders_page.input_name_in()
        orders_page.find_element_and_click_input_surname()
        orders_page.input_surname_in()
        orders_page.find_element_and_click_input_address()
        orders_page.input_address_in()
        orders_page.find_and_click_metro_station()
        orders_page.wait_before_choose_station()
        orders_page.click_on_metro_station()
        orders_page.find_and_click_phone_number()
        orders_page.input_phone_number_in()
        orders_page.click_next_button()
        orders_page.find_and_click_when_to_bring_scooter()
        orders_page.choose_when_to_bring_scooter()
        orders_page.find_and_click_rental_period()
        orders_page.choose_rental_period()
        orders_page.choose_color_of_scooter()
        orders_page.click_order_button()
        orders_page.click_yes_button()
        orders_page.wait_to_proceed_banner()
        assert re.match(orders_page.order_text_pattern_1, orders_page.order_get_text()) is not None

    @allure.title('Проверяем что при нажатии на логотип Яндекса открывается редирект')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Яндекса')
    def test_link_yandex_logo(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        orders_page = OrdersPage(driver)
        orders_page.accept_cookie()
        orders_page.click_on_yandex_logo()
        orders_page.driver.switch_to.window(orders_page.driver.window_handles[1])
        orders_page.wait_to_open_dzen_window()
        assert orders_page.current_url() == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверяем что при нажатии на логотип Самоката, открывается главная страница Самоката')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Самоката')
    def test_link_scooter_logo(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        orders_page = OrdersPage(driver)
        orders_page.accept_cookie()
        orders_page.click_on_button_order()
        orders_page.click_on_logo_scooter()
        assert orders_page.current_url() == 'https://qa-scooter.praktikum-services.ru/'


