import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    driver = None

    accordion__heading_button_0 = [By.ID, 'accordion__heading-0']
    accordion__heading_button_1 = [By.ID, 'accordion__heading-1']
    accordion__heading_button_2 = [By.ID, 'accordion__heading-2']
    accordion__heading_button_3 = [By.ID, 'accordion__heading-3']
    accordion__heading_button_4 = [By.ID, 'accordion__heading-4']
    accordion__heading_button_5 = [By.ID, 'accordion__heading-5']
    accordion__heading_button_6 = [By.ID, 'accordion__heading-6']
    accordion__heading_button_7 = [By.ID, 'accordion__heading-7']
    pop_up_agreement_cookies = [By.ID, 'rcc-confirm-button']
    check_accordion__heading_button_0_text = [By.ID, 'accordion__panel-0']
    check_accordion__heading_button_1_text = [By.ID, 'accordion__panel-1']
    check_accordion__heading_button_2_text = [By.ID, 'accordion__panel-2']
    check_accordion__heading_button_3_text = [By.ID, 'accordion__panel-3']
    check_accordion__heading_button_4_text = [By.ID, 'accordion__panel-4']
    check_accordion__heading_button_5_text = [By.ID, 'accordion__panel-5']
    check_accordion__heading_button_6_text = [By.ID, 'accordion__panel-6']
    check_accordion__heading_button_7_text = [By.ID, 'accordion__panel-7']
    text_accordion_heading_0 = ('Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    text_accordion_heading_1 = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    text_accordion_heading_2 = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    text_accordion_heading_3 = ('Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
    text_accordion_heading_4 = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')
    text_accordion_heading_5 = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    text_accordion_heading_6 = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')
    text_accordion_heading_7 = ('Да, обязательно. Всем самокатов! И Москве, и Московской области.')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принимаем куки')
    def click_popup_cookies(self):
        self.driver.find_element(*self.pop_up_agreement_cookies).click()

    @allure.step('Жмакаем на первую кнопку')
    def click_accordion_heading_button_0(self):
        self.driver.find_element(*self.accordion__heading_button_0).click()

    @allure.step('Жмакаем на вторую кнопку')
    def click_accordion_heading_button_1(self):
        self.driver.find_element(*self.accordion__heading_button_1).click()

    @allure.step('Жмакаем на третью кнопку')
    def click_accordion_heading_button_2(self):
        self.driver.find_element(*self.accordion__heading_button_2).click()

    @allure.step('Жмакаем на четвертую кнопку')
    def click_accordion_heading_button_3(self):
        self.driver.find_element(*self.accordion__heading_button_3).click()

    @allure.step('Жмакаем на пятую кнопку')
    def click_accordion_heading_button_4(self):
        self.driver.find_element(*self.accordion__heading_button_4).click()

    @allure.step('Жмакаем на шестую кнопку')
    def click_accordion_heading_button_5(self):
        self.driver.find_element(*self.accordion__heading_button_5).click()

    @allure.step('Жмакаем на седьмую кнопку')
    def click_accordion_heading_button_6(self):
        self.driver.find_element(*self.accordion__heading_button_6).click()

    @allure.step('Жмакаем на восьмую кнопку')
    def click_accordion_heading_button_7(self):
        self.driver.find_element(*self.accordion__heading_button_7).click()

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_0(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_0_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_1(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_1_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_2(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_2_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_3(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_3_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_4(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_4_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_5(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_5_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_6(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_6_text))

    @allure.step('Ждем появления нужного текста')
    def wait_accordion_heading_button_7(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.check_accordion__heading_button_7_text))

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_0(self):
        return self.driver.find_element(*self.check_accordion__heading_button_0_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_1(self):
        return self.driver.find_element(*self.check_accordion__heading_button_1_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_2(self):
        return self.driver.find_element(*self.check_accordion__heading_button_2_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_3(self):
        return self.driver.find_element(*self.check_accordion__heading_button_3_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_4(self):
        return self.driver.find_element(*self.check_accordion__heading_button_4_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_5(self):
        return self.driver.find_element(*self.check_accordion__heading_button_5_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_6(self):
        return self.driver.find_element(*self.check_accordion__heading_button_6_text).text

    @allure.step('Сравниваем текст')
    def get_text_accordion_heading_7(self):
        return self.driver.find_element(*self.check_accordion__heading_button_7_text).text


