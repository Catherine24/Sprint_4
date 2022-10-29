import allure
import pytest
from selenium import webdriver
from pom.main_page_pom import MainPage


class TestMainPageFAQ:
    driver: webdriver

    @allure.title('Запускаем браузер и принимаем куки, закрываем браузер')
    @pytest.fixture
    def main_page_pom(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page_pom = MainPage(driver)
        main_page_pom.click_popup_cookies()
        yield MainPage(driver)
        driver.quit()

    @allure.title('Проверка первого выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки первого выпадающего списка, ответ на вопрос = Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    def test_click_accordion_heading_button_0(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_0()
        assert main_page_pom.get_text_accordion_heading_0() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка второго выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки второго выпадающего списка, ответ на вопрос = Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    def test_click_accordion__heading_button_1(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_1()
        assert main_page_pom.get_text_accordion_heading_1() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка третьего выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки третьего выпадающего списка, ответ на вопрос = Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    def test_click_accordion__heading_button_2(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_2()
        assert main_page_pom.get_text_accordion_heading_2() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка четвертого выпадающего списка')
    @allure.description('Последовательное выполнение шагов для четвертого выпадающего списка, ответ на вопрос = Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
    def test_click_accordion__heading_button_3(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_3()
        assert main_page_pom.get_text_accordion_heading_3() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка пятого выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки пятого выпадающего списка, ответ на вопрос = Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')
    def test_click_accordion__heading_button_4(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_4()
        assert main_page_pom.get_text_accordion_heading_4() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка шестого выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки шестого выпадающего списка, ответ на вопрос = Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    def test_click_accordion__heading_button_5(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_5()
        assert main_page_pom.get_text_accordion_heading_5() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка седьмого выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки седьмого выпадающего списка, ответ на вопрос = Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')
    def test_click_accordion__heading_button_6(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_6()
        assert main_page_pom.get_text_accordion_heading_6() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка восьмого выпадающего списка')
    @allure.description('Последовательное выполнение шагов для проверки восьмого выпадающего списка, ответ на вопрос = Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    def test_click_accordion__heading_button_7(self, main_page_pom):
        main_page_pom.process_click_accordion_heading_button_7()
        assert main_page_pom.get_text_accordion_heading_7() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

